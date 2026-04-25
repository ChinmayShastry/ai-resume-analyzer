def compute_gap(resume_skills, jd_skills):
    resume_set = set([s.lower() for s in resume_skills])
    jd_set = set([s.lower() for s in jd_skills])

    missing_skills = list(jd_set - resume_set)
    matched_skills = list(jd_set & resume_set)

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(len(matched_skills) / len(jd_set) * 100, 2) if jd_set else 0
    }