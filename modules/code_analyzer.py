import ast
from radon.complexity import cc_visit
from radon.metrics import mi_visit


class CodeAnalyzer:
    def analyze_code(self, code):
        result = {
            "syntax_valid": True,
            "syntax_error": None,
            "complexity": 0,
            "maintainability_index": 0,
            "functions": 0,
            "classes": 0,
            "lines_of_code": 0,
        }

        if not code or not code.strip():
            return result

        result["lines_of_code"] = len(code.splitlines())

        try:
            tree = ast.parse(code)

            result["functions"] = sum(
                isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                for node in ast.walk(tree)
            )

            result["classes"] = sum(
                isinstance(node, ast.ClassDef)
                for node in ast.walk(tree)
            )

            complexity_blocks = cc_visit(code)

            result["complexity"] = sum(
                block.complexity for block in complexity_blocks
            )

            result["maintainability_index"] = round(
                mi_visit(code, multi=True), 2
            )

        except SyntaxError as error:
            result["syntax_valid"] = False
            result["syntax_error"] = str(error)

        except Exception as error:
            result["syntax_valid"] = False
            result["syntax_error"] = f"Analysis failed: {str(error)}"

        return result