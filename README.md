# Machine learning project

### Student Name: Dharmveer Singh

### Student Number: 69916

#### Description:

Project directory includes following files:

- **app.py**: A Flask API script used to serve the trained model for predictions. This script sets up an endpoint that takes input features and returns the predicted credit score.
- **best_svm_model.joblib**: The trained Support Vector Machine (SVM) model saved in a joblib file. This model is used for making predictions on new data.
- **requirements.txt**: A file listing all the dependencies and Python packages required to run the project. This includes Flask, scikit-learn, and any other libraries used in the project.

#### Running API:

```bash
python3 app.py
```

#### Curl request for test:

```
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{
"features": {
"Month": 7,
"Age": 23,
"Occupation": 1.0,
"Annual_Income": 50000,
"Monthly_Inhand_Salary": 4000,
"Num_Bank_Accounts": 3,
"Num_Credit_Card": 2,
"Interest_Rate": 0.1,
"Delay_from_due_date": 30,
"Num_of_Delayed_Payment": 2,
"Changed_Credit_Limit": 0,
"Num_Credit_Inquiries": 1,
"Credit_Mix": 0,
"Outstanding_Debt": 1,
"Credit_Utilization_Ratio": 0,
"Credit_History_Age": 10,
"Payment_of_Min_Amount": 0,
"Total_EMI_per_month": 0,
"Amount_invested_monthly": 1000,
"Payment_Behaviour": 0,
"Monthly_Balance": 0,
"Count_Auto Loan": 0,
"Count_Credit-Builder Loan": 0,
"Count_Personal Loan": 0,
"Count_Home Equity Loan": 0,
"Count_Not Specified": 0,
"Count_Mortgage Loan": 0,
"Count_Student Loan": 0,
"Count_Debt Consolidation Loan": 0,
"Count_Payday Loan": 0
}
}'
```
