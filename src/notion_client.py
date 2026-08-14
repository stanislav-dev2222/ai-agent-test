import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def load_environment() -> None:
    env_path = Path(__file__).resolve().parent.parent / ".env"

    if not env_path.exists():
        raise RuntimeError("Файл .env не знайдено.")

    for line in env_path.read_text(encoding="utf-8").splitlines():
        if "=" not in line or line.strip().startswith("#"):
            continue

        key, value = line.split("=", 1)
        os.environ[key.strip()] = value.strip()


def save_task_to_notion(task: dict[str, str]) -> str:
    load_environment()

    token = os.getenv("NOTION_TOKEN")
    data_source_id = os.getenv("NOTION_DATA_SOURCE_ID")

    if not token or not data_source_id:
        raise RuntimeError("Додайте NOTION_TOKEN і NOTION_DATA_SOURCE_ID у файл .env.")

    payload = {
        "parent": {
            "type": "data_source_id",
            "data_source_id": data_source_id,
        },
        "properties": {
            "Назва": {
                "title": [{"text": {"content": task["Назва"]}}],
            },
            "Мета": {
                "rich_text": [{"text": {"content": task["Мета"]}}],
            },
            "Дедлайн": {
                "rich_text": [{"text": {"content": task["Дедлайн"]}}],
            },
            "Пріоритет": {
                "select": {"name": task["Пріоритет"]},
            },
            "Очікуваний результат": {
                "rich_text": [{"text": {"content": task["Очікуваний результат"]}}],
            },
            "Статус": {
                "select": {"name": "Нова"},
            },
        },
    }

    request = Request(
        "https://api.notion.com/v1/pages",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Notion-Version": "2026-03-11",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=15) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["url"]
    except HTTPError as error:
        details = error.read().decode("utf-8")
        raise RuntimeError(f"Помилка Notion: {details}") from error
    except URLError as error:
        raise RuntimeError("Не вдалося підключитися до Notion.") from error