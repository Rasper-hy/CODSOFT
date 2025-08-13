import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

np.random.seed(42)
data = pd.DataFrame({
    'Age': np.random.randint(18, 70, 100),
    'Monthly_Usage': np.random.randint(1, 100, 100),
    'Support_Calls': np.random.randint(0, 10, 100),
    'Tenure_Months': np.random.randint(1, 60, 100),
    'Churn': np.random.choice([0, 1], size=100)
})

X = data.drop("Churn", axis=1)
y = data["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print(classification_report(y_test, y_pred))
