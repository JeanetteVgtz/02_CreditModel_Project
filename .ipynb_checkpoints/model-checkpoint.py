# ---------------------------------------------------------------
# CREDIT MODEL PROJECT | JEANETTE VALENZUELA GUTIÉRREZ
# ---------------------------------------------------------------
# - Dataset: train.csv (provided by professor)
# - Goal: Train a Credit Risk Model and assign personalized interest rates
# ---------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, roc_curve

sns.set(style="whitegrid", palette="viridis")
plt.rcParams["figure.figsize"] = (8,5)

# ---------------------------------------------------------------
# Load dataset
# ---------------------------------------------------------------
df = pd.read_csv("train.csv")
print("Dataset shape:", df.shape)
print(df.head())

# Fill NaNs and encode categoricals
for col in df.select_dtypes(include=["float", "int"]).columns:
    df[col].fillna(df[col].median(), inplace=True)
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# Split data
target_col = "loan_status"
X = df.drop(columns=[target_col])
y = df[target_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Logistic Regression
log_reg = LogisticRegression(max_iter=10000)
log_reg.fit(X_train_scaled, y_train)
y_pred_lr = log_reg.predict(X_test_scaled)
y_proba_lr = log_reg.predict_proba(X_test_scaled)[:,1]
acc_lr = accuracy_score(y_test, y_pred_lr)
auc_lr = roc_auc_score(y_test, y_proba_lr)
print(f"\n📈 Logistic Regression → Accuracy: {acc_lr:.3f} | AUC: {auc_lr:.3f}")

# Random Forest
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
y_proba_rf = rf.predict_proba(X_test)[:,1]
acc_rf = accuracy_score(y_test, y_pred_rf)
auc_rf = roc_auc_score(y_test, y_proba_rf)
print(f"🌲 Random Forest → Accuracy: {acc_rf:.3f} | AUC: {auc_rf:.3f}")

# Assign interest rates based on PD
df["PD"] = log_reg.predict_proba(scaler.transform(X))[:,1]
BASE_RATE = 0.218
ALPHA_PD = 0.30
df["Final_Rate"] = (BASE_RATE + ALPHA_PD * df["PD"]).clip(upper=0.55)
df["Risk_Segment"] = pd.cut(df["PD"], bins=[0,0.2,0.4,0.6,0.8,1],
                            labels=["Muy Bajo","Bajo","Medio","Alto","Muy Alto"])

rate_summary = df.groupby("Risk_Segment")[["PD","Final_Rate"]].mean().sort_values(by="PD")
print("\nTasas promedio por nivel de riesgo:")
print(rate_summary)

# Save results
df.to_excel("Credit_Model_Results.xlsx", index=False)
print("\n✅ Archivo exportado: Credit_Model_Results.xlsx")

# Optional: plot if running interactively
if __name__ == "__main__":
    sns.histplot(df["PD"], bins=30, color="skyblue")
    plt.title("Distribución de Probabilidad de Default (PD)")
    plt.show()
