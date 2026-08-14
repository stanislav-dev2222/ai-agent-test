from src.agent import get_response


def main() -> None:
    name = input("Введите ваше имя: ").strip()

    if not name:
        name = "друг"

    print(f"\nПривет, {name}! Добро пожаловать в AI Agent Test.")

    question = input("Введите ваш вопрос или задачу: ")
    response = get_response(question)

    print(f"\nОтвет агента: {response}")


if __name__ == "__main__":
    main()