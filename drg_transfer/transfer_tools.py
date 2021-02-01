from pathlib import Path

from typing import Union, Literal, NamedTuple, TypedDict


# Types
class SaveFilePaths(NamedTuple):
    xbox: Path
    steam: Path


class SaveFile(TypedDict):
    kind: Union[Literal["xbox"], Literal["steam"]]
    path: Path


class FileTransfer(NamedTuple):
    keep: SaveFile
    overwrite: SaveFile


# Functions
def get_env_paths() -> SaveFilePaths:
    """
    Gets path objects for the save file paths given in the environment variables.

    :return:
    """
    pass


def decide_save_to_keep(xbox_mtime, steam_mtime) -> FileTransfer:
    """
    Compares the save files and decides which file is newer and should be transferred to overwrite the old file.

    :param xbox_mtime:
    :param steam_mtime:
    :return:
    """
    pass


def backup_save(save_file: SaveFile) -> None:
    """
    Makes a copy of the save file, appending the current date and time to its name.
    :param save_file:
    """
    pass


def transfer_save(proposed_transfer: FileTransfer) -> None:
    """
    Transfers the save file over, overwriting the existing file there.
    :param proposed_transfer:
    """
    pass
