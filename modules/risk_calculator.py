class RiskCalculator:
    def calculate_risk(self, analysis):
        score = 0

        complexity = analysis.get("complexity", 0)
        maintainability = analysis.get("maintainability_index", 100)
        syntax_valid = analysis.get("syntax_valid", True)

        if not syntax_valid:
            score += 50

        if complexity > 20:
            score += 30
        elif complexity > 10:
            score += 20
        elif complexity > 5:
            score += 10

        if maintainability < 20:
            score += 30
        elif maintainability < 50:
            score += 20
        elif maintainability < 70:
            score += 10

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