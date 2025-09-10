import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Step 1: Load Data

df = pd.read_excel("dataset.xlsx")  

# Drop missing values
df = df.dropna()


# Step 2: Visualization

# Distribution of categories
sns.countplot(x="status_dynamic", data=df)
plt.title("Distribution of Safety Categories")
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(
    df[["upstream_water_level","downstream_water_level","inflow_rate","outflow_rate","dynamic_storage"]].corr(), 
    annot=True, cmap="coolwarm"
)
plt.title("Feature Correlations")
plt.show()


# Step 3: ML Model

X = df[["upstream_water_level","downstream_water_level","inflow_rate","outflow_rate"]]
y = df["status_dynamic"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Random Forest Classifier
clf = RandomForestClassifier(
    n_estimators=300, max_depth=12, random_state=42, class_weight="balanced"
)
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)


# Step 4: Evaluation

acc = accuracy_score(y_test, y_pred)
print(" Model Accuracy:", round(acc*100,2), "%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

from sklearn.metrics import ConfusionMatrixDisplay

# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Method 2: Seaborn heatmap (alternative, looks nicer)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
            xticklabels=clf.classes_, yticklabels=clf.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix Heatmap")
plt.show()

