#!/usr/bin/env python3

import shutil
import sys

disk = input("Enter the disk letter followed by with Colon e.g 'C:' \n")

def check_disk_usage(disk, min_absolute, min_percentage):
    """Return true if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # calculate how many gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percentage or gigabytes_free < min_absolute:
        return False
    return True

# check for atleast 2GB or 10% free
if not check_disk_usage(disk, 2, 10):
    print("Errro! Not enough disk space")
    sys.exit(1)
print("Everything is OK")
sys.exit(0)
