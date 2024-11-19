import pandas as pd

def load_data(filepath):
    """Load the dataset."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Clean the dataset by handling missing values, removing duplicates, etc."""
    df = df.drop_duplicates()
    df.fillna(df.mean(), inplace=True)
    return df

if __name__ == "__main__":
    raw_data_path = "data/raw/customer_data.csv"
    processed_data_path = "data/processed/cleaned_data.csv"

    # Load and clean data
    data = load_data(raw_data_path)
    cleaned_data = clean_data(data)

    # Save cleaned data
    cleaned_data.to_csv(processed_data_path, index=False)
    print(f"Processed data saved to {processed_data_path}")
