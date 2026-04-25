from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')


def split_into_chunks(text, chunk_size=200):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def compute_similarity(resume_text, jd_text):
    resume_chunks = split_into_chunks(resume_text)

    jd_embedding = model.encode([jd_text])[0]

    scores = []

    for chunk in resume_chunks:
        emb = model.encode([chunk])[0]
        score = cosine_similarity([emb], [jd_embedding])[0][0]
        scores.append(score)

    return max(scores) if scores else 0.0
