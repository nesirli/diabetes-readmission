from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from functools import lru_cache

ROOT_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(env_file=ROOT_DIR / ".env")

    data_dir: Path = ROOT_DIR / "data"
    plots_dir: Path = ROOT_DIR / "plots"
    best_params_dir: Path = data_dir / "best_params"

    mlflow_tracking_uri: str = f"sqlite:///{ROOT_DIR / 'data' / 'mlflow.db'}"
    mlflow_experiment_name: str = "diabetes_readmission"
    mlflow_model_name: str = "diabetes_readmission_model"
    mlflow_model_alias: str = "top_model"
    mlflow_artifact_location: Path = ROOT_DIR / "mlruns"


@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()