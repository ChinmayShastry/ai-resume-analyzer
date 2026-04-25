def compute_similarity(resume_text, jd_text):
    resume_chunks = split_into_chunks(resume_text)

    jd_embedding = model.encode([jd_text])[0]

    scores = []
    for chunk in resume_chunks:
        emb = model.encode([chunk])[0]
        score = cosine_similarity([emb], [jd_embedding])[0][0]
        scores.append(score)

    return max(scores)
