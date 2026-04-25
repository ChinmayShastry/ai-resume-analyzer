from config import SCORING_WEIGHTS

def calculate_score(similarity, gap, section_quality=0.5):

    skill_score = gap["match_percentage"] / 100

    components = {
        "skills": SCORING_WEIGHTS["skills_match"] * skill_score,
        "similarity": SCORING_WEIGHTS["semantic_similarity"] * similarity,
        "format": SCORING_WEIGHTS["format_quality"] * section_quality
    }

    final_score = sum(components.values())

    return round(final_score * 100, 2), components
