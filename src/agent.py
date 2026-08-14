def ask_required(prompt: str) -> str:
    """Запрашивает обязательное поле, пока пользователь не введёт значение."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Будь ласка, введіть значення.")


def choose_priority() -> str:
    priorities = {
        "1": "Високий",
        "2": "Середній",
        "3": "Низький",
    }

    print("\nОберіть пріоритет:")
    print("1 — Високий")
    print("2 — Середній")
    print("3 — Низький")

    while True:
        choice = input("Ваш вибір (1-3): ").strip()

        if choice in priorities:
            return priorities[choice]

        print("Введіть 1, 2 або 3.")


def collect_task() -> dict[str, str]:
    """Збирає дані для нової задачі."""
    print("\n--- Створення нової задачі ---")

    return {
        "Назва": ask_required("Коротка назва задачі: "),
        "Мета": ask_required("Яка мета задачі? "),
        "Дедлайн": ask_required("Який дедлайн? "),
        "Пріоритет": choose_priority(),
        "Очікуваний результат": ask_required("Який очікуваний результат? "),
    }


def format_task(task: dict[str, str]) -> str:
    """Перетворює дані задачі на готову картку."""
    return f"""
--- Картка задачі ---

Назва: {task["Назва"]}
Мета: {task["Мета"]}
Дедлайн: {task["Дедлайн"]}
Пріоритет: {task["Пріоритет"]}
Очікуваний результат: {task["Очікуваний результат"]}
"""