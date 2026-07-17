import pandas as pd

from diabetes_readmission.ingest.load_data import load_data


def test_load_data():
    """Test the load_data function."""
    df = load_data()

    # Check if the returned object is a pandas DataFrame
    assert isinstance(df, pd.DataFrame), "The returned object is not a pandas DataFrame."

    # Check if the DataFrame has the expected number of rows and columns
    assert df.shape[0] == 101766
    assert df.shape[1] == 48