#!/usr/bin/python

import sys
import os

# We're expecting a space deliminated string from the makefile. Split it into
# an array so we can get started.
files_raw = sys.argv[1]
files = files_raw.split()

good_files = []
# Parse through every file
for i in range(len(files)):

    # Open in reversed (to find the last instance of 'iso_url'
    for line in reversed(open(files[i]).readlines()):
        if "iso_url" in line:
            # Now that we've found our line, we need to check if it starts
            # with 'iso' (e.g. it's a local file).
            iso_url = line.split('"')[3]
            if iso_url.startswith("http"):
                good_files.append(files[i])
            else:
                exists = os.path.isfile(iso_url)
                if exists:
                    good_files.append(files[i])
            break

# now that we have a list of good files, dump it out for the makefile
sys.stdout.write("%s\n" % ' '.join(good_files))

