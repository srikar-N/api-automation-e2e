# API Automation – E2E Pytest Framework

This project demonstrates an end-to-end API automation framework built using **Python, Pytest, and Requests**.

## 🚀 What is covered
- End-to-end CRUD lifecycle testing
- POST → GET → PUT → PATCH → DELETE → GET (404)
- Dynamic test data generation
- Pytest fixtures for setup and teardown
- PATCH behavior validation based on real API contract
- Pytest markers for test categorization
- HTML report generation

## 🧪 Tech Stack
- Python
- Pytest
- Requests
- Pytest-HTML

## 📂 Project Structure
project_e2e/
├── Api/ # API request layer
├── utils/ # Payload generation
├── tests/ # Test cases
├── conftest.py # Pytest fixtures
├── pytest.ini # Marker registration


## ▶️ How to Run Tests

Install dependencies:
```bash
pip install -r requirements.txt
```

## Run all tests:
pytest

## Run only E2E test:
pytest -m e2e

## Generate HTML report:
pytest --html=report.html --self-contained-html

## 📝 Notes

- The "PATCH" API overwrites the nested data object instead of merging fields.

- Tests are written to validate actual API behavior, not assumptions.
