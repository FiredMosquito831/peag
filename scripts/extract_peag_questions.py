"""
Extract ALL PEAG MCQ questions from ALL _extract.md files.

Output: PEAG/Website/data/sets/peag.json
"""

import re
import json
from pathlib import Path

PEAG_DIR = Path(__file__).parent
OUTPUT_FILE = PEAG_DIR / "Website" / "data" / "sets" / "peag.json"


def clean(text):
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\[(.+?)\]\{\.mark\}', r'\1', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace('\xad', '')
    return text


def parse_moodle(fpath):
    """Format: **N** intrebare ... Raspunsul corect este: X"""
    if not fpath.exists():
        return []
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    questions = []
    blocks = re.split(r'\*\*(\d+)\*\*\s*intrebare', content)
    # Also try Romanian characters
    blocks += re.split(r'\*\*(\d+)\*\*\s*întrebare', content)

    for block in blocks:
        q_match = re.search(r'(.*?)\n+Alegeți o opțiune:', block, re.DOTALL)
        if not q_match:
            continue

        q_raw = q_match.group(1)
        q_raw = re.sub(r'(?:Corect|Incorect)\s*\n+', '\n', q_raw)
        q_raw = re.sub(r'Marcat [\d,]+ din [\d,]+\s*\n+', '\n', q_raw)
        q_raw = re.sub(r'Întrebare cu flag\s*\n+', '', q_raw)
        q_raw = re.sub(r'Textul întrebării\s*\n+', '', q_raw)
        q_text = clean(q_raw).strip()

        if not q_text or len(q_text) < 10:
            continue

        ans_pattern = re.compile(r'([a-eA-E])\.?\.\s+([^\n]+)')
        answer_matches = ans_pattern.findall(block)
        correct_match = re.search(r'Răspunsul corect este:\s*(.+?)(?:\n|$)', block)
        correct_text = clean(correct_match.group(1)) if correct_match else ""

        if q_text and answer_matches:
            answers = []
            for letter, ans in answer_matches:
                ans_clean = clean(ans)
                if not ans_clean:
                    continue
                is_correct = False
                if correct_text:
                    al = ans_clean.lower().rstrip()
                    cl = correct_text.lower().rstrip()
                    if al == cl or al.startswith(cl) or cl.startswith(al):
                        is_correct = True
                answers.append({"text": ans_clean, "isCorrect": is_correct})

            if len(answers) >= 2 and any(a["isCorrect"] for a in answers):
                questions.append({"question": q_text, "answers": answers})
    return questions


def parse_mark_file(fpath):
    r"""Format: [a. text]{.mark} = correct, a\. text = normal. Questions: N\. text"""
    if not fpath.exists():
        return []
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    questions = []

    # Split into paragraphs (answers are on separate paragraphs)
    paragraphs = re.split(r'\n\n+', content)

    i = 0
    while i < len(paragraphs):
        para = paragraphs[i].strip()

        # Question starts with N\. or N.
        q_match = re.match(r'^(\d+)\\\.\s*(.*)', para, re.DOTALL)
        if not q_match:
            q_match = re.match(r'^(\d+)\.\s*(.*)', para, re.DOTALL)

        if not q_match:
            i += 1
            continue

        q_text = clean(q_match.group(2))
        if len(q_text) < 5:
            i += 1
            continue

        # Collect answer paragraphs
        answers = []
        j = i + 1
        while j < len(paragraphs):
            ans_para = paragraphs[j].strip()

            # Check answer formats: a\. text, a. text, or [a. text]{.mark}
            ans_match = re.match(r'^([a-eA-E])\\\.\s*(.*)', ans_para, re.DOTALL)
            if not ans_match:
                ans_match = re.match(r'^([a-eA-E])\.\s*(.*)', ans_para, re.DOTALL)
            if not ans_match:
                ans_match = re.match(r'^\s*\[([a-eA-E])\.\s*(.+?)\]\{\.mark\}$', ans_para, re.DOTALL)

            if not ans_match:
                break

            ans_text = clean(ans_match.group(2))
            if ans_text:
                is_marked = '{.mark}' in paragraphs[j]
                answers.append({"text": ans_text, "isCorrect": is_marked})
            j += 1

        if len(answers) >= 2 and any(a["isCorrect"] for a in answers):
            questions.append({"question": q_text, "answers": answers})

        i = j if j > i + 1 else i + 1

    return questions


