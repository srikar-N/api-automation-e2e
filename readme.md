# API Automation – E2E Pytest Framework

# API Automation – End-to-End Pytest Framework

This repository demonstrates a complete **end-to-end API automation test suite** built using **Python**, **Requests**, and **Pytest**.

It validates an API through the full CRUD lifecycle:
- **Create** (POST)
- **Read** (GET)
- **Update** (PUT)
- **Partial Update** (PATCH)
- **Delete** (DELETE)
- **Confirm Deletion** (GET returns 404)

The tests are structured for clarity, maintainability, and real-world usage.

---
## 📂 Project Structure
project_e2e/
├── Api/ # API request layer
│ └── objects.py
├── utils/ # Test data generation
│ └── payload.py
├── tests/ # Pytest test cases
│ └── test_e2e_objects.py
├── conftest.py # Pytest fixtures
├── pytest.ini # Marker declarations
├── requirements.txt # Dependencies
└── .gitignore


---

## 🚀 Features

✔ Clean separation of API layer and test logic  
✔ Pytest fixtures for setup/teardown  
✔ E2E test chaining  
✔ Dynamic payload generation  
✔ PATCH behavior validation  
✔ Registered markers (`@pytest.mark.e2e`)  
✔ HTML report generation

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/srikar-N/api-automation-e2e.git
cd api-automation-e2e
```

## Install dependencies:
pip install -r requirements.txt



## ▶️ How to Run Tests

## Run all tests:
pytest

## Run only E2E test:
pytest -m e2e

## Generate HTML report:
pytest --html=report.html --self-contained-html

## 📝 Notes

- The API under test has a "PATCH" behavior that overwrites the nested data object instead of merging it. The test suite asserts based on the actual API behavior, not assumptions.

- Tests are written to be clear, maintainable, and easy to extend.

- Created by Srikar N
GitHub – https://github.com/srikar-N
