from . import game


def main():
    question = game.Question(
        id=1,
        topic="Games",
        text="Publisher of GTA series",
        answer="Rockstar Games",
        value=100
    )
    print(f"Question id: {question.id}")
    print(f"Question topic: {question.topic}")
    print(f"Question text: {question.text}")
    print(f"Question answer: {question.answer}")
    print(f"Question value: {question.value}")


if __name__ == "__main__":
    main()