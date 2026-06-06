import pytest
from src.data_manager import synonyms, show_all

def test_synonyms_contains_initial_words():
    """Тест 1: проверка начального словаря"""
    expected_pairs = {
        "хороший": "отличный",
        "плохой": "ужасный",
        "большой": "огромный",
        "маленький": "крошечный",
        "быстрый": "скорый",
        "медленный": "неторопливый",
        "веселый": "радостный",
        "грустный": "печальный"
    }
    
    for word, synonym in expected_pairs.items():
        assert word in synonyms
        assert synonyms[word] == synonym
    
    assert len(synonyms) == 8


def test_show_all_output_empty_dict(capsys):
    """Тест 2: проверка вывода при пустом словаре"""
    original_synonyms = synonyms.copy()
    synonyms.clear()
    
    show_all()
    captured = capsys.readouterr()
    
    assert "Лексикон пуст" in captured.out
    
    synonyms.update(original_synonyms)


def test_show_all_output_non_empty(capsys):
    """Тест 3: проверка вывода при непустом словаре"""
    original_synonyms = synonyms.copy()
    synonyms.clear()
    synonyms.update({"тест1": "синоним1", "тест2": "синоним2"})
    
    show_all()
    captured = capsys.readouterr()
    
    assert "тест1" in captured.out
    assert "синоним1" in captured.out
    assert "Всего пар: 2" in captured.out
    
    synonyms.clear()
    synonyms.update(original_synonyms)