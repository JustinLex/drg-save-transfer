from datetime import datetime
from pathlib import Path
import configparser
import shutil

from typing import Union, Literal, Tuple, NamedTuple, TypedDict


# Types

# type alias for either the string literal "steam" or "xbox", bit of a magic string
xb_or_steam = Union[Literal["xbox"], Literal["steam"]]


class SaveFilePaths(TypedDict):
    """Dict with both the xbox and steam paths."""
    xbox: Path
    steam: Path


class SaveFile:
    """
    Class describing a savefile.

    Rich comparison for this class compares the mtimes, newest file > oldest file
    """

    def __init__(self,
                 kind: xb_or_steam,
                 path: Path,
                 mtime: datetime):
        self.kind = kind
        self.path = path
        self.mtime = mtime

    def __lt__(self, other):
        return self.mtime < other.mtime

    def __eq__(self, other):
        return self.mtime == other.mtime


class FileTransfer(NamedTuple):
    """Dict describing a proposed file transfer operation, transferring from the keep path to the overwrite path."""
    keep: SaveFile
    overwrite: SaveFile


class SavefileNotFoundError(Exception):
    """
    Error for when a savefile is not found.

    This error describes if the file is meant to be an xbox or steam savefile,
    and the path where the savefile was expected.
    """
    filename: str
    kind: xb_or_steam

    def __init__(self, enoent: FileNotFoundError, kind: xb_or_steam):
        self.filename = enoent.filename
        self.kind = kind


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
        kind: xb_or_steam,
        path: Path) -> SaveFile:
    """
    Makes sure the savefile exists and stats the savefile's modified time so we can return a SaveFile dict.

    :raises SavefileNotFoundError: If savefile does not exist
    """
    try:
        mtime_seconds = path.stat().st_mtime
    except FileNotFoundError as err:
        # Package what kind of save file we were expecting so that the UI can tell the user which file was missing
        raise SavefileNotFoundError(enoent=err, kind=kind)

    # Does Windows' mtime give UTC timestamps?? Printing this time to the user might be wildly inaccurate.
    mtime = datetime.fromtimestamp(mtime_seconds)

    return SaveFile(kind=kind, path=path, mtime=mtime)


def decide_save_to_keep(savefiles: Tuple[SaveFile, SaveFile]) -> FileTransfer:
    """Compares the save files and decides which file is newer and should be transferred to overwrite the old file."""
    keep = max(savefiles)
    overwrite = min(savefiles)
    return FileTransfer(keep=keep, overwrite=overwrite)


def backup_save(save_file: SaveFile) -> None:
    """Makes a copy of the save file, appending the current date and time to its name."""
    old_path = save_file.path
    new_save_name = old_path.name + "-backup-" + str(datetime.now())
    save_file.path.rename(old_path.with_name(new_save_name))


def transfer_save(proposed_transfer: FileTransfer) -> None:
    """Transfers the save file over, overwriting the existing file there."""
    shutil.copy2(
        src=str(proposed_transfer.keep.path),
        dst=str(proposed_transfer.overwrite.path)
    )
