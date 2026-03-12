import json
import pickle
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


# Load training data
with open("intents.json", "r") as f:
    data = json.load(f)

sentences = []
labels = []

# Collect patterns and their tags
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        sentences.append(pattern.lower())
        labels.append(intent["tag"])

print("Loaded", len(sentences), "training samples")
print("Classes:", list(set(labels)))


# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    sentences,
    labels,
    test_size=0.2,
    random_state=42
)


# Convert text to TF-IDF features
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),     # use single words and two-word phrases
    max_features=1000,
    sublinear_tf=True
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


# Train logistic regression model
model = LogisticRegression(
    max_iter=1000,
    C=5,
    solver="lbfgs"
)

model.fit(X_train_vec, y_train)


# Evaluate the model
y_pred = model.predict(X_test_vec)

accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", round(accuracy * 100, 1), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Save the trained model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("classes.pkl", "wb") as f:
    pickle.dump(list(set(labels)), f)

print("\nModel saved to model.pkl")
print("Vectorizer saved to vectorizer.pkl")
print("Training complete")