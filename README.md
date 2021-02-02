# Deep Rock Galactic Save transfer Tool - Python version
This is a reimplementation of [elibosley](https://github.com/elibosley)'s 
[deep-rock-galactic-save-transfer tool](https://github.com/elibosley/deep-rock-galactic-save-transfer), 
written in Python to prove that Python is better than Javascript. 
(And to learn more about the two languages, and how to script with them.) (But winning is more important.)

This tool allows you to transfer save files for [Deep Rock Galactic](https://store.steampowered.com/app/548430/Deep_Rock_Galactic/)
between the Steam edition of the game, and the Xbox Games Pass edition.

## Usage
1. Copy settings.ini.example to a new settings.ini file, and set the paths to your corresponding copies of the game installed on your
computer. You should just have to change the path to the home folder for your Windows user,
but if you have the game installed on a different drive, it might be somewhere else.

2. Open the directory with this program in cmd.exe or Powershell. 

3. Test the program by running `python drg_transfer_cli.py` with dry_run set to true (requires Python 3.8+)

4. Set dry_run in settings.ini to false and run `python drg_transfer_cli.py` again to transfer your savefiles

5. ???

6. Profit

## Differences to JS version
* Savefile paths and the dry-run setting is stored in settings.ini. 
A NodeJS-style .env file could be used here as well, but support for that is in the dotenv library,
and we are avoiding external pip packages for ease of development.

* Console output is not colored for the same reasons, as it is done with an external pip package.