import json

NAME = "Python"


def create_dict(name: str) -> dict[str, str | dict]:
    """Create a dictionary that correspond to the .code-profile file format:

    ```json
    {
      "name": "name_argument",
      "settings": {"settings": "settings.json contents"},
      "keybindings": {"keybindings": "keybindings.json contents", "platform": 3},
      "snippets": {"snippets": {"python.json": "python.json contents"}},
      "extensions": "extensions.json contents"
    }
    ```
    """
    d: dict[str, str | dict] = {"name": name}

    with (
        open("profile/settings.json") as f_settings,
        open("profile/keybindings.json") as f_keybindings,
        open("profile/snippets/python.json") as f_snippets,
        open("profile/extensions.json") as f_extensions,
    ):
        d["settings"] = json.dumps({"settings": f_settings.read()})
        d["keybindings"] = json.dumps(
            {"keybindings": f_keybindings.read(), "platform": 3}
        )
        d["snippets"] = json.dumps({"snippets": {"python.json": f_snippets.read()}})
        d["extensions"] = f_extensions.read()

    return d


def main():
    d = create_dict(NAME)
    with open(f"profile/{NAME}.code-profile", "w") as f:
        json.dump(d, f)


if __name__ == "__main__":
    main()
