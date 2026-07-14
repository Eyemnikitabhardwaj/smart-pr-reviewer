class RiskCalculator:
    def calculate_risk(self, analysis):
        score = 0

        if not analysis.get("syntax_valid", True):
            score += 50

        complexity = analysis.get("complexity", 0)

        if complexity > 20:
            score += 30
        elif complexity > 10:
            score += 20
        elif complexity > 5:
            score += 10

        maintainability = analysis.get(
            "maintainability_index",
            100
        )

        if maintainability < 20:
            score += 30
        elif maintainability < 50:
            score += 20
        elif maintainability < 70:
            score += 10

        for issue in analysis.get("sql_issues", []):
            severity = issue.get("severity", "").upper()

            if severity == "HIGH":
                score += 50
            elif severity == "MEDIUM":
                score += 20
            elif severity == "LOW":
                score += 5

        score = min(score, 100)

        if score >= 70:
            level = "HIGH"
        elif score >= 40:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            "risk_score": score,
            "risk_level": level
        } 