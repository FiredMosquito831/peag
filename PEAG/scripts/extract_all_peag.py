"""Extract ALL PEAG MCQs from ALL 8 files in custom folder - ALL questions regardless of correct markers."""
import re, json
from pathlib import Path

SRC = Path("docx md format extract by me")

def clean(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t)
    t = re.sub(r'\[(.+?)\]\{\.mark\}', r'\1', t)
    t = re.sub(r'!\[.*?\]\(.*?\)', '', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'&nbsp;', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    t = t.replace('\xad', '')
    return t

questions = []
seen = set()

def add_q(q_text, answers, source=""):
    if len(answers) < 2:
        return
    key = q_text[:80].lower()
    if key not in seen:
        seen.add(key)
        questions.append({"question": q_text, "answers": answers})

# FILE 1: raspunsuri_peag.md (Moodle)
with open(SRC / "raspunsuri_peag.md", "r", encoding="utf-8") as f:
    content = f.read()
blocks = re.split(r'\*\*(\d+)\*\*\s*intrebare', content)
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
    if len(q_text) < 10:
        continue
    ans_pat = re.compile(r'([a-eA-E])\.?\.\s+([^\n]+)')
    answers_raw = ans_pat.findall(block)
    correct_match = re.search(r'Răspunsul corect este:\s*(.+?)(?:\n|$)', block)
    correct_text = clean(correct_match.group(1)) if correct_match else ""
    answers = []
    for letter, ans in answers_raw:
        ac = clean(ans)
        if not ac:
            continue
        al, cl = ac.lower().rstrip(), correct_text.lower().rstrip()
        ic = (al == cl or al.startswith(cl) or cl.startswith(al))
        answers.append({"text": ac, "isCorrect": ic})
    add_q(q_text, answers, "F1")
print(f"F1 raspunsuri_peag.md: {len(questions)}")

# FILE 2: PEAG quzzies.md (inline Corect markers)
with open(SRC / "PEAG quzzies.md", "r", encoding="utf-8") as f:
    content = f.read()
paragraphs = re.split(r'\n\n+', content)
i = 0
while i < len(paragraphs):
    para = paragraphs[i].strip()
    if para.startswith('**CAP.'):
        i += 1; continue
    q_match = re.match(r'^(\d+)\.\s*(.*)', para, re.DOTALL)
    if not q_match:
        i += 1; continue
    q_text = clean(q_match.group(2))
    if len(q_text) < 5:
        i += 1; continue
    answers = []
    j = i + 1
    while j < len(paragraphs):
        ap = paragraphs[j].strip()
        am = re.match(r'^([a-eA-E])\.?\s*(.*)', ap, re.DOTALL)
        if not am:
            break
        at = clean(am.group(2))
        if at:
            ic = bool(re.search(r'\(.*(?:corect|CORECT).*\)', at, re.IGNORECASE)) or bool(re.search(r'\*\*.*(?:corect|CORECT).*\*\*', at, re.IGNORECASE))
            answers.append({"text": at, "isCorrect": ic})
        j += 1
    add_q(q_text, answers, "F2")
    i = j if j > i + 1 else i + 1
print(f"F2 PEAG quzzies.md: {len(questions)}")

# FILE 3: PEAG GRILE.md (study notes: **N. text** with -options)
with open(SRC / "PEAG GRILE.md", "r", encoding="utf-8") as f:
    content = f.read()
q_blocks = re.split(r'\*\*(\d+[\.)]\s+[^*]+)\*\*', content)
i = 1
while i + 1 < len(q_blocks):
    q_header = q_blocks[i]
    following = q_blocks[i + 1]
    q_text = re.sub(r'\d+[\.)]\s*', '', q_header).strip()
    q_text = re.sub(r'\s*\([\d,\s]+\s*rasp[^\)]*\)', '', q_text)
    q_text = clean(q_text).strip()
    if len(q_text) < 5:
        i += 2; continue
    options = re.findall(r'^[-]\s+(.+)$', following, re.MULTILINE)
    answers = [{"text": clean(o), "isCorrect": False} for o in options if clean(o)]
    add_q(q_text, answers, "F3")
    i += 2
print(f"F3 PEAG GRILE.md: {len(questions)}")

# FILE 4: Peag Exam.md (study notes)
with open(SRC / "Peag Exam.md", "r", encoding="utf-8") as f:
    content = f.read()
q_blocks = re.split(r'\*\*(\d+[\.)]\s+[^*]+)\*\*', content)
i = 1
while i + 1 < len(q_blocks):
    q_header = q_blocks[i]
    following = q_blocks[i + 1]
    q_text = re.sub(r'\d+[\.)]\s*', '', q_header).strip()
    q_text = re.sub(r'\s*\([\d,\s]+\s*rasp[^\)]*\)', '', q_text)
    q_text = clean(q_text).strip()
    if len(q_text) < 5:
        i += 2; continue
    options = re.findall(r'^[-]\s+(.+)$', following, re.MULTILINE)
    answers = [{"text": clean(o), "isCorrect": False} for o in options if clean(o)]
    add_q(q_text, answers, "F4")
    i += 2
print(f"F4 Peag Exam.md: {len(questions)}")

# FILE 5: GRILE PEAG USCATU si nu numai.md (paragraph-based Q+A, no correct markers)
with open(SRC / "GRILE PEAG USCATU si nu numai.md", "r", encoding="utf-8") as f:
    content = f.read()
paragraphs = re.split(r'\n\n+', content)
i = 0
while i < len(paragraphs):
    para = paragraphs[i].strip()
    if para.startswith('**GRILE'):
        i += 1; continue
    q_match = re.match(r'^(\d+)\\\.\s*(.*)', para, re.DOTALL)
    if not q_match:
        q_match = re.match(r'^(\d+)\.\s*(.*)', para, re.DOTALL)
    if not q_match:
        i += 1; continue
    q_text = clean(q_match.group(2))
    if len(q_text) < 5:
        i += 1; continue
    answers = []
    j = i + 1
    while j < len(paragraphs):
        ap = paragraphs[j].strip()
        am = re.match(r'^([a-eA-E])\\\.\s*(.*)', ap, re.DOTALL)
        if not am:
            am = re.match(r'^([a-eA-E])\.\s*(.*)', ap, re.DOTALL)
        if not am:
            break
        at = clean(am.group(2))
        if at:
            answers.append({"text": at, "isCorrect": False})
        j += 1
    add_q(q_text, answers, "F5")
    i = j if j > i + 1 else i + 1
print(f"F5 GRILE PEAG USCATU.md: {len(questions)}")

# FILE 6: Exemple subiecte afisate - mai 2021 (1).md (sequential numbering)
with open(SRC / "Exemple subiecte afisate - mai 2021 (1).md", "r", encoding="utf-8") as f:
    content = f.read()
lines = content.strip().split('\n')
current_question = None
current_answers = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    qm = re.match(r'^(\d+)\.\s+(.*)', line)
    if not qm:
        continue
    text = qm.group(2)
    if current_question is None:
        current_question = clean(text)
    elif current_answers and len(text) > 30:
        add_q(current_question, current_answers, "F6")
        current_question = clean(text)
        current_answers = []
    else:
        ct = clean(text)
        if ct:
            ct = re.sub(r'^\d+\.\s*', '', ct)
            current_answers.append({"text": ct, "isCorrect": False})
if current_question and current_answers and len(current_answers) >= 2:
    add_q(current_question, current_answers, "F6")
print(f"F6 Exemple subiecte.md: {len(questions)}")

# FILE 7: Grile.md (questions with options)
with open(SRC / "Grile.md", "r", encoding="utf-8") as f:
    content = f.read()
paragraphs = re.split(r'\n\n+', content)
i = 0
while i < len(paragraphs):
    para = paragraphs[i].strip()
    if "Alegeți" in para or para.startswith('**'):
        i += 1; continue
    if len(para) > 30 and not re.match(r'^[a-eA-E]\.', para):
        q_text = clean(para)
        answers = []
        j = i + 1
        while j < len(paragraphs):
            ap = paragraphs[j].strip()
            am = re.match(r'^([a-eA-E])\.\s*(.*)', ap)
            if not am:
                break
            at = clean(am.group(2))
            if at:
                answers.append({"text": at, "isCorrect": False})
            j += 1
        add_q(q_text, answers, "F7")
    i += 1
print(f"F7 Grile.md: {len(questions)}")

# FILE 8: grile profa OCR Reader.md (Moodle)
with open(SRC / "grile profa OCR Reader.md", "r", encoding="utf-8") as f:
    content = f.read()
blocks = re.split(r'\*\*(\d+)\*\*\s*întrebare', content)
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
    if len(q_text) < 10:
        continue
    ans_pat = re.compile(r'([a-eA-E])\.?\.\s+([^\n]+)')
    answers_raw = ans_pat.findall(block)
    correct_match = re.search(r'Răspunsul corect este:\s*(.+?)(?:\n|$)', block)
    correct_text = clean(correct_match.group(1)) if correct_match else ""
    answers = []
    for letter, ans in answers_raw:
        ac = clean(ans)
        if not ac:
            continue
        al, cl = ac.lower().rstrip(), correct_text.lower().rstrip()
        ic = (al == cl or al.startswith(cl) or cl.startswith(al))
        answers.append({"text": ac, "isCorrect": ic})
    add_q(q_text, answers, "F8")
print(f"F8 grile profa OCR Reader.md: {len(questions)}")

# Assign IDs
for idx, q in enumerate(questions, 1):
    q["id"] = idx

output = {"id": "peag", "name": "Evolutive Programming Algorithms", "questions": questions}

OUT = Path("Website/data/sets/peag.json")
OUT2 = Path("Website/sets/peag.json")
for p in [OUT, OUT2]:
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

multi = sum(1 for q in questions if sum(1 for a in q["answers"] if a["isCorrect"]) > 1)
single = sum(1 for q in questions if sum(1 for a in q["answers"] if a["isCorrect"]) == 1)
none = sum(1 for q in questions if sum(1 for a in q["answers"] if a["isCorrect"]) == 0)

print(f"\nTotal: {len(questions)} unique questions from ALL 8 files")
print(f"  Single-answer: {single}, Multi-answer: {multi}, No correct marked: {none}")
print(f"Output: {OUT}")
