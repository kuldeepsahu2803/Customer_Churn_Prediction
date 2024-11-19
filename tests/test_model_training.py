import pandas as pd
from src.model_training import train_model
from sklearn.ensemble import RandomForestClassifier

def test_train_model():
    """
    Test the train_model function to ensure it correctly trains a model.
    """
    X = pd.DataFrame({"Feature1": [1, 2, 3], "Feature2": [4, 5, 6]})
    y = pd.Series([0, 1, 0])
    
    model = train_model(X, y)
    
    # Check if the model is an instance of RandomForestClassifier
    assert isinstance(model, RandomForestClassifier), "Model is not of type RandomForestClassifier."
    
    # Check if the model has been trained
    assert hasattr(model, "feature_importances_"), "Model training failed."
