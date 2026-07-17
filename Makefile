all:
	install validate_data test tune train evaluate promote inference

install:
	uv sync --all-extras

train:
	uv run python -m src.diabetes_readmission.models.train

tune:
	uv run python -m src.diabetes_readmission.models.tune

evaluate:
	uv run python -m src.diabetes_readmission.models.evaluate

promote:
	uv run python -m src.diabetes_readmission.models.promote

inference:
	uv run python -m src.diabetes_readmission.serving.inference

test:
	uv run pytest tests/

validate_data:
	uv run python -m src.diabetes_readmission.utils.validate_data

interpret:
	uv run python -m src.diabetes_readmission.models.interpret

serve-api:
	uv run uvicorn src.diabetes_readmission.app.main:app --reload

lint:
	uv run ruff check src tests --fix

format:
	uv run ruff format src tests