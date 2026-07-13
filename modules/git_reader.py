from git import Repo
import os


class GitReader:
    def __init__(self, repo_path):
        self.repo = Repo(repo_path)

    def get_changed_files(self):
        changed_files = []

        for item in self.repo.index.diff(None):
            if item.a_path.endswith(".py"):
                changed_files.append(item.a_path)

        return changed_files

    def get_diff(self):
        code_parts = []

        for file_path in self.repo.git.ls_files("*.py").splitlines():
            full_path = os.path.join(
                self.repo.working_tree_dir,
                file_path
            )

            try:
                with open(full_path, "r", encoding="utf-8") as file:
                    code_parts.append(file.read())
            except Exception:
                pass

        return "\n\n".join(code_parts)

    def get_current_branch(self):
        return self.repo.active_branch.name 
    