from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityChecker:
    def calculate_similarity(self, code_a, code_b):
        if not code_a or not code_b:
            return 0.0

        try:
            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform([code_a, code_b])

            score = cosine_similarity(
                vectors[0:1],
                vectors[1:2]
            )[0][0]

            return round(float(score) * 100, 2)

        except ValueError:
            return 0.0