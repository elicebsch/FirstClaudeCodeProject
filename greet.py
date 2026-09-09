"""A tiny greeting helper."""


def greet(name: str) -> str:
    """Return a friendly greeting for the given name.

    Falls back to a generic greeting if the name is missing or
    contains only whitespace (e.g. "" or "   ").
    """
    name = (name or "").strip()
    if not name:
        return "Hello, there!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("world"))
