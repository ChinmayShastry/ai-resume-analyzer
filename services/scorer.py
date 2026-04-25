def calculate_score(similarity, gap, sections_quality=0.5):
    skill_score = gap["match_percentage"] / 100

    final_score = (
        0.4 * skill_score +
        0.4 * similarity +
        0.2 * sections_quality
    )

    return round(final_score * 100, 2)
