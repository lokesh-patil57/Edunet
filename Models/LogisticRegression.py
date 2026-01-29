import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
data = pd.read_csv('green_tech_data.csv')

data.head()

# Inspect for missing values and general structure
print(data.isnull().sum())

# Count plot to check if the data is balanced
sns.countplot(x='sustainability', data=data)
plt.title('Count of Sustainable vs Non-Sustainable Classes')
plt.xlabel('Sustainability')
plt.ylabel('Count')
plt.show()

# Example feature selection
X = data[['carbon_emissions', 'energy_output', 'renewability_index', 'cost_efficiency']]
y = data['sustainability']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)  # x_test is your actual data

y_pred

print(np.array(y_test))

# Accuracy Score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Not Sustainable', 'Sustainable'], 
            yticklabels=['Not Sustainable', 'Sustainable'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Classification Report
print(classification_report(y_test, y_pred, target_names=['Not Sustainable', 'Sustainable']))

# Feature importance
coefficients = pd.DataFrame(model.coef_.T, index=X.columns, columns=['Coefficient'])
print(coefficients)

import joblib
# Save the model to a file
joblib.dump(model, 'lrmodel_sustainable.pkl')

# Load the model from the file
model = joblib.load('lrmodel_sustainable.pkl')

# Example input data
# 181.089042	128.286267	0.642032	0.732568	1
input_data = np.array([[181.089042, 128.286267, 0.642032, 0.732568]])

# Make predictions
prediction = model.predict(input_data)

# Print the prediction
print("Predicted class:", prediction[0])

# Actual Energy Consumption = 1.703533