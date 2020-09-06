#!/usr/bin/python3
from sys import argv
import shutil

if (len(argv) == 2):
    print("Adding to archive . . .")
    shutil.make_archive(argv[1],'zip',argv[1])
    print("Done")
else:
        print("Usage: z <DirectoryName>")


