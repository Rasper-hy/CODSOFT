# Credit Card Fraud Detection using Logistic Regression
# Run in Google Colab

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 1. Load dataset
url = "https://raw.githubusercontent.com/joaopauloschuler/kaggle-credit-fraud/master/creditcard.csv"
df = pd.read_csv(url)

# 2. Features and target
X = df.drop("Class", axis=1)
y = df["Class"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train model
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# 5. Predictions and evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
