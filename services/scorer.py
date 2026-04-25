from config import SCORING_WEIGHTS

def calculate_score(similarity, gap, section_quality=0.5):
    """
    similarity: float (0–1)
    gap: dict from compute_gap()
    section_quality: placeholder (0–1), improve later
    """

    skill_score = gap["match_percentage"] / 100

    final_score = (
        SCORING_WEIGHTS["skills_match"] * skill_score +
        SCORING_WEIGHTS["semantic_similarity"] * similarity +
        SCORING_WEIGHTS["format_quality"] * section_quality
    )

    return round(final_score * 100, 2)
