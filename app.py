import os
import streamlit as st

from config import Config
from modules.git_validator import GitValidator
from modules.git_reader import GitReader
from modules.code_analyzer import CodeAnalyzer
from modules.sql_validator import SQLValidator
from modules.risk_calculator import RiskCalculator
from modules.ai_engine import AIEngine
from modules.report_generator import ReportGenerator


st.set_page_config(
    page_title="Smart PR Reviewer",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Smart PR Reviewer")
st.write("AI-powered Git pull request and code review system")

repo_path = st.text_input("Enter local Git repository path")

if st.button("Analyze Repository"):

    if not repo_path:
        st.error("Please enter a repository path.")

    else:
        valid, message = GitValidator.validate_repository(repo_path)

        if not valid:
            st.error(message)

        else:
            st.success(message)

            reader = GitReader(repo_path)

            branch = reader.get_current_branch()
            diff = reader.get_diff()

            st.subheader("Current Branch")
            st.write(branch)

            sample_file = os.path.join(
                repo_path,
                "sample_repo",
                "sample_code.py"
            )

            if os.path.exists(sample_file):
                with open(
                    sample_file,
                    "r",
                    encoding="utf-8"
                ) as file:
                    code_content = file.read()
            else:
                code_content = diff

            analyzer = CodeAnalyzer()
            analysis = analyzer.analyze_code(code_content)

            sql_validator = SQLValidator()
            sql_analysis = sql_validator.analyze(code_content)

            risk_input = analysis.copy()
            risk_input["sql_issues"] = sql_analysis.get(
                "issues",
                []
            )

            risk_calculator = RiskCalculator()
            risk = risk_calculator.calculate_risk(risk_input)

            ai_engine = AIEngine(Config.GEMINI_API_KEY)

            ai_review = ai_engine.review_code(
                code_content,
                analysis
            )

            st.subheader("Static Analysis")
            st.json(analysis)

            st.subheader("SQL Analysis")
            st.json(sql_analysis)

            st.subheader("Risk Assessment")
            st.json(risk)

            st.subheader("AI Review")
            st.write(ai_review)

            report_generator = ReportGenerator(
                Config.REPORTS_DIR
            )

            report_path = report_generator.generate_report(
                repo_path,
                {
                    "static_analysis": analysis,
                    "sql_analysis": sql_analysis,
                    "ai_review": ai_review
                },
                risk
            )

            st.success(
                f"Report generated: {report_path}"
            ) 