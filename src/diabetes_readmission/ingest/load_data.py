import pandas as pd
from ucimlrepo import fetch_ucirepo

from diabetes_readmission.config import settings


def load_data() -> pd.DataFrame:
    """Load the diabetes readmission dataset from the UCI Machine Learning Repository."""

    # Fetch the dataset
    dataset = fetch_ucirepo(id=296)

    # Access features and targets
    X = dataset.data.features
    y = dataset.data.targets

    # Combine into a single pandas DataFrame
    df = pd.concat([X, y], axis=1)

    return df