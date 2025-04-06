from datetime import datetime

def calculate_age(birth_date: datetime) -> int:
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def update_age_in_files(age: int, files: list) -> bool:
    changed = False  

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            original_content = f.read()

        content = original_content.replace("[AGE]", str(age))

        lines = content.splitlines()
        updated_lines = []
        for line in lines:
            if line.strip().startswith('<p align="center">Age:'):
                updated_lines.append(f'<p align="center">Age: {age}</p>')
            else:
                updated_lines.append(line)

        final_content = "\n".join(updated_lines)

        if final_content != original_content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(final_content)
            changed = True

    return changed

def run_age_update():
    birth_date = datetime(1996, 7, 4)
    age = calculate_age(birth_date)
    files = ["README.md"]
    if update_age_in_files(age, files):
        print(f"[✅] Age updated to {age}")
    else:
        print("[ℹ️] Age already up-to-date, no changes made.")
