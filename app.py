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

repo_path = st.text_input(
    "Enter local Git repository path"
)

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

            if not diff:
                st.warning("No code changes detected.")

            else:
                analyzer = CodeAnalyzer()
                analysis = analyzer.analyze_code(open("app.py", "r", encoding="utf-8").read())

                sql_validator = SQLValidator()
                sql_analysis = sql_validator.analyze(diff)

                risk_calculator = RiskCalculator()
                risk = risk_calculator.calculate_risk(analysis)

                ai_engine = AIEngine(Config.GEMINI_API_KEY)
                ai_review = ai_engine.review_code(
                    diff,
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
                    analysis,
                    risk
                )

                st.success(
                    f"Report generated: {report_path}"
                ) 