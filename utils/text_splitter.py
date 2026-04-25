SECTION_KEYWORDS = {
    "education": ["education", "academic", "qualification"],
    "experience": ["experience", "work", "employment", "internship"],
    "projects": ["project", "projects"],
    "skills": ["skills", "technologies", "tech stack"],
}


def detect_section(line: str):
    line_lower = line.lower()

    for section, keywords in SECTION_KEYWORDS.items():
        for keyword in keywords:
            if keyword in line_lower:
                return section

    return None


def split_resume_sections(text: str):
    sections = {
        "education": "",
        "experience": "",
        "projects": "",
        "skills": "",
        "other": ""
    }

    current_section = "other"

    lines = text.split("\n")

    for line in lines:
        detected = detect_section(line)

        if detected:
            current_section = detected
            continue

        sections[current_section] += line + "\n"

    return sections
