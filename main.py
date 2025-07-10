import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle
import os

# 1. Membuat dataset sederhana
np.random.seed(42)
X = np.random.rand(100, 1) * 10
Y = 3 * X + np.random.randn(100, 1) * 2

# Membagi dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Melatih model
model = LinearRegression()
model.fit(X_train, Y_train)

# Prediksi
Y_pred = model.predict(X_test)

# Evaluasi
print(f"MSE: {mean_squared_error(Y_test, Y_pred):.2f}")
print(f"R²: {r2_score(Y_test, Y_pred):.2f}")

# Visualisasi futuristic
plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(X_test, Y_test, color="#00FFC6", edgecolors='white', s=60, label="Data Aktual")
ax.plot(X_test, Y_pred, color="#FF00D4", linewidth=2.5, label="Regresi Prediksi")
ax.set_facecolor('#0C3B5D')
fig.patch.set_facecolor('#0C3B5D')
ax.grid(color="#00FFC6", linestyle='--', linewidth=0.5, alpha=0.3)
ax.set_xlabel("X", color="#00FFC6")
ax.set_ylabel("Y", color="#00FFC6")
ax.set_title("Hasil Linear Regression (HUD Style)", color="#00FFC6")
ax.tick_params(axis='x', colors="#00FFC6")
ax.tick_params(axis='y', colors="#00FFC6")
ax.legend(facecolor="#122C44", edgecolor="#00FFC6", labelcolor="#00FFC6")
plt.tight_layout()
plt.savefig("regression_plot.png", dpi=150)
print("Plot futuristic disimpan sebagai 'regression_plot.png'")

# Simpan model
os.makedirs("models", exist_ok=True)
with open("models/linear_model.pkl", "wb") as f:
    pickle.dump(model, f)
