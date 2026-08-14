def get_response(question: str) -> str:
    question = question.strip().lower()

    if not question:
        return "Вы не ввели вопрос. Попробуйте ещё раз."

    if "привет" in question:
        return "Привет! Я учебный AI-агент для Project Manager."

    if "помощ" in question:
        return "Я могу принять ваш вопрос и показать базовый ответ."

    if "задач" in question:
        return "Сформулируйте цель, срок и ожидаемый результат задачи."

    return "Я получил ваш запрос. В следующей версии смогу дать более подробный ответ."