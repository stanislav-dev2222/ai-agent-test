def greet_user():
    name = input("Введите ваше имя: ").strip()

    if not name:
        name = "друг"

    print(f"Привет, {name}! Добро пожаловать в AI Agent Test.")


if __name__ == "__main__":
    greet_user()
    