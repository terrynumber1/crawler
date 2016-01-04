#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

# Createa regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?))
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

    # TODO: Loop over the files in the working directory.
    # TODO: Skip files without a date.
    # TODO: Get the different parts of the filename.
    # TODO: Form the European-style filename.
    # TODO: Get the full, absolute file paths.
    # TODO: Rename the files.
