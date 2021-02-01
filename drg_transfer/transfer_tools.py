from pathlib import Path
import configparser

from typing import Union, Literal, Tuple, NamedTuple, TypedDict


# Types
class SaveFilePaths(TypedDict):
    xbox: Path
    steam: Path


class SaveFile(TypedDict):
    kind: Union[Literal["xbox"], Literal["steam"]]
    path: Path
    mtime: None


class FileTransfer(NamedTuple):
    keep: SaveFile
    overwrite: SaveFile


# Functions
@property
def dry_run() -> bool:
    """Gets the value for the dry_run setting in settings.ini."""
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config.getboolean('cli_settings', 'dry_run')


def get_paths() -> SaveFilePaths:
    """Gets Path objects for the save file paths given in settings.ini."""
    config = configparser.ConfigParser()
    config.read('settings.ini')

    xbox_path_string: str = config['paths']['xbox_path']
    steam_path_string: str = config['paths']['steam_path']

    xbox_path = Path(xbox_path_string)
    steam_path = Path(steam_path_string)

    return {'xbox': xbox_path, 'steam': steam_path}


def check_and_stat_savepath(
        kind: Union[Literal["xbox"], Literal["steam"]],
        path: Path) -> SaveFile:
    """Makes sure the savefile exists and stats the savefile's modified time so we can return a SaveFile dict."""
    pass


def decide_save_to_keep(savefiles: Tuple[SaveFile, SaveFile]) -> FileTransfer:
    """Compares the save files and decides which file is newer and should be transferred to overwrite the old file."""
    pass


def backup_save(save_file: SaveFile) -> None:
    """Makes a copy of the save file, appending the current date and time to its name."""
    pass


def transfer_save(proposed_transfer: FileTransfer) -> None:
    """Transfers the save file over, overwriting the existing file there."""
    pass
