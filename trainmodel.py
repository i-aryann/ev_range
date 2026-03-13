import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("EV_SUPER_ML_DATASET.csv")

# Target creation
df["max_range"] = df["gear_type"].map({
    "CY":112,
    "TorkZ":167
})

df["remaining_range"] = df["max_range"] - df["distance_km"]

# Encode gear
le = LabelEncoder()
df["gear_type"] = le.fit_transform(df["gear_type"])

# Features
X = df.drop(columns=["remaining_range","max_range"])
y = df["remaining_range"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred))
print("R2 Score:", r2_score(y_test, pred))

# Save model
joblib.dump(model, "linear_ev_model.pkl")
joblib.dump(le, "gear_encoder.pkl")
joblib.dump(X.columns, "model_columns.pkl")