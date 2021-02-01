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
xbox_save = transfer_tools.check_and_stat_savepath(kind="xbox", path=paths['xbox'])
steam_save = transfer_tools.check_and_stat_savepath(kind="steam", path=paths['steam'])

# Print file info

proposed_transfer = transfer_tools.decide_save_to_keep((xbox_save, steam_save))

# tell user about proposed transfer

# Bail if dry run
if transfer_tools.dry_run:
    print("Running in DRY RUN MODE, quitting.")
    quit()

# Prompt user for yes or no

transfer_tools.backup_save(None)
transfer_tools.transfer_save(proposed_transfer)

# Mission accomplished
