def greetings(name: str) -> str:
    print(f"Hello {name}!")


def main():
    for names in ["Ali", "Bob", "Cindy"]:
        greetings(names)


if __name__ == "__main__":
    main()

    