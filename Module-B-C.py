def search_synonym():
    """Поиск синонима по введенному слову с проверкой наличия"""
    word = input("Введите слово: ").strip().lower()
    
    # Проверка наличия слова в словаре
    if word in synonyms:
        print(f"Синоним слова '{word}': {synonyms[word]}")
    else:
        print(f"Слово '{word}' не найдено в лексиконе.")
        
        # Предложение добавить новое слово
        add = input("Хотите добавить это слово? (д/н): ").strip().lower()
        if add == 'д' or add == 'да':
            add_new_pair(word)

def add_new_pair(word=None):
    """Добавление новой пары слов-синонимов с проверкой существования"""
    
    # Простой пользовательский ввод
    if word is None:
        word = input("Введите новое слово: ").strip().lower()
    
    # Проверка, существует ли уже такое слово
    if word in synonyms:
        print(f"Слово '{word}' уже есть в лексиконе!")
        return
    
    synonym = input(f"Введите синоним для слова '{word}': ").strip().lower()
    
    # Добавление новой пары
    synonyms[word] = synonym
    print(f"✅ Пара '{word} - {synonym}' успешно добавлена!")
    