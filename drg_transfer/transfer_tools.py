from pathlib import Path

from typing import Union, Literal, Tuple, NamedTuple, TypedDict


# Types
class SaveFilePaths(NamedTuple):
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
def get_env_paths() -> SaveFilePaths:
    """
    Gets path objects for the save file paths given in the environment variables.

    :return:
    """
    pass


def check_and_stat_savepath(
        kind: Union[Literal["xbox"], Literal["steam"]],
        path: Path) -> SaveFile:
    """
    Makes sure the savefile exists and gets the savefile's modified time so we can return a SaveFile dict.

    :param kind:
    :param path:
    :return:
    """
    pass


def decide_save_to_keep(savefiles: Tuple[SaveFile]) -> FileTransfer:
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
