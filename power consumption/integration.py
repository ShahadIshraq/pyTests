import numpy as np
import scipy.integrate as intg

from os import walk
import re

t = 1.22e-3



mypath = input("The path : ")
output_file = open(mypath+"/result", 'w')
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

print(filenames)

for filename in filenames:
    match = re.match(r'slice[0-9]+', filename)
    if match is None:
        continue
    print(filename)
    f = open(mypath+"/"+filename, 'r')
    y = []

    c = 0
    for line in f:
        c = c + 1
        line = line.split()
        if len(line) < 1:
            continue
        line = line[0]
        if line is None:
            continue
        value = float(line)
        y.append(value)

    f.close()
    x = np.arange(0.0,  len(y)*1.22 - 0.2, 1.22)
    output_file.write(str(5.0*intg.simps(y, x)/len(y)*1.22)+"\n")

output_file.close()