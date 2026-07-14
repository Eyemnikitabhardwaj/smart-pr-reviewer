# 🔍 Smart PR Reviewer
An AI-assisted Git pull request and code review system built using Python and Streamlit.

## 📌 Project Overview

Smart PR Reviewer is a developer-focused code analysis tool designed to analyze a local Git repository and identify potential code and database query issues.

The application performs static code analysis, SQL query validation, risk assessment, and automated report generation through a simple Streamlit interface.

## ✨ Features

- Git repository validation
- Current Git branch detection
- Python static code analysis
- Syntax validation and error detection
- Code complexity analysis
- Maintainability analysis
- Function and class counting
- Lines of code analysis
- SQL query detection
- SELECT * detection
- DELETE query without WHERE detection
- Index review recommendations
- N+1 query pattern detection (loop-based heuristic)
- Duplicate function detection using sequence similarity matching
- Automated risk score calculation
- LOW, MEDIUM and HIGH risk classification
- JSON review report generation
- Interactive Streamlit interface

## 🛠️ Technology Stack

- Python
- Streamlit
- GitPython
- Radon
- Git
- JSON

Token-efficient design: local static/heuristic checks run before any AI call, minimizing LLM token usage.

## 📂 Project Structure

```
smart-pr-reviewer/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── ai_engine.py
│   ├── code_analyzer.py
│   ├── git_reader.py
│   ├── git_validator.py
│   ├── report_generator.py
│   ├── risk_calculator.py
│   ├── similarity.py
│   └── sql_validator.py
│
├── sample_repo/
│   └── sample_code.py
│
└── reports/
```

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/Eyemnikitabhardwaj/smart-pr-reviewer.git

```

Move into the project directory:

```
cd smart-pr-reviewer
```

Install required dependencies:

```
pip install -r requirements.txt
```

## ▶️ Run the Application

Run the Streamlit application using:

```
python -m streamlit run app.py
```

The application will open in your web browser.

## 🔎 How to Use

1. Enter the path of a local Git repository.
2. Click **Analyze Repository**.
3. The application validates the Git repository.
4. The current Git branch is detected.
5. Python code is analyzed.
6. SQL queries are checked for potential issues.
7. A risk score and risk level are generated.
8. A JSON analysis report is saved in the reports directory.

## 📊 Analysis Output

The application displays:

### Static Analysis

- Syntax validity
- Syntax errors
- Code complexity
- Maintainability index
- Number of functions
- Number of classes
- Lines of code

### SQL Analysis

The SQL validator can identify issues such as:

- SELECT * usage
- DELETE queries without a WHERE clause
- Queries requiring index review
- Possible N+1 query patterns

### Risk Assessment

Detected code and SQL issues are used to calculate a risk score.

Risk levels:

- LOW
- MEDIUM
- HIGH

## Output
<img width="517" height="617" alt="image" src="https://github.com/user-attachments/assets/15f82bfd-b07a-4152-bf86-160336539035" />
<img width="442" height="401" alt="image" src="https://github.com/user-attachments/assets/4b2d5327-4bc0-439e-ad19-cbef4e0e722a" />


## 📄 Report Generation

After analysis, the application automatically generates a JSON report inside the `reports` directory.

The report contains code analysis and risk assessment results.

## 🚀 Future Enhancements

- GitHub API integration
- Automated pull request analysis
- Database schema and index analysis
- Advanced AI-based code review
- CI/CD pipeline integration

## 👩‍💻 Developer

**Nikita Bhardwaj**

GitHub: Eyemnikitabhardwaj

## 📌 Project Status

Working MVP developed for automated code and SQL risk analysis.

