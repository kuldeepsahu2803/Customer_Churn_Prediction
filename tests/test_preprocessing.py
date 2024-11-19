import pandas as pd
from src.data_preprocessing import clean_data

def test_clean_data():
    """
    Test the clean_data function to ensure it correctly handles missing values
    and removes duplicates.
    """
    raw_data = pd.DataFrame({
        "Column1": [1, 2, None, 4],
        "Column2": ["A", "B", "B", "B"]
    })
    
    cleaned_data = clean_data(raw_data)
    
    # Check if there are no missing values
    assert cleaned_data.isnull().sum().sum() == 0, "Missing values remain after cleaning."
    
    # Check if duplicates are removed
    assert cleaned_data.shape[0] == len(raw_data.drop_duplicates()), "Duplicates not removed correctly."
