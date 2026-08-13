# game.py

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Question:
    """A question in a question pack."""

    id: int
    topic: str
    text: str
    answer: str
    value: int


    def __post_init__(self):
        if self.topic.strip() == "":
            raise ValueError("Topic cannot be empty")
        if self.text.strip() == "":
            raise ValueError("Text cannot be empty")
        if self.answer.strip() == "":
            raise ValueError("Answer cannot be empty")
        if type(self.value) is not int:
            raise ValueError("Value must be intager")
        if self.value <= 0:
            raise ValueError("Value cannot be non-positive")


@dataclass
class Player:
    """Player data from Telegram"""
    telegram_id: int
    name: str
    player_score: int = field(
        repr = False,
        default=0,
        init = False
    )


    def __post_init__(self):
        if self.name.strip() == "":
            raise ValueError("Telegram name cannot be empty")
        if type(self.telegram_id) is not int:
            raise ValueError("Telegram ID must be intager")
        if self.telegram_id <= 0:
            raise ValueError("Telegram ID cannot be non-positive")


@dataclass
class GameSession:
    """"Represents the current game session and its connected players."""
    players: list[Player] = field(default_factory=list)

    def add_player(self, player:Player) -> None:
        for existing_player in self.players:
            if existing_player.telegram_id == player.telegram_id:
                raise ValueError("Player already in game")
        self.players.append(player)