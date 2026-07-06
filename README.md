# Automation-Testing

A robust automated testing framework built using Python and Pytest to ensure the reliability and performance of both API and UI functionalities. The repository is integrated with a modern CI/CD pipeline using GitHub Actions and features comprehensive visual reporting via Allure Reports.

---

## 🚀 Key Features

* **API Testing**: Automated validation of open-source REST APIs using Python's `requests` library.
* **UI Testing**: Comprehensive browser automation using Selenium WebDriver (configured for Chrome).
* **Test Isolation**: Implemented a tag-based execution strategy using custom Pytest markers (`@pytest.mark.api` and `@pytest.mark.ui`).
* **CI/CD Integration**: Separate, event-driven pipelines for continuous integration and automated deployment.
* **Allure Reports**: Rich, interactive visual reports deployed directly to GitHub Pages after every run.

---

## 📂 Project Structure
```text
.
├── .github/
│   └── workflows/
│       ├── ci.yml              # CI pipeline (Runs tests & uploads raw data)
│       └── cd.yml              # CD pipeline (Generates Allure Report & deploys)
├── tests/
│   ├── api/                    # API test suites (Open-source integrations)
│   └── ui/                     # UI test suites (Localhost environments)
├── reports/                    # Generated test artifacts and results
├── pytest.ini                  # Pytest configuration and custom markers
├── requirements.txt            # Project dependencies
└── README.md

```
---

## 🛠️ Tech Stack & Prerequisites

Language: Python 3.10+

Testing Core: Pytest

Reporting: Allure Framework

CI/CD: GitHub Actions

Hosting: GitHub Pages

---

## 🔧 Local Setup
### Clone the repository:

Bash
git clone [https://github.com/ThiKim148/Automation-Testing.git](https://github.com/ThiKim148/Automation-Testing.git)
cd Automation-Testing
Create and activate a virtual environment:

Bash
python -m venv venv

### On Windows:
.\venv\Scripts\activate

### On macOS/Linux:
source venv/bin/activate
Install dependencies:

### Bash
pip install --upgrade pip
pip install -r requirements.txt
🎯 Test Execution
Local Execution
You can filter and run test suites locally using custom Pytest markers:

### Run API Tests only:

#### Bash
python -m pytest -m api -v
Run UI Tests only (Requires local server to be active):

#### Bash
python -m pytest -m ui -v
Generate Allure Report Locally
To visualize test results on your local machine, execute the following commands:

#### Bash
Run tests and save raw data
python -m pytest -m api --alluredir=reports/allure-results

### Serve the interactive report
allure serve reports/allure-results

---

## 🔄 CI/CD & Deployment Workflow
The project utilizes a modern decoupled workflow using GitHub Actions native deployment, keeping the repository clean from extra ghost branches (like gh-pages).

Plaintext
[ Code Push / PR ] 
       │
       ▼
┌─────────────────────────────┐
│    Automation Testing CI    │ ──► Installs dependencies
│          (ci.yml)           │ ──► Executes API tests with '@pytest.mark.api'
└─────────────────────────────┘ ──► Uploads raw allure-results
       │
       ▼ (Triggers on completion)
┌─────────────────────────────┐
│       Allure Report CD      │ ──► Downloads raw allure-results
│          (cd.yml)           │ ──► Compiles results into static HTML
└─────────────────────────────┘ ──► Deploys directly to GitHub Pages
Live Test Reports
Every execution on the main branch automatically updates the live test dashboard.

---

## 📊 View the Live Allure Report: https://thikim148.github.io/Automation-Testing/


## 👤Author
Ho Thi Kim - Automation Testing

