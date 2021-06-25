import numpy
import seaborn
import matplotlib.pyplot as plt
import os

#Done
# SHort_High, Short_Low, Long_High
# Dissociate the Variable Regions by length and plot

# Import all the Variable regions
a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Short_High_VR\\VR1.fasta"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Short_High_VR\\VR2.fasta"
c = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Short_High_VR\\VR3.fasta"
d = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/Short_High_VR'

# Read all the files into a line

# VR1
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


# VR2
VR2_file = open(b)
VR2_nb = VR2_file.read()
VR2_alt = VR2_nb.splitlines()
VR2_file.close()
# Cut off the line
VR2 = []
VR2_line = numpy.arange(1, len(VR2_alt)+1, 2)
for position, line in enumerate(VR2_alt):
    print(position, line)
    if position in VR2_line:
        VR2.append(line)

# VR3
VR3_file = open(c)
VR3_nb = VR3_file.read()
VR3_alt = VR3_nb.splitlines()
VR3_file.close()
# Cut off the line
VR3 = []
VR3_line = numpy.arange(1, len(VR3_alt)+1, 2)
for position, line in enumerate(VR3_alt):
    print(position, line)
    if position in VR3_line:
        VR3.append(line)

print( 'VR1:', VR1, '\n VR2:', VR2, '\n VR3:', VR3 )
# Sort by length

# VR1 (length: 5 to 7)
VR1_5, VR1_6, VR1_7 = [], [], []
VR1_list = [VR1_5, VR1_6, VR1_7]
lenVR1 = numpy.arange(5, 8, 1)
numVR1 = numpy.zeros(1, len(VR1_list)) #Total number of aaseq per length
for position, line in enumerate(VR1):
    print(position, line)
    for i in range(len(VR1_list)):
        num = lenVR1[i]
        if len(line) == num:
            VR1_list[i].append(line)
            numVR1[i] = numVR1[i] + 1

# VR2 (length: 12 to 15)
VR2_12, VR2_13, VR2_14, VR2_15 = [], [], [], []
VR2_list = [VR2_12, VR2_13, VR2_14, VR2_15]
lenVR2 = numpy.arange(12, 16, 1)
numVR2 = numpy.zeros(1, len(VR2_list)) #Total number of aaseq per length
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
numVR3 = numpy.zeros(1, len(VR3_list)) #Total number of aaseq per length
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
        seaborn.heatmap(pwm, yticklabels=aa, vmin=0, xticklabels=pos)
        plt.title('Heat Map for High Amino Acids in %s for length: %d' % (VarRegName, VarRegLen))
        # Save the Image
        save_path = d
        file_name = ('Second_HeatMap_Short_High_%s_len_%d.png' %(VarRegName, VarRegLen))
        plt.savefig(os.path.join(save_path, file_name))
        plt.show()

# Choose a different color scheme
# Figure out the max and min situation
# Expected Range -3 to 4 (expect some higher positives)
# Quality check - Get out the original seq if it matches
# Plot a histogram of the different lengths present in the files
#       to see the distribution between the lengths
# Instead of:
# >1
# GGY
# Do;
# >low_fitness_1
# ggy