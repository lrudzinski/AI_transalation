from config import TOKEN
from transalation import TranslationService
import pytest

from long_text import scene_text


@pytest.fixture
def translator():
    endpoint = 'https://composer.opera-api.com/api/v1/prompts/translate'
    authorization_token = TOKEN
    return TranslationService(endpoint, authorization_token)


def test_basic_transalation(translator):
    selected_text = "how are you?"
    translated_text = translator.get_translation(selected_text)
    assert translated_text["message"] == "Jak się masz?"


def test_wrong_input(translator):
    selected_text = 123123
    translated_text = translator.get_translation(selected_text)
    assert translated_text != 200


def test_long_text(translator):
    translated_text = translator.get_translation(scene_text)
    assert translated_text['finish_reason'] == "length"


def test_empty_text(translator):
    selected_text = ''
    translated_text = translator.get_translation(selected_text)
    assert translated_text == ''


def test_phonetic(translator):
    selected_text = "Ho ar yoy"
    translated_text = translator.get_translation(selected_text)
    assert translated_text["message"] == "Jak się masz?"


def test_proper_name(translator):
    selected_text = "Wroclaw"
    translated_text = translator.get_translation(selected_text)
    assert translated_text["message"] == "Wrocław"


def test_nordish(translator):
    selected_text = "Hvor er Opera"
    translated_text = translator.get_translation(selected_text)
    assert translated_text["message"] == "Gdzie jest Opera."