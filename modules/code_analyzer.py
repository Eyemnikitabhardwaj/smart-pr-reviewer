import ast
import difflib
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
        def detect_duplicate_functions(function_sources):
    """
    function_sources: dict {function_name: function_code_string}
    Returns pairs of functions with high similarity (possible duplicates)
    """
    duplicates = []
    names = list(function_sources.keys())
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            ratio = difflib.SequenceMatcher(
                None, function_sources[names[i]], function_sources[names[j]]
            ).ratio()
            if ratio > 0.75:
                duplicates.append({
                    "function_1": names[i],
                    "function_2": names[j],
                    "similarity": round(ratio, 2),
                    "suggestion": f"Consider reusing '{names[i]}' instead of duplicating logic in '{names[j]}'"
                })
    return duplicates
