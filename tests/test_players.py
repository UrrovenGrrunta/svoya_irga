import pytest

from svoya_igra import game


def test_player_stores_telegram_id_and_name():
    test_player = game.Player(
        telegram_id = 123456,
        name = "UrrovenGrrunta"
    )
    assert test_player.telegram_id == 123456
    assert test_player.name == "UrrovenGrrunta"


def test_new_player_starts_with_zero_score():
    test_player = game.Player(
        telegram_id = 123456,
        name = "UrrovenGrrunta"
    )
    if test_player.player_score > 0 or test_player.player_score < 0:
        raise ValueError("Score cannot be grater or lower then 0 at the start")

def test_player_rejects_empty_name():
    with pytest.raises(ValueError):
        test_player = game.Player(
            telegram_id = 123456,
            name = "",
        )


def test_player_rejects_whitespace_name():
    with pytest.raises(ValueError):
        test_player = game.Player(
            telegram_id = 1213456,
            name = " ",
        )


def test_player_rejects_non_positive_telegram_id():
    with pytest.raises(ValueError):
        test_player = game.Player(
            telegram_id = -123456,
            name = "UrrovenGrrunta",
        )


def test_player_rejects_non_integer_telegram_id():
    with pytest.raises(ValueError):
        test_player = game.Player(
            telegram_id = "abcdef",  #type: ignore[arg-type]
            name = "UrrovenGrrunta",
        )

def test_player_rejects_zero_telegram_id():
    with pytest.raises(ValueError):
        test_player = game.Player(
            telegram_id = 0,
            name = "UrrovenGrrunta"
        )