def parse_study_notes(fpath):
    """Study notes: **N. Question text (answer hints)** with -option lines"""
    if not fpath.exists():
        return []
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    questions = []
    q_blocks = re.split(r'\*\*(\d+[\.)]\s+[^*]+)\*\*', content)

    i = 1
    while i + 1 < len(q_blocks):
        q_header = q_blocks[i]
        following_text = q_blocks[i + 1]

        q_text = re.sub(r'\d+[\.)]\s*', '', q_header).strip()
        q_text = re.sub(r'\s*\([\d,\s]+\s*rasp[^\)]*\)', '', q_text)
        q_text = clean(q_text).strip()

        if len(q_text) < 5:
            i += 2
            continue

        options = re.findall(r'^[-•]\s+(.+)$', following_text, re.MULTILINE)

        if options and len(options) >= 2:
            answers = []
            for opt in options:
                opt_clean = clean(opt).strip()
                if opt_clean:
                    answers.append({"text": opt_clean, "isCorrect": False})

            if len(answers) >= 2:
                questions.append({"question": q_text, "answers": answers})

        i += 2
    return questions


def main():
    print("Parsing ALL PEAG MCQ sources...")

    all_questions = []
    seen = set()

    sources = [
        ("raspunsuri_peag_extract.md", parse_moodle, "Moodle"),
        ("Exemple subiecte afisate - mai 2021 (1)_extract.md", parse_mark_file, "{.mark}"),
        ("GRILE PEAG USCATU si nu numai_extract.md", parse_mark_file, "{.mark}"),
        ("grile profa OCR Reader_extract.md", parse_moodle, "Moodle OCR"),
        ("Grile_extract.md", parse_mark_file, "{.mark}"),
        ("Peag Exam_extract.md", parse_study_notes, "Study notes"),
        ("PEAG GRILE_extract.md", parse_study_notes, "Study notes"),
        ("PEAG quzzies_extract.md", parse_mark_file, "{.mark}"),
        ("THE_ULTIMATE_GRILE_ADUNATE_SI_CULESE_CU_DRAG_SI_BUCURIE_DE_PE_LA_TOTI_SI_TOATE_extract.md", parse_mark_file, "{.mark}"),
    ]

    for fname, parser, desc in sources:
        fpath = PEAG_DIR / fname
        try:
            qs = parser(fpath)
            print(f"  {fname[:55]:55s} {desc:15s} {len(qs)} questions")

            for q in qs:
                key = q["question"][:80].lower()
                if key not in seen:
                    seen.add(key)
                    all_questions.append(q)
        except Exception as e:
            print(f"  {fname[:55]:55s} {desc:15s} ERROR: {e}")

    for idx, q in enumerate(all_questions, 1):
        q["id"] = idx

    output = {
        "id": "peag",
        "name": "Evolutive Programming Algorithms",
        "questions": all_questions
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nTotal unique: {len(all_questions)} questions")

    multi = sum(1 for q in all_questions if sum(1 for a in q["answers"] if a["isCorrect"]) > 1)
    single = sum(1 for q in all_questions if sum(1 for a in q["answers"] if a["isCorrect"]) == 1)
    none = sum(1 for q in all_questions if sum(1 for a in q["answers"] if a["isCorrect"]) == 0)

    print(f"  Single-answer: {single}")
    print(f"  Multi-answer: {multi}")
    print(f"  No answer marked: {none}")


if __name__ == "__main__":
    main()
