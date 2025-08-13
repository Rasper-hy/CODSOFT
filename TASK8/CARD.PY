import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

np.random.seed(42)
data = pd.DataFrame({
    'Transaction_Amount':
    np.random.uniform(1, 5000, 1000),
    'Transaction_Time':
    np.random.randint(0, 24, 1000),
    'Merchant_Rating':
    np.random.randint(1, 6, 1000),
    'Customer_Age':
    np.random.randint(18, 80, 1000),
    'Fraud':
    np.random.choice([0, 1], size=1000, p=[0.95, 0.05])
})

X = data.drop("Fraud", axis=1)
y = data["Fraud"]

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print(classification_report(y_test, y_pred))
