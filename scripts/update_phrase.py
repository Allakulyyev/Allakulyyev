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

PHRASES_RU = [
    "Работает — не трогай. Не работает — тоже не трогай. Вдруг заработает.",
    "Чем больше понимаю код, тем меньше понимаю заказчика.",
    "Коммент в коде: // не спрашивай как это работает.",
    "Когда багов нет — это не успех. Это иллюзия.",
    "Поменял одну строчку — пересобирается вся вселенная.",
    "Продакшн — как карма: всё, что ты накосячил в прошлом, вернётся.",
    "Мой стиль кодинга: пока работает — не объясняй",
    "Сохраняй спокойствие. Git всё помнит.",
    "Чужой код — это как чужая философия: понять можно, принять — сложно.",
    "Чужой код — это как чужая философия: понять можно, принять — сложно.."
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
    phrase_ru = get_phrase_by_day(PHRASES_RU)

    update_file_placeholder("README.md", "[DAILY_PHRASE]", phrase_en)
    update_file_placeholder("README.ru.md", "[DAILY_PHRASE_RU]", phrase_ru)
