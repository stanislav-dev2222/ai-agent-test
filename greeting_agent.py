def get_response(question):
    question = question.strip().lower()

    if not question:
        return "Вы не ввели вопрос. Попробуйте ещё раз."

    if "привет" in question:
        return "Привет! Я учебный AI-агент."
    if "помощ" in question:
        return "Я могу принять ваш вопрос и показать базовый ответ."
    if "задач" in question:
        return "Сформулируйте цель, срок и ожидаемый результат задачи."

    return "Я получил ваш запрос. В следующей версии я смогу давать более подробные ответы."


def main():
    name = input("Введите ваше имя: ").strip()

    if not name:
        name = "друг"

    print(f"Привет, {name}! Добро пожаловать в AI Agent Test.")

    question = input("Введите ваш вопрос или задачу: ")
    response = get_response(question)

    print(f"\nОтвет агента: {response}")


if __name__ == "__main__":
    main()