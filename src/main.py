from src.agent import collect_task, format_task
from src.notion_client import save_task_to_notion


def main() -> None:
    print("Вітаю! Я помічник Project Manager.")
    print("Допоможу оформити нову задачу.")

    task = collect_task()

    print(format_task(task))

    save_choice = input("Зберегти задачу в Notion? (так/ні): ").strip().lower()

    if save_choice in {"так", "т", "yes", "y"}:
        try:
            page_url = save_task_to_notion(task)
            print(f"\nЗадачу збережено в Notion: {page_url}")
        except RuntimeError as error:
            print(f"\nНе вдалося зберегти задачу: {error}")
    else:
        print("\nЗадачу не збережено.")


if __name__ == "__main__":
    main()