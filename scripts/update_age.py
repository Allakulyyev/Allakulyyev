from datetime import datetime

def calculate_age(birth_date: datetime) -> int:
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def update_age_in_files(age: int, files: list):
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content.replace("[AGE]", str(age))

        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)

def run_age_update():
    birth_date = datetime(1996, 7, 4)
    age = calculate_age(birth_date)
    files = ["README.md"]
    update_age_in_files(age, files)
