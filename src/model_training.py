import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(X_train, y_train):
    """Train a Random Forest model."""
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    feature_data_path = "data/processed/feature_data.csv"

    # Load data
    data = pd.read_csv(feature_data_path)
    X = data.drop(columns=["churn"])
    y = data["churn"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = train_model(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")
