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
        l = line.lower()

        if "education" in l:
            current_section = "education"
        elif "experience" in l or "work" in l:
            current_section = "experience"
        elif "project" in l:
            current_section = "projects"
        elif "skill" in l:
            current_section = "skills"

        sections[current_section] += line + "\n"

    return sections