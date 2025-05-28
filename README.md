# 💳 Fraud Detection

A machine learning-based fraud detection system built to identify fraudulent financial transactions using real-world transaction data. The goal is to develop a reliable and efficient model that can flag suspicious activity with high precision and recall.

---

## 📌 Problem Statement

Financial fraud, especially in digital transactions, has become increasingly sophisticated, making early detection both critical and challenging. Traditional rule-based systems are no longer sufficient to catch all frauds while minimizing false alarms. This project aims to build an intelligent fraud detection model that leverages machine learning algorithms to effectively distinguish between legitimate and fraudulent transactions, ensuring both security and efficiency in real-world financial systems.

---

## 📂 Dataset Used

- **Source**: [Kaggle - PaySim Fraud Dataset](https://www.kaggle.com/datasets/ealaxi/paysim1/data)
- The dataset simulates mobile money transactions and includes features like transaction amount, type, and balance before and after the transaction.
- Class distribution is highly imbalanced, making it an excellent candidate for testing classification algorithms on rare event prediction.

---

## ⚙️ Tech Stack / Tools Used

- **Programming Language**: Python  
- **Libraries**: `scikit-learn`, `xgboost`, `pandas`, `numpy`, `matplotlib`, `seaborn`
- **Experiment Tracking**: `MLflow`
- **Frontend**: `Streamlit`
- **Model Selection Algorithms**: 
  - Logistic Regression  
  - Decision Tree  
  - Random Forest ✅ *(Selected for deployment)*  
  - SVM  
  - XGBoost  

---

## 🔬 Approach / Methodology

1. **Data Preprocessing**
   - Handling missing and irrelevant data
   - Encoding categorical variables
   - Dealing with class imbalance using appropriate techniques
2. **Model Training & Hyperparameter Tuning**
   - GridSearchCV was used for hyperparameter tuning across multiple models.
3. **Model Selection**
   - Random Forest and XGBoost showed similar performance, but **Random Forest** was chosen due to lower computational cost.
4. **Experiment Tracking**
   - All training runs and metrics were logged using **MLflow** for reproducibility and comparison.
5. **Interface**
   - A simple **Streamlit UI** was built to demonstrate model predictions.

---

## 📊 Best Model: Random Forest Classifier

**Hyperparameters:**

```json
{
  "criterion": "gini",
  "max_depth": 10,
  "min_samples_split": 1000,
  "n_estimators": 100
}



Evaluation Metrics:

Metric      	Value
Accuracy	    0.99998
Precision	    0.98735
Recall	        0.99757
F1 Score	    0.99243


## How to Run the Project
1. Clone the repository
    git clone https://github.com/yourusername/fraud-detection.git
    cd fraud-detection
2. Install Dependencies
    pip install -r requirements.txt
3. Run Streamlit App
    streamlit run app.py


##Future Improvements

1.Real-Time Prediction: Integrate the model with an API backend to accept live transaction data for 2.2/2.2.real-time fraud prediction.
3.Model Retraining Pipeline: Set up scheduled retraining based on new transaction data.
4.Feature Engineering: Add time-series behavior patterns, user profiling, and geolocation tracking.
5.¡Explainability: Integrate SHAP or LIME to explain model decisions and increase transparency.
