Some Visual Studio Code profiles, easily usable and editable.

I've been using vscode profiles for a few months now to have specific settings/themes for their own use.
I felt the need to spend time organizing all of this in a repo, which is intended to be as simple as possible
to add profiles while documenting them (instead of having a raw .code-profile file as vscode offers).

Vscode already has some profile templates (which you can see [here](https://code.visualstudio.com/docs/editor/profiles#_python-profile-template))
but they are quite limited in the sense that they aim to be as generic as possible.
The main goal of this repository is to have a bank of more specific (but well-documented) profiles,
as long as they would be useful to a significant number of people.
The contents of these profiles are in the `profiles` folder and
you can easily see what each one contains.

## Installation

Copy the link of the profile you want to use (see the list below) and paste it in the **File > Preferences > Profiles > Import Profile...** setting.
![find the Import Profile setting](doc/image.png)

Read [the official documentation](https://code.visualstudio.com/docs/editor/profiles) of vscode profiles for more details.

## List of profiles

By clicking on the profile name, you will be redirected to the profile's documentation file. There you will find
an overview of the profile (theme used, extensions installed, etc.) and some recommendations specific to the profile.

| Profile                             | Download link                                                |
| ----------------------------------- | ---------------------------------------------------------------- |
| [Python](profiles/python/python.md) | [Lython.code_profile](profiles/python/Python.code-profile?raw=1) |
| [Latex](profiles/latex/latex.md)    | [Latex.code_profile](profiles/latex/Latex.code-profile?raw=1)    |

## Configuration

The settings are configured in the `settings.json` file of each profile. You can read the file to see the settings that are already configured.

To modify your own settings, you can navigate to **File > Preferences > Settings** and search for the setting you want to change.
Click on the little icon on the right (Open Settings (JSON)) if you want to directly modify your own `settings.json` file.

For example, if you want to change the font, you can either:

- search "font" in the settings and change the font family
- change or add the `editor.fontFamily` setting in the `settings.json` file.

This is exactly the same for the keybindings. You can navigate to **File > Preferences > Keyboard Shortcuts** and search for the keybinding you want to change.

## Contributing

Feel free to contribute by creating a pull request or an issue. You can suggest a profile or something to add to an existing profile
that would be useful to everyone (not something specific to your own use case) by creating an issue or a pull request.

### Create a new profile

You can refer to the profiles already there in the `profiles` folder.

1. Create a folder in the 'profiles' folder with the name of your profile in lowercase, replacing spaces with underscores (e.g., 'python').
2. Create a markdown file in this folder with the same name of your folder (e.g. `python.md`) to present it, with the same structure as the other profiles.
3. Add your json files in this folder. You can copy this files from another profile and modify them.
4. Add the name of your profile in the `profiles.json` (e.g. `Python`) file at the root of the repository.
5. Test that your profile works:
   - Execute the `scripts/build_profiles.py` script
   - Import your profile in VS Code with the .code-profile generated in the folder of your profile
6. Add your profile to the list in the `README.md` file at the root of the repository.
