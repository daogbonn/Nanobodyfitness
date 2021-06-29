# Goal: Calculate the difference between the position weight matrices of the high and low fitness

import numpy
import seaborn
import matplotlib.pyplot as plt
import os


# Dissociate the Variable Regions by length and plot

# Import all the Variable regions
a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\long_High_VR\\VR1.fasta"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Long_High_VR\\VR2.fasta"
c = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Long_High_VR\\VR3.fasta"
d = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\long_Low_VR\\VR1.fasta"
e = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Long_Low_VR\\VR2.fasta"
f = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Long_Low_VR\\VR3.fasta"
g = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/'

# Read all the files into a line
file_loc = [a, b, c, d, e, f] # Location of the files
file_names = ['VR1_High_alt', 'VR2_High_alt', 'VR3_High_alt', 'VR1_Low_alt', 'VR2_Low_alt', 'VR3_Low_alt']
VR1_High, VR2_High, VR3_High, VR1_Low, VR2_Low, VR3_Low = [], [], [], [], [], []
files = [VR1_High, VR2_High, VR3_High, VR1_Low, VR2_Low, VR3_Low]


for i in range(len(file_loc)):
    open_file = open(file_loc[i])
    nb = open_file.read()
    alt = nb.splitlines()
    open_file.close()
    # Cut off line
    lis = files[i]
    lis_line = numpy.arange(1, len(alt)+1, 2)
    for position, line in enumerate(alt):
        print(position, line)
        if position in lis_line:
            lis.append(line)


# Sort by length

# VR1 (length: 5 to 7)
VR1_5L, VR1_6L, VR1_7L = [], [], []
VR1_5H, VR1_6H, VR1_7H = [], [], []
VR1L_list = [VR1_5L, VR1_6L, VR1_7L]
VR1H_list = [VR1_5H, VR1_6H, VR1_7H]
lenVR1 = numpy.arange(5, 8, 1)
numVR1L = [0, 0, 0]
numVR1H = [0, 0, 0]
num_VR1 = [numVR1L, numVR1H]
VR1_list = [VR1L_list, VR1H_list]
VR1_comp = [VR1_Low, VR1_High]
for i in range(len(VR1_comp)):
    VR1_now = VR1_comp[i]
    VR1_lis = VR1_list[i]
    numVR1 = num_VR1[i]
    for position, line in enumerate(VR1_now):
        print(position, line)
        for j in range(len(VR1_lis)):
            num = lenVR1[i]
            if len(line) == num:
                VR1_lis[i].append(line)
                numVR1[j] = numVR1[j] + 1



# VR2 (length: 12 to 15)
VR2_12, VR2_13, VR2_14, VR2_15 = [], [], [], []
VR2_list = [VR2_12, VR2_13, VR2_14, VR2_15]
lenVR2 = numpy.arange(12, 16, 1)
numVR2 = [0, 0, 0, 0]
for position, line in enumerate(VR2):
    print(position, line)
    for i in range(len(VR2_list)):
        num = lenVR2[i]
        if len(line) == num:
            VR2_list[i].append(line)
            numVR2[i] = numVR2[i] + 1


# VR2 (length: 8 to 22)
VR3_8, VR3_9, VR3_10, VR3_11, VR3_12, VR3_13, VR3_14, VR3_15, VR3_16, VR3_17, VR3_18, VR3_19, VR3_20, VR3_21, VR3_22 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
VR3_list = [VR3_8, VR3_9, VR3_10, VR3_11, VR3_12, VR3_13, VR3_14, VR3_15, VR3_16, VR3_17, VR3_18, VR3_19, VR3_20, VR3_21, VR3_22]
lenVR3 = numpy.arange(8, 23, 1)
numVR3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for position, line in enumerate(VR3):
    print(position, line)
    for i in range(len(VR3_list)):
        num = lenVR3[i]
        if len(line) == num:
            VR3_list[i].append(line)
            numVR3[i] = numVR3[i] + 1


VR1_list = [VR1_5, VR1_6, VR1_7]
VR2_list = [VR2_12, VR2_13, VR2_14, VR2_15]
VR3_list = [VR3_8, VR3_9, VR3_10, VR3_11, VR3_12, VR3_13, VR3_14, VR3_15, VR3_16, VR3_17, VR3_18, VR3_19, VR3_20, VR3_21, VR3_22]

VR_list = [VR1_5, VR1_6, VR1_7, VR2_12, VR2_13, VR2_14, VR2_15, VR3_8, VR3_9, VR3_10, VR3_11, VR3_12, VR3_13, VR3_14, VR3_15, VR3_16, VR3_17, VR3_18, VR3_19, VR3_20, VR3_21, VR3_22]
VR_list_Name = ['VR1_5', 'VR1_6', 'VR1_7', 'VR2_12', 'VR2_13', 'VR2_14', 'VR2_15', 'VR3_8', 'VR3_9', 'VR3_10', 'VR3_11', 'VR3_12', 'VR3_13', 'VR3_14', 'VR3_15', 'VR3_16', 'VR3_17', 'VR3_18', 'VR3_19', 'VR3_20', 'VR3_21', 'VR3_22']
print('VR_List:', VR_list)

VarReg_Name = ['CDR1', 'CDR1', 'CDR1', 'CDR2', 'CDR2', 'CDR2', 'CDR2', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3']
VarReg_Len = [5, 6, 7, 12, 13, 14, 15, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

# Make the Position Weight Matrix for each for each

aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']

for k in range(len(VR_list)):
    print(k)
    if len(VR_list[k]) >= 1:  # If VR_list contains something
        g = VR_list[k]
        s = (len(aa), len(g[1]))
        mat = numpy.zeros(s)  # matrix of 20 rows and length in column
        pos = numpy.arange(1, len(g[1])+1, 1)
        # Name
        VarRegName = VarReg_Name[k] # Which CDR region
        VarRegLen = VarReg_Len[k] # Which variable region
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
        plt.title('Heat Map for High Amino Acids in %s for length: %d' % (VarRegName, VarRegLen))
        # Save the Image
        save_path = g
        file_name = ('HeatMap_Long_High_%s_len_%d.png' %(VarRegName, VarRegLen))
        plt.savefig(os.path.join(save_path, file_name))
        plt.show()

# Quality check - Get out the original seq if it matches
# Instead of:
# >1
# GGY
# Do;
# >low_fitness_1
# ggy