import json
from pathlib import Path 

DATA_FILE= Path("data/students.txt")

def _ensure_file()-> None:
    '''This Function Ensures the file and directory if not there it will create it '''
    DATA_FILE.parent.mkdir(parents= True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("",encoding="utf-8")

def load_students() -> list[dict]:
    '''Loads All the students(One JSON OBject per line)'''
    _ensure_file()
    students=[]
    with open(DATA_FILE, encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if line:
                students.append(json.loads(line))
    return students

def save_students(students: list[dict]):
    "Write all Students back to the file "
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for student in students:
            f.write(json.dumps(student)+ "\n")
