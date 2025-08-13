import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'Budget_Million': [50, 30, 80, 20, 100, 60, 15, 200, 120, 10],
    'Duration_Minutes': [120, 90, 150, 85, 180, 110, 100, 160, 140, 95],
    'Votes_Thousands': [500, 150, 800, 120, 1500, 700, 80, 3000, 2000, 60],
    'Popularity_Score': [75, 50, 85, 45, 95, 70, 30, 99, 92, 25]
})

# Features & target
X = data[['Budget_Million', 'Duration_Minutes', 'Votes_Thousands']]
y = data['Popularity_Score']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions on test set
predictions = model.predict(X_test)

print("Budget | Duration | Votes -> Predicted Popularity")
for budget, duration, votes, pred in zip(X_test['Budget_Million'],
                                         X_test['Duration_Minutes'],
                                         X_test['Votes_Thousands'],
                                         predictions):
    print(f"${budget}M | {duration} min | {votes}k votes -> {pred:.1f}/100")

# User input prediction
print("\n--- Movie Popularity Prediction ---")
budget = float(input("Enter movie budget in million USD: "))
duration = float(input("Enter duration in minutes: "))
votes = float(input("Enter number of votes (in thousands): "))

user_pred = model.predict([[budget, duration, votes]])
print(f"Estimated Popularity Score: {user_pred[0]:.1f}/100")
