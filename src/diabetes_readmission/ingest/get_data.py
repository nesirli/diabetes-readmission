import pandas as pd
from ucimlrepo import fetch_ucirepo

from diabetes_readmission.config import settings

raw_data_dir = settings.raw_data_dir
raw_data_dir.mkdir(parents=True, exist_ok=True)


def download_data() -> None:
    """Download the diabetes readmission dataset from the UCI Machine Learning Repository and save it locally."""
    dataset = fetch_ucirepo(id=296)

    X = dataset.data.features
    y = dataset.data.targets

    df = pd.concat([X, y], axis=1)
    df.to_csv(raw_data_dir / "diabetes_readmission.csv", index=False)


def load_data() -> pd.DataFrame:
    """Load the diabetes readmission dataset from the local CSV file."""
    df = pd.read_csv(raw_data_dir / "diabetes_readmission.csv")
    return df


if __name__ == "__main__":
    download_data()
    print(
        "Data downloaded and saved to:",
        settings.raw_data_dir / "diabetes_readmission.csv",
    )
