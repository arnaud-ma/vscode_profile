# VS Code Python Profile with complete settings
A python profile with a lot of settings and a full theme already configured. The theme used is `One Dark Pro` with some additional features.

## Installation

1. Navigate to: **File > Preferences > Profiles > Import Profile...**
![](doc/image.png)

1. Paste the link: https://raw.githubusercontent.com/arnaud-ma/vscode_profile/main/Python.code-profile

If you want to get the ligatures, you can install the [Jetbrains mono font](https://github.com/JetBrains/JetBrainsMono#installation)

### Ruff configuration

Unfortunately there can be many problems putting ruff settings directly into the `settings.json` file and applying those settings for any workspace. What you can do instead is to add a `pyproject.toml` file at the root of your project with all the settings you want. \
For example my template file is :

<details>
<summary>pyproject.toml</summary>
<p>

```toml
[tool.black]
# should be same as ruff
line-length = 88

[tool.ruff]
# should be same as black
line-length = 88

# https://beta.ruff.rs/docs/rules/
select = [
    "E",    # pycodestyle
    "F",    # pyflakes
    "N",    # pep8-naming
    "W",    # warnings (indentation, line length, etc.)
    "UP",   # pyupgrade
    "S",    # bandit
    "B",    # bugbear
    "COM",  # commas
    "C4",   # comprehensions
    "EM",   # error messages
    "RET",  # returns
    "RSE",  # raise statements
    "Q003", # quotes
    "SLF",  # private methods
    "SIM",  # simplify
    "TCH",  # type checking
    "PL",   # pylint
]

ignore = [
    "E501",   # line too long
    "F841",   # unused variable
    "RET505", # unnecessary `else` after `return` statement
    "COM812", # trailing comma (conflict with black formatter)
    "B905",   # no strict in zip
    "S311",   # random number generator not cryptographically strong
    "S101",   # use of assert detected
    "SLF001", # private member access
]

exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# exclude some rules in the __init__.py files
[tool.ruff.extend-per-file-ignores]
"__init__.py" = ["F401"] # unused import

[tool.ruff.pydocstyle]
# https://beta.ruff.rs/docs/settings/#pydocstyle-convention
convention = "google"

[tool.ruff.flake8-quotes]
inline-quotes = "double"
multiline-quotes = "double"
docstring-quotes = "double"


[tool.ruff.pylint]
max-args = 5

[tool.pyright]
# deactivate pyright features that are already covered by ruff
# only activate type checking actually
typeCheckingMode = "basic"
stubPath = "typings"
reportGeneralTypeIssues = true
reportMissingTypeStubs = false
reportUndefinedVariable = false
reportUnusedVariable = false
reportUnusedClass = false
reportUnusedFunction = false
```
</p>
</details>

## Extensions

- `Python` - Python extension for Visual Studio Code.
- `Pylance` - Fast, feature-rich language support for Python.
- `Black formatter` -  The uncompromising Python code formatter.
- `Ruff` - Support for the Ruff linter.
- `autoDocstring` - Automatically generates docstrings.
- `Even Better TOML` - TOML file support, for project config setup files like `pyproject.toml`.
- `Code Spell Checker` - A basic spell checker that works well with code and documents.
- `Python indent` - Correct python indentation in VS Code.
- `One Dark Pro` - Atom's iconic One Dark theme.

## Theme

The theme used is `One Dark Pro`. Some features are added in the `settings.json` file :

- For the font, you can see the `- font / writing style` section in the `settings.json` file.
- Module import are bolded
- Abstract methods are bolded
- Everything related to annotation is of a different color (close from the comments color)
- async function are of a different color

For even more customization, you can add (only need to download):

- a file icon theme like [Material icon theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
- a product icon theme like [Fluent icons](https://marketplace.visualstudio.com/items?itemName=miguelsolorio.fluent-icons)

## Settings

You can read the `settings.json` file to see the settings that are already configured.

## Key bindings

- `ctrl+enter` - Run the python file
- `ctrl+t` - Toggle the terminal, `ctrl+shift t` to open a new one
- `ctrl+k` - If focus on the terminal, clear it
- `alt+d` - Add word to dictionary
- `f4` - Go to the reference
