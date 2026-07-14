import re


class SQLValidator:
    def analyze(self, code):
        issues = []

        sql_patterns = [
            r"\bSELECT\b.+?\bFROM\b",
            r"\bINSERT\s+INTO\b",
            r"\bUPDATE\b.+?\bSET\b",
            r"\bDELETE\s+FROM\b"
        ]

        contains_sql = any(
            re.search(pattern, code, re.IGNORECASE | re.DOTALL)
            for pattern in sql_patterns
        )

        if not contains_sql:
            return {
                "sql_detected": False,
                "issues": []
            }

        if re.search(r"SELECT\s+\*", code, re.IGNORECASE):
            issues.append({
                "type": "SELECT_STAR",
                "severity": "MEDIUM",
                "message": "Avoid SELECT *. Fetch only required columns."
            })

        if re.search(r"DELETE\s+FROM\s+\w+\s*;", code, re.IGNORECASE):
            issues.append({
                "type": "DELETE_WITHOUT_WHERE",
                "severity": "HIGH",
                "message": "DELETE query may be missing a WHERE clause."
            })

        if re.search(
            r"UPDATE\s+\w+\s+SET.+?;",
            code,
            re.IGNORECASE | re.DOTALL
        ):
            update_query = re.search(
                r"UPDATE\s+\w+\s+SET.+?;",
                code,
                re.IGNORECASE | re.DOTALL
            )

            if update_query and "WHERE" not in update_query.group().upper():
                issues.append({
                    "type": "UPDATE_WITHOUT_WHERE",
                    "severity": "HIGH",
                    "message": "UPDATE query may be missing a WHERE clause."
                })

        if re.search(r"ORDER\s+BY", code, re.IGNORECASE):
            issues.append({
                "type": "INDEX_REVIEW",
                "severity": "LOW",
                "message": "Review indexing for columns used in ORDER BY."
            })

        if re.search(r"\bJOIN\b", code, re.IGNORECASE):
            issues.append({
                "type": "JOIN_REVIEW",
                "severity": "LOW",
                "message": "Review indexes on JOIN columns."
            })

        return {
            "sql_detected": True,
            "issues": issues
        } 
def detect_n_plus_one(code_lines):
    """Heuristic: flags a query-like call found inside a loop block"""
    issues = []
    query_keywords = ["select", "query(", "execute(", ".filter(", ".get(", "cursor."]
    for i, line in enumerate(code_lines):
        stripped = line.strip().lower()
        if stripped.startswith("for ") or stripped.startswith("while "):
            for j in range(i + 1, min(i + 8, len(code_lines))):
                if any(k in code_lines[j].lower() for k in query_keywords):
                    issues.append({
                        "line": j + 1,
                        "issue": "Possible N+1 query pattern detected inside loop",
                        "severity": "MEDIUM"
                    })
                    break
    return issues
