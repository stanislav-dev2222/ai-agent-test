from src.agent import collect_task, format_task


def main() -> None:
    print("Вітаю! Я помічник Project Manager.")
    print("Допоможу оформити нову задачу.")

    task = collect_task()
    task_card = format_task(task)

    print(task_card)
    print("Задачу сформовано. У наступній версії збережемо її в Notion.")


if __name__ == "__main__":
    main()