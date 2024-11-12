# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace with the correct path to your dataset)
url = 'C:/Users/User/OneDrive/Desktop/final project.py/heart.csv'  # Corrected file path
data = pd.read_csv(url)  # Load dataset (no need to define column names if already present)

# Display basic info and check for missing values
print(data.info())  # Show basic info about the dataset
print(data.isnull().sum())  # Check for missing values

# Preprocessing the data
# Convert categorical variables to numeric using pd.get_dummies (One-Hot Encoding)
# Check if these columns exist in the dataset, otherwise modify accordingly.
data = pd.get_dummies(data, columns=['cp', 'restecg', 'slope', 'thal'], drop_first=True)

# Define features and target
X = data.drop('target', axis=1)  # Features (drop the target column)
y = data['target']  # Target variable (heart disease presence)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling (Standardization)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit the scaler on the training data and transform it
X_test_scaled = scaler.transform(X_test)  # Use the same scaler to transform the test data

# Initialize the model (Random Forest Classifier)
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Model Evaluation
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Visualize the Confusion Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', 
            xticklabels=['No Heart Disease', 'Heart Disease'], 
            yticklabels=['No Heart Disease', 'Heart Disease'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Feature Importance (Optional but useful to understand which features affect the prediction)
features = X.columns  # Feature names
importances = model.feature_importances_  # Importance of each feature
indices = np.argsort(importances)[::-1]  # Sort the feature importance in descending order

# Plot Feature Importance
plt.figure(figsize=(10, 6))
plt.title('Feature Importance')
plt.barh(range(len(indices)), importances[indices], align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()

