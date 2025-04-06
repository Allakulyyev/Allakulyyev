import datetime

PHRASES_EN = [
    "Whitespace is my syntax.",
    "Code reads like poetry… until you see the imports",
    "Python doesn’t force structure. It politely suggests it.",
    "Every problem can be solved with a decorator. Or made worse.",
    "It's not a bug, it's a feature in disguise",
    "I'm not lazy — I'm just highly optimized",
    "Code. Break. Fix. Repeat.",
    "My IDE autoformats. My soul doesn’t.",
    "It worked yesterday. I changed nothing. It’s broken now.",
    "The cleaner the code, the dirtier the commit history.",
    "Deadlines are just goals written in denial.",
    "Security is when even you can’t access your own system.",
    "The system is stable. That’s what scares me.",
    "Yes, I use dark mode",    
]

def get_phrase_by_day(phrases):
    """Return a phrase based on the day of the year"""
    index = datetime.datetime.now().timetuple().tm_yday % len(phrases)
    return phrases[index]

def update_phrase_html_line(filename, new_phrase):
    """Replace the <h3 align="center">...</h3> line with the new phrase"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        if line.strip().startswith('<h3 align="center">') and line.strip().endswith('</h3>'):
            updated_lines.append(f'<h3 align="center">{new_phrase}</h3>\n')
        else:
            updated_lines.append(line)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

def run_phrase_update():
    phrase_en = get_phrase_by_day(PHRASES_EN)
    update_phrase_html_line("README.md", phrase_en)
    print(f"Phrase updated to {phrase_en}")
