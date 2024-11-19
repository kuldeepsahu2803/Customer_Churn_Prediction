import pandas as pd
from sklearn.metrics import classification_report

def evaluate_model(y_true, y_pred):
    """Generate evaluation metrics."""
    return classification_report(y_true, y_pred)

if __name__ == "__main__":
    # Example usage (ensure y_test and y_pred are loaded/generated appropriately)
    y_test = [0, 1, 0, 1, 0]
    y_pred = [0, 1, 0, 0, 0]

    report = evaluate_model(y_test, y_pred)
    print(report)
