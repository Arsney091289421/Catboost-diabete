
# Diabetes Prediction API Documentation

---

## 1. Decision to Use a Classification Model

For this project, I decided to build a classification model, similar to the approach used in **Assignment 3**. The goal is to predict the likelihood of diabetes based on user-provided medical and physical attributes.

---

## 2. Why Choose This Dataset?

Given the requirements for an API, it is more practical to work with a dataset containing fewer but highly relevant features. I chose the **Pima Indians Diabetes Dataset**, which contains eight clearly defined and effective features, making it a suitable choice for this prediction task.

---

## 3. Selected Dataset: Pima Indians Diabetes Dataset

The dataset includes the following features:
- **Pregnancies**: Number of pregnancies
- **Glucose**: Plasma glucose concentration (mg/dL)
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skinfold thickness (mm)
- **Insulin**: 2-hour serum insulin (mu U/mL)
- **BMI**: Body mass index (BMI = weight[kg]/height[m]^2)
- **DiabetesPedigreeFunction**: Diabetes pedigree function (genetic influence measure)
- **Age**: Age (years)

---

## 4. Handling Zero Values in the Data

Several features in the dataset (e.g., **Glucose**, **BloodPressure**) contain a significant number of zeros, which are likely to represent missing data. I decided to remove samples with zero values for the following reasons:
1. **Experimental Results**: Retaining zero values did not improve model performance.
2. **Real-World Relevance**: In real-life diabetes risk prediction, complete and accurate measurements are typically available, making it logical to discard these samples.

---

## 5. Data Splitting

- **Out-of-Sample Data (OOS)**: 0.04% of the dataset was set aside as out-of-sample data, used solely for endpoint testing. A smaller sample is sufficient for this purpose.
- **Train-Validation Split**: The remaining data was split into **80% for training and 20% for validation**, a common and reasonable ratio.

---

## 6. Feature Engineering

- **No Feature Engineering Performed**
- **Reason**: The dataset already includes eight carefully selected and highly relevant features. No additional features were needed.
- **Potential Impact**: While new feature generation could marginally improve performance in some cases, it is unlikely to provide significant benefits given the current dataset.

---

## 7. Feature Selection

- **No Feature Selection Performed**
- **Reason**: All eight features in the dataset are highly relevant to diabetes prediction. Removing any feature might result in information loss. Moreover, the dataset is relatively small, and feature selection is unnecessary.
- **Model Dependency**: CatBoost inherently handles feature importance effectively, eliminating the need for preselection.
- **Potential Impact**: While feature selection might be helpful for larger or more complex datasets, retaining all features is more beneficial for simplicity and interpretability in this case.

---

## 8. Hyperparameter Tuning

I used **Bayesian Optimization** for hyperparameter tuning:
- **Reason**: Compared to grid search, Bayesian optimization is more efficient and effective, especially in larger search spaces.
- **Outcome**: The optimal hyperparameters were saved directly in the pipeline.

---

## 9. Pipeline Structure

The final model was implemented as a pipeline:
- **Classifier**: CatBoostClassifier with optimal hyperparameters.
- **Scaler**: StandardScaler to normalize input features and improve performance.
- The pipeline ensures seamless integration of preprocessing and modeling steps.

---

## 10. Code Execution

The code leverages **FastAPI** to create an endpoint for diabetes prediction:
1. **Model**: A pre-trained CatBoost model predicts the probability of diabetes.
2. **Input**: Users provide eight specific medical and physical measurements.
3. **Output**: The API returns the probability of diabetes or no diabetes for the given input.

---

## 11. Requirements

To run the project locally, the following dependencies are required:
- Python 3.8+
- FastAPI
- Pandas
- Cloudpickle
- CatBoost

---

## 12. Quick Start Guide

1. Clone the project and navigate to the folder:
   ```bash
   git clone https://github.com/Arsney091289421/Catboost-diabete.git
   cd Catboost-diabete
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the API:
   ```bash
   uvicorn main:app --reload
   ```
5. Open the Swagger UI in a browser to test the endpoint:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## 13. Output Explanation

- **Prediction Output**: The API returns the probabilities for `Diabetes` and `No Diabetes` in percentage format.
- **Reason**: Probabilities provide a more intuitive understanding of diabetes risk compared to a binary classification.

---

## 14. Model Strengths and Weaknesses

**Strengths**:
- **Simplicity**: The pipeline and deployment are straightforward and easy to follow.
- **Ease of Deployment**: FastAPI integrates smoothly with the model, offering a seamless user experience.
- **Intuitive Outputs**: Both inputs and outputs are user-friendly and easy to understand.

**Weaknesses**:
- **Model Performance**: The accuracy on the out-of-sample test set is approximately **0.75**, leaving room for improvement.
- **Data Limitations**: The dataset is relatively small, which might limit the model’s generalization capabilities.

---

## 15. Challenges

1. **Feature Selection and Engineering**:
   - Initially, I attempted to implement custom feature selection and engineering.
   - **Problem**: These steps caused numerous compatibility and invocation errors.
   - **Solution**: After comparing results, I found these steps had minimal impact on performance and decided to omit them.

2. **Dataset Limitations**:
   - The dataset size is relatively small, which might limit the model’s potential.
   - **Solution**: While larger datasets could enhance model performance, no suitable alternatives were available for this task.
