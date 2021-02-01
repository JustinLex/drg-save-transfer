from .drg_transfer import transfer_tools
# import argparse
#
# parser = argparse.ArgumentParser(
#     description="Transfer save files for Deep Rock Galactic between Steam and Xbox Games Pass."
#
# )

paths = transfer_tools.get_env_paths()

try:
    # stat files to see if they exist and to get mtimes
    xbox_mtime = None
    steam_mtime = None
    pass
except Exception:
    quit()

else:
    # Print file info
    proposed_transfer = transfer_tools.decide_save_to_keep(xbox_mtime, steam_mtime)
    # tell user about proposed transfer
    # Bail if dry run
    # Prompt user for yes or no
    transfer_tools.backup_save(None)
    transfer_tools.transfer_save(proposed_transfer)
    # Mission accomplished
