synonyms = {
    "хороший": "отличный",
    "плохой": "ужасный",
    "большой": "огромный",
    "маленький": "крошечный",
    "быстрый": "скорый",
    "медленный": "неторопливый",
    "веселый": "радостный",
    "грустный": "печальный",
}


def show_menu():
    print("\n" + "=" * 40)
    print("ЛЕКСИКОН СИНОНИМОВ")
    print("=" * 40)
    print("1. Поиск синонима")
    print("2. Добавить новую пару")
    print("3. Показать все слова")
    print("4. Выход")
    print("=" * 40)


def show_all():
    if not synonyms:
        print("Лексикон пуст.")
        return

    print("\nВСЕ СЛОВА В ЛЕКСИКОНЕ:")
    print("-" * 30)

    for word in sorted(synonyms.keys()):
        print(f"{word:12} -> {synonyms[word]}")

    print("-" * 30)
    print(f"Всего пар: {len(synonyms)}")
