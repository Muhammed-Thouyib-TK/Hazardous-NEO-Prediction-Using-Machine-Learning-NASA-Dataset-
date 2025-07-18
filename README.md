# ☄️ Hazardous NEO Prediction Using Machine Learning (NASA Dataset)

> Binary classification of hazardous Near-Earth Objects (NEOs) using NASA data and supervised machine learning models like Logistic Regression and Random Forest.

In this project, I developed a machine learning pipeline to predict hazardous Near-Earth Objects (NEOs) using real-world astronomical data from NASA. With a focus on binary classification, the project walks through a complete ML workflow—from data cleaning to model evaluation—offering insights into how AI can support planetary defense and space research.

## 📌 Key Highlights of the Project

### ➡ Data Loading & Preprocessing
- Loaded NASA's Near-Earth Object dataset (1910–2024)
- Dropped non-informative columns like `neo_id`, `name`, and `orbiting_body`
- Encoded boolean features (`is_sentry_object`, `is_hazardous`) to numeric format
- Cleaned dataset by handling nulls with `dropna()`

### ➡ Exploratory Data Analysis (EDA)
- Visualized the class distribution of hazardous vs. non-hazardous objects
- Detected class imbalance, revealing potential classification challenges
- Used bar plots and summary statistics for feature understanding

### ➡ Model Building
- Trained two supervised ML models:
  - 🔹 **Logistic Regression** – Baseline linear model
  - 🔹 **Random Forest Classifier** – Robust ensemble model

### ➡ Model Evaluation
- Evaluated models using:
  - 🔸 Accuracy Score
  - 🔸 Confusion Matrix
  - 🔸 Classification Report (Precision, Recall, F1-Score)
- Observed that Random Forest outperformed Logistic Regression, especially in identifying hazardous objects (minority class)

## 🛠 Tools & Technologies Used
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Scikit-learn for ML modeling and evaluation
- Jupyter Notebook for development and exploration

## 🔭 Conclusion
This project demonstrates how supervised machine learning models can classify potentially hazardous space objects using real astronomical data. The Random Forest model, in particular, delivered strong performance for imbalanced binary classification, supporting further research in planetary defense and space risk mitigation.
