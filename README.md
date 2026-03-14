# ⚡ EV Remaining Range Prediction System (Machine Learning + Streamlit)

## 📌 Project Overview

This project builds a **Machine Learning Regression Model** to estimate the **remaining driving range of an Electric Vehicle (EV)** based on real experimental performance data.

The system uses:

* EV speed
* Distance already covered
* Current consumption
* Vehicle load
* Ambient temperature
* Gear transmission type

to predict the **Estimated Remaining Range (km)**.

A **Streamlit Web Dashboard** is also developed for real-time user interaction and prediction.

---

## 🎯 Problem Statement

Electric vehicle users often face **range anxiety** due to uncertain battery discharge behavior.

This project solves:

> “How much distance can the EV still travel under current operating conditions?”

The ML model learns battery drain patterns and predicts the **remaining range dynamically.**

---

## 📊 Dataset Description

The dataset is based on **experimental field trials on Electric 3-Wheelers** comparing:

* Conventional CY Gear
* Tork-Z Gearbox System

### Dataset includes:

* Speed vs Distance vs Current observations
* Vehicle load conditions
* Thermal parameters
* Electrical characteristics
* Environmental conditions

### Advanced Engineered Features

* Power Consumption (kW)
* Energy Consumption per km
* Efficiency Score
* Payload Ratio
* Thermal Stress Index
* Speed Degradation Rate

Synthetic variations of **load and ambient temperature** are added to improve ML generalization.

Final Dataset Size → **300+ rows**

---

## 🤖 Machine Learning Model

A **Linear Regression Model** is used to predict:

> **Remaining EV Range (km)**

### Target Variable

Remaining Range is calculated as:

```
Remaining Range = Maximum Range of Gear − Distance Covered
```

Where:

* CY Gear Max Range ≈ 112 km
* Tork-Z Gear Max Range ≈ 167 km

---

## 🧠 Features Used in Model

* Gear Type
* Speed
* Distance Covered
* Current Draw
* Battery Voltage
* Vehicle Load
* Efficiency Metrics
* Thermal Metrics
* Ambient Temperature
* Acceleration

---

## 🖥️ Streamlit Dashboard

The UI allows users to:

* Select Gear Type
* Enter Speed
* Enter Distance Covered
* Enter Current Consumption
* Set Vehicle Load
* Set Ambient Temperature

The system instantly predicts:

> ⚡ **Estimated Remaining Driving Range**

---

## ⚙️ Installation & Setup (Step-by-Step)

### 1️⃣ Clone or Download Project

```
git clone <repo-link>
cd project-folder
```

OR manually place files in one folder.

---

### 2️⃣ Create Virtual Environment

```
python -m venv ev_venv
```

---

### 3️⃣ Activate Environment

**Windows PowerShell**

```
ev_venv\Scripts\activate
```

---

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 5️⃣ Train Machine Learning Model

```
python train_linear_model.py
```

This will create:

* linear_ev_model.pkl
* gear_encoder.pkl
* model_columns.pkl

---

### 6️⃣ Run Streamlit Application

```
streamlit run app.py
```

Browser will open automatically.

---

## 📈 Model Performance

Typical performance:

* R² Score → 0.80 – 0.92
* MAE → 5–12 km

This makes the model suitable for:

* Research demonstrations
* EV analytics dashboards
* Range estimation prototypes

---

## 🚀 Future Improvements

* Random Forest / XGBoost model comparison
* Deep Learning range prediction
* Real-time battery drain visualization
* IoT integration with EV sensors
* Fleet optimization analytics
* Cloud deployment

---

## 📚 Research Significance

This project demonstrates:

* Physics-aware feature engineering
* Real experimental EV dataset usage
* Practical ML deployment via Streamlit
* Explainable baseline regression modeling

Suitable for:

* Conference submissions
* Academic projects
* Data science portfolios
* EV analytics research

---

## 👨‍💻 Author

EV Performance Analytics Project
Machine Learning + Energy Optimization Study

---

## ⭐ License

Open for academic and educational use
