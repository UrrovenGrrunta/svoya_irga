import pytest

from svoya_igra import game
from dataclasses import FrozenInstanceError


def test_question_stores_values():
    test_question = game.Question(
        id=1,
        topic="Games",
        text="Publisher of GTA series",
        answer="Rockstar Games",
        value=100
    )
    assert test_question.id == 1
    assert test_question.topic == "Games"
    assert test_question.text == "Publisher of GTA series"
    assert test_question.answer == "Rockstar Games"
    assert test_question.value == 100


def test_question_with_same_values_are_equal():
    test_question_one = game.Question(
        id = 1,
        topic = "Games",
        text = "Publisher of GTA series",
        answer = "Rockstar Games",
        value = 100
    )
    test_question_two = game.Question(
        id = 1,
        topic = "Games",
        text = "Publisher of GTA series",
        answer = "Rockstar Games",
        value = 100
    )
    assert test_question_one == test_question_two


def test_question_rejects_empty_topic():
    with pytest.raises(ValueError):
        test_question = game.Question(
            id=1,
            topic="",
            text="Publisher of GTA series",
            answer="Rockstar Games",
            value=100
        )


def test_question_rejects_whitespace_topic():
    with pytest.raises(ValueError):
        test_question = game.Question(
            id=1,
            topic="        ",
            text="Publisher of GTA series",
            answer="Rockstar Games",
            value=100
        )


def test_question_rejects_empty_text():
    with pytest.raises(ValueError):
        test_question = game.Question(
            id=1,
            topic="Games",
            text="",
            answer="Rockstar Games",
            value=100
        )


def test_question_rejects_empty_answer():
    with pytest.raises(ValueError):
        test_question = game.Question(
            id=1,
            topic="Games",
            text="Publisher of GTA series",
            answer="",
            value=100
        )


def test_question_rejects_zero_value():
    with pytest.raises(ValueError):
        test_question = game.Question(
            id=1,
            topic="Games",
            text="Publisher of GTA series",
            answer="Rockstar Games",
            value=0
    )


def test_question_rejects_negative_value():
    with pytest.raises(ValueError):
        test_question = game.Question(
            id=1,
            topic="Games",
            text="Publisher of GTA series",
            answer="Rockstar Games",
            value=-100
    )

def test_question_reject_non_integer_value():
    with pytest.raises(ValueError):
        test_question = game.Question(
            id=1,
            topic="Game",
            text="Publisher of GTA series",
            answer="Rockstar Games",
            value= 100.5  # type: ignore
        )


def test_question_cannot_be_modified():
    test_question = game.Question(
        id=1,
        topic="Games",
        text="Publisher of GTA series",
        answer="Rockstar Games",
        value=100
    )
    with pytest.raises(FrozenInstanceError):
        test_question.value = 200  # type: ignore
