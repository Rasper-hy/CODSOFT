# Titanic Survival Prediction - No installation required
# Simple rule-based version (not ML)

import csv
import urllib.request

# 1. Download Titanic dataset from GitHub
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]

# 2. Read data
data = list(csv.DictReader(lines))

# 3. Simple rule-based survival prediction:
#    Rule: Females survived more often, higher class survived more
def predict_survival(passenger):
    if passenger["Sex"].lower() == "female":
        return 1  # Survived
    elif passenger["Pclass"] == "1" and float(passenger["Age"] or 0) < 50:
        return 1
    else:
        return 0

# 4. Test the rule on the dataset
correct = 0
total = 0

for p in data:
    if p["Survived"]:  # Skip empty rows
        total += 1
        if predict_survival(p) == int(p["Survived"]):
            correct += 1

print(f"Rule Accuracy: {correct/total:.2%}")

# 5. Try predicting a new passenger
sample_passenger = {
    "Sex": "male",
    "Pclass": "3",
    "Age": "25"
}
print("Prediction for sample passenger:",
      "Survived" if predict_survival(sample_passenger) else "Did not survive")
