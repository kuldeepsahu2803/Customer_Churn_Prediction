import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_features(df, categorical_columns):
    """Encode categorical columns using Label Encoding."""
    encoder = LabelEncoder()
    for col in categorical_columns:
        df[col] = encoder.fit_transform(df[col])
    return df

if __name__ == "__main__":
    processed_data_path = "data/processed/cleaned_data.csv"
    feature_data_path = "data/processed/feature_data.csv"

    # Load data
    data = pd.read_csv(processed_data_path)

    # Encode categorical features
    categorical_cols = ["gender", "contract_type"]
    feature_data = encode_features(data, categorical_cols)

    # Save feature data
    feature_data.to_csv(feature_data_path, index=False)
    print(f"Feature data saved to {feature_data_path}")
