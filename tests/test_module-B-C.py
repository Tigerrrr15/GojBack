import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Замените 'src.synonym_module' на реальный путь к вашему файлу
from src.synonym_module import add_new_pair, synonyms


# Фикстура для очистки глобального словаря перед каждым тестом
@pytest.fixture(autouse=True)
def clear_synonyms():
    synonyms.clear()
    yield
    synonyms.clear()


def test_add_new_pair_обычный_случай():
    """Тест: проверка работы функции на корректных данных"""
    # Arrange (подготовка)
    входные_данные = "счастье"
    # side_effect передает ответы для каждого вызова input() внутри функции
    mocked_inputs = ["радость"]

    ожидаемый_результат_в_словаре = "радость"

    # Act (действие)
    # Подменяем input, чтобы он возвращал "радость", и print, чтобы он ничего не выводил в консоль
    with (
        patch("builtins.input", side_effect=mocked_inputs),
        patch("builtins.print") as mock_print,
    ):
        add_new_pair(входные_данные)

    # Assert (проверка)
    # Проверяем, что слово реально добавилось в глобальный словарь
    фактический_результат = synonyms.get(входные_данные)
    assert фактический_результат == ожидаемый_результат_в_словаре

    # Дополнительно проверяем, что функция напечатала успех
    mock_print.assert_called_with("✅ Пара 'счастье - радость' успешно добавлена!")


def test_add_new_pair_граничный_случай():
    """Тест: проверка работы функции на граничных значениях"""
    # Arrange (подготовка)
    # Граничный случай: передаем пустую строку
    входные_данные = ""
    mocked_inputs = ["пустота"]
    ожидаемый_результат = "пустота"

    # Act & Assert (действие и проверка)
    with patch("builtins.input", side_effect=mocked_inputs), patch("builtins.print"):
        add_new_pair(входные_данные)

    assert synonyms[входные_данные] == ожидаемый_результат


def test_add_new_pair_исключение():
    """Тест: проверка, что функция выбрасывает исключение при некорректных данных"""
    некорректные_данные = "тест"

    # ВНИМАНИЕ: В исходном коде функция не выбрасывает ValueError сама по себе.
    # Чтобы strictly следовать вашему шаблону с pytest.raises(ValueError),
    # мы симулируем ситуацию, когда системный input() внезапно выдает ошибку.
    with patch("builtins.input", side_effect=ValueError("Системная ошибка ввода")):
        with pytest.raises(ValueError):
            add_new_pair(некорректные_данные)


# ==========================================
# Аналогичные тесты для функции search_synonym
# ==========================================


def test_search_synonym_обычный_случай():
    """Тест: проверка работы функции на корректных данных"""
    # Arrange (подготовка)
    synonyms["кот"] = "кошка"
    входные_данные = ["кот"]  # То, что введет "пользователь"
    ожидаемый_результат = "Синоним слова 'кот': кошка"

    # Act (действие)
    with (
        patch("builtins.input", side_effect=входные_данные),
        patch("builtins.print") as mock_print,
    ):
        search_synonym()
        # Извлекаем то, что функция попыталась напечатать
        фактический_результат = mock_print.call_args[0][0]

    # Assert (проверка)
    assert фактический_результат == ожидаемый_результат


def test_search_synonym_граничный_случай():
    """Тест: проверка работы функции на граничных значениях (слово отсутствует, отказ от добавления)"""
    # Arrange (подготовка)
    входные_данные = ["несуществующее_слово", "н"]  # Ввод слова + ответ "нет"
    ожидаемый_результат = "Слово 'несуществующее_слово' не найдено в лексиконе."

    # Act (действие)
    with (
        patch("builtins.input", side_effect=входные_данные),
        patch("builtins.print") as mock_print,
    ):
        search_synonym()
        фактический_результат = mock_print.call_args_list[0][0][0]

    # Assert (проверка)
    assert фактический_результат == ожидаемый_результат
    # Проверяем, что словарь не вырос
    assert len(synonyms) == 0


def test_search_synonym_исключение():
    """Тест: проверка, что функция пробрасывает исключение (симуляция ошибки ввода)"""
    некорректные_данные = [ValueError("Ошибка ввода")]

    with patch("builtins.input", side_effect=некорректные_данные):
        with pytest.raises(ValueError):
            search_synonym()
