from git import Repo, InvalidGitRepositoryError, NoSuchPathError


class GitValidator:
    @staticmethod
    def validate_repository(repo_path):
        try:
            repo = Repo(repo_path)

            if repo.bare:
                return False, "Bare repository is not supported."

            return True, "Valid Git repository."

        except NoSuchPathError:
            return False, "Repository path does not exist."

        except InvalidGitRepositoryError:
            return False, "Selected folder is not a Git repository."

        except Exception as error:
            return False, f"Git validation failed: {str(error)}"