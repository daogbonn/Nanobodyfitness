# Plotting the values as a heat map

import numpy
import seaborn
import matplotlib.pyplot as plt
import os


# Import all the Variable regions
a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Long_High_VR\\VR3_17.fasta"
d = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data'

# Read files into a line
VR1_file = open(a)
VR1_nb = VR1_file.read()
VR1_alt = VR1_nb.splitlines()
VR1_file.close()
# Cut off the line
VR1 = []
VR1_line = numpy.arange(1, len(VR1_alt)+1, 2)
for position, line in enumerate(VR1_alt):
    print(position, line)
    if position in VR1_line:
        VR1.append(line)

g = VR1
aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']
s = (len(aa), len(g[1]))
mat = numpy.zeros(s)
pos = numpy.arange(1, len(g[1]) + 1, 1)
# Make the Position Weight Matrix for each for each
for position, line in enumerate(g):
    for j in range(len(g[1])):
        for i in range(len(aa)):
            aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']
            j=j
            if line[j] == aa[i]:
                num = mat[i, j] + 1
                mat[i, j] = num
N = len(g)
print(mat)
ppm = mat / N
print(ppm)
b = 0.05
pwm = numpy.log2((ppm/b))
print(pwm)
# Make the heatmap
min = pwm[numpy.isfinite(pwm)].min()
max = pwm[numpy.isfinite(pwm)].max()
print(min, max)
seaborn.heatmap(pwm, vmin=min, vmax=max, cmap="YlGnBu", xticklabels=pos, yticklabels=aa)
plt.xlabel('Position on Sequence')
plt.ylabel('Amino Acid')
plt.show()

# Save Image
save_path = d
file_name = ('Heat Map of CDR3 with Length 17')
plt.savefig(os.path.join(save_path, file_name))
plt.show()

# Choose a different color scheme
# Expected Range -3 to 4 (expect some higher positives)
# Quality check - Get out the original seq if it matches
# Instead of:
# >1
# GGY
# Do;
# >low_fitness_1
# ggy

# Write a line to save just the lines
# Use VR1_7
# name = 'VR3_8_ex.fasta'
# CompName = os.path.join(save_path, name)
# file = open(CompName, 'w')
# for i in range(len(g)):
#     print(g[i])
#     file.write(str(g[i]) + "\n")
# file.close()
