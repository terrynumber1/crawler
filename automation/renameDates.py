#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

datePattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without date
    if mo == None:
        continue # Skip the rest of the FOR loop and go to the next file.

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # print('----------------------')
    # print(mo.group())
    # print(mo.group(1))
    # print(mo.group(2))
    # print(mo.group(3))
    # print(mo.group(4))
    # print(mo.group(5))
    # print(mo.group(6))
    # print(mo.group(7))
    # print(mo.group(8))

    # Form the European-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    print(amerFilename)
