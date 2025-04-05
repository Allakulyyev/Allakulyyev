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

def update_file_placeholder(filename, placeholder, phrase):
    """Replace placeholder with phrase in given file"""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content.replace(placeholder, phrase)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)

def run_phrase_update():
    phrase_en = get_phrase_by_day(PHRASES_EN)
    update_file_placeholder("README.md", "[DAILY_PHRASE]", phrase_en)  # ← убраны лишние скобки
