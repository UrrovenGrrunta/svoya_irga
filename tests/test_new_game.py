import pytest

from svoya_igra import game


def test_new_game_has_no_players():
    game_session = game.GameSession()

    assert game_session.players == []


def test_game_session_adds_player():
    game_session = game.GameSession()

    player = game.Player(
        telegram_id=123456, 
        name="UrrovenGrrunta"
    )

    game_session.add_player(player)
    assert player in game_session.players


def test_game_session_rejects_duplicate_telegram_id():
    game_session = game.GameSession()

    first_player = game.Player(
        telegram_id=123456,
        name="Urroven"
    )
    second_player = game.Player(
        telegram_id=123456,
        name="Grrunta"
    )
    game_session.add_player(first_player)
    with pytest.raises(ValueError):
        game_session.add_player(second_player)