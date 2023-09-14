"""
This script generates a .code-profile file for each profile directory
(in the profiles/ directory), specified in PROFILE_NAMES

A profile directory must have the following structure:
    snippet/
        snippet1.json
        snippet2.json
    extensions.json
    keybindings.json
    settings.json

There can be more files or missing files in the directory,
but the files listed above are the only ones that will be dumped into
the .code-profile file (if they exist).

The .code-profile file format is as follows:
{
    "name": "name_argument",
    "settings": {
        "settings": "settings.json contents"
    },
    "keybindings": {
        "keybindings": "keybindings.json contents",
        "platform": 3
    },
    "snippets": {
        "snippets": {
            "snippet1": "snippet1.json contents",
            "snippet2": "snippet2.json contents"
        }
    },
    "extensions": "extensions.json contents"
}
"""

import json
import warnings
from dataclasses import dataclass
from os import PathLike
from pathlib import Path

"""The directory that contains the profile directories."""
DIRECTORY = Path("profiles")

"""The names of the profile directories to generate .code-profile files for."""
PROFILE_NAMES = ("python",)

@dataclass
class Profile:
    """A Profile object that represent a directory with the following structure:
    ```
    snippet/
        snippet1.json
        snippet2.json
    extensions.json
    keybindings.json
    settings.json
    ```

    There can be more files or missing files in the directory, but the files
    listed above are the only ones that will be dumped into the .code-profile file
    (if they exist)

    Args:
        path (str | PathLike[str]): The path to the profile directory.

    Methods:
        create_dict(name: str) -> dict[str, str | dict]:
            Create a dictionary that correspond to the .code-profile file format
            (see the docstring of the method for more details of the format).
        write(name: str):
            Write the .code-profile file into the profile directory.

    Example:
    ```python
        >>> profile = Profile("path/to/a_python_profile")
        >>> profile.write("Python")
    ```
    """

    path: str | PathLike[str]  # type: ignore

    def __post_init__(self):
        self.path: Path = Path(self.path)
        self.configs = ("extensions", "keybindings", "settings", "snippets")

    def dump_snippets(self) -> str | None:
        snippets = self.path / "snippets"
        if not snippets.exists():
            return None

        snippets = list(snippets.glob("*.json"))
        if not snippets:
            return None

        not_dumped = {
            "snippets": {
                snippet.name: snippet.read_text(encoding="utf8") for snippet in snippets
            }
        }
        return json.dumps(not_dumped)

    def dump_extensions(self) -> str | None:
        extensions = self.path / "extensions.json"
        if not extensions.exists():
            return None
        return extensions.read_text(encoding="utf8")

    def dump_keybindings(self) -> str | None:
        keybindings = self.path / "keybindings.json"
        if not keybindings.exists():
            return None
        not_dumped = {
            "keybindings": keybindings.read_text(encoding="utf8"),
            "platform": 3,
        }
        return json.dumps(not_dumped)

    def dump_settings(self) -> str | None:
        settings = self.path / "settings.json"
        if not settings.exists():
            return None
        not_dumped = {"settings": settings.read_text(encoding="utf8")}
        return json.dumps(not_dumped)

    def create_code_profile_dict(self, name: str) -> dict[str, str | dict]:
        """Create a dictionary that correspond to the .code-profile file format:

        ```json
        {
          "name": "name_argument",
          "settings": {
              "settings": "settings.json contents"
            },
          "keybindings": {
              "keybindings": "keybindings.json contents",
              "platform": 3
            },
          "snippets": {
              "snippets": {
                "snippet1": "snippet1.json contents",
                "snippet2": "snippet2.json contents"
              }
            },
          "extensions": "extensions.json contents"
        }
        ```
        """
        d: dict[str, str | dict] = {"name": name}
        for file in ("settings", "keybindings", "snippets", "extensions"):
            dumped = getattr(self, f"dump_{file}")()
            if dumped is not None:
                d[file] = dumped
        if not d:
            warnings.warn(f"Profile {name!r} is empty", RuntimeWarning, stacklevel=2)
        return d

    def write_code_profile(self, name: str):
        """Write the .code-profile file into the profile directory."""
        d = self.create_code_profile_dict(name)
        with open(self.path / f"{name}.code-profile", "w") as f:
            json.dump(d, f)


def main():
    for name in PROFILE_NAMES:
        profile = Profile(DIRECTORY / name)
        profile.write_code_profile(name)


if __name__ == "__main__":
    main()
