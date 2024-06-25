import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# 1. Load the dataset and display the first few rows
data = pd.read_csv('sample_dataset.csv')
print(data.head())

# 2. Generate summary statistics
summary_stats = data.describe()
print(summary_stats)

# Calculate mean and standard deviation of Sepal Length
sepal_length_mean = data['Sepal Length (cm)'].mean()
sepal_length_std = data['Sepal Length (cm)'].std()
print(f"Sepal Length Mean: {sepal_length_mean}")
print(f"Sepal Length Standard Deviation: {sepal_length_std}")

# 3. Check for missing values and handle them
missing_values = data.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Handle missing values (if any)
data_filled = data.fillna(data.mean())
print("Missing values after filling:")
print(data_filled.isnull().sum())

# 4. Convert species labels to numerical values
species_mapping = {'FlowerA': 0, 'FlowerB': 1, 'FlowerC': 2}
data['Species'] = data['Species'].map(species_mapping)
print("Data with numerical species labels:")
print(data.head())

# 5. Split the dataset into training and testing sets
X = data.drop('Species', axis=1)
y = data['Species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
print(f"Training data size: {X_train.shape}")
print(f"Testing data size: {X_test.shape}")

# 6. Train a decision tree classifier
model = DecisionTreeClassifier(random_state=42, max_depth=3)
model.fit(X_train, y_train)

# 7. Visualize the trained decision tree
plt.figure(figsize=(20,10))
plot_tree(model, filled=True, feature_names=X.columns, class_names=['FlowerA', 'FlowerB', 'FlowerC'])
plt.show()

# 8. Predict the species for the testing data and compute the accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# 9. Generate a classification report and a confusion matrix
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=['FlowerA', 'FlowerB', 'FlowerC']))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
