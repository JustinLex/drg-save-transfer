from .drg_transfer import transfer_tools
# import argparse
#
# parser = argparse.ArgumentParser(
#     description="Transfer save files for Deep Rock Galactic between Steam and Xbox Games Pass."
#
# )

# Read paths from settings.ini
paths = transfer_tools.get_paths()

# Check that savefiles exist and stat their mtimes
try:
    xbox_save = transfer_tools.check_and_stat_savepath(kind="xbox", path=paths['xbox'])
    steam_save = transfer_tools.check_and_stat_savepath(kind="steam", path=paths['steam'])
except transfer_tools.SavefileNotFoundError as err:
    print(f'ERROR: Could not find the {err.kind} savefile at {err.filename}!')
    raise

# Print file info
print(
    f'''Save files found.
Xbox Games Pass save location and modified time:
{str(xbox_save.path)}
{str(xbox_save.mtime)}
Steam save location and modified time:
{str(steam_save.path)}
{str(steam_save.mtime)}
'''
)

# Figure out which file is newer, and abort if they appear to be identical
try:
    proposed_transfer = transfer_tools.decide_save_to_keep((xbox_save, steam_save))
except transfer_tools.SavefilesAreIdenticalError:
    print("Both save files appear to be identical. Nothing to transfer, quitting.")
    quit()

# tell user about proposed transfer
kind_to_keep = proposed_transfer.keep.kind
kind_to_overwrite = proposed_transfer.overwrite.kind
print(f"Your {kind_to_keep} save file is newer and will be transferred to {kind_to_overwrite}.")
print(f"Your save file on {kind_to_overwrite} will be replaced by this operation.")

# Bail if dry run
if transfer_tools.dry_run:
    print("Running in DRY RUN MODE, files will not be modified. Quitting.")
    quit()

# Prompt user for yes or no
response = input("Do you want to copy this savefile? (y/N)")
if response.lower() != 'y':
    print("Save transfer cancelled.")
    quit()

# Backup save to be overwritten and make transfer
transfer_tools.backup_save(proposed_transfer.overwrite)
transfer_tools.transfer_save(proposed_transfer)

# Mission accomplished
print("Your save file has been successfully transferred! Happy mining!")
