"""A tiny greeting helper."""


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    if not name:
        return "Hello, there!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("world"))
