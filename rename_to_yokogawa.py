import os
import re

files = []
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    files.extend(filenames)
    break

for fname in files:

    if 'Probabilities' in fname:

        m = re.search(r"plate01_(.\d*)_x(\d*)_y(\d*)", fname)
        well_name = m.group(1)
        x = int(m.group(2))
        y = int(m.group(3))

        field = y * 9 + x + 1

        newname = '20170607-Kim2-NascentRNA-Volume-PCNA_' + well_name + '_T0001F' + str(field).zfill(3) + 'L01A02Z01C05.tif'

        os.rename(fname, newname)
