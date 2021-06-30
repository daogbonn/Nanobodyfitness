# Matrix Extraction

# Goal - Analyze the data at each position using the pfm and conducting tests
# What - Obtain the pfm (in this case it is mat)
#       - For each position or column, calculate the proportion of amino acids
#       - Carry out test to see the proportion and the siginificance score

import numpy
import seaborn
import matplotlib.pyplot as plt
import os



# Import all the Variable regions
a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Long_High_VR\\VR1.fasta"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Long_High_VR\\VR2.fasta"
c = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Long_High_VR\\VR3.fasta"
d = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Long_Low_VR\\VR1.fasta"
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



VR1_5L, VR1_6L, VR1_7L = [], [], []
VR1_5H, VR1_6H, VR1_7H = [], [], []
VR2_12L, VR2_13L, VR2_14L, VR2_15L = [], [], [], []
VR2_12H, VR2_13H, VR2_14H, VR2_15H = [], [], [], []
VR3_8L, VR3_9L, VR3_10L, VR3_11L, VR3_12L, VR3_13L, VR3_14L, VR3_15L, VR3_16L, VR3_17L, VR3_18L, VR3_19L, VR3_20L, VR3_21L, VR3_22L = [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
VR3_8H, VR3_9H, VR3_10H, VR3_11H, VR3_12H, VR3_13H, VR3_14H, VR3_15H, VR3_16H, VR3_17H, VR3_18H, VR3_19H, VR3_20H, VR3_21H, VR3_22H = [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

VR1L_list = [VR1_5L, VR1_6L, VR1_7L]
VR1H_list = [VR1_5H, VR1_6H, VR1_7H]
VR2L_list = [VR2_12L, VR2_13L, VR2_14L, VR2_15L]
VR2H_list = [VR2_12H, VR2_13H, VR2_14H, VR2_15H ]
VR3L_list = [VR3_8L, VR3_9L, VR3_10L, VR3_11L, VR3_12L, VR3_13L, VR3_14L, VR3_15L, VR3_16L, VR3_17L, VR3_18L, VR3_19L, VR3_20L, VR3_21L, VR3_22L]
VR3H_list = [VR3_8H, VR3_9H, VR3_10H, VR3_11H, VR3_12H, VR3_13H, VR3_14H, VR3_15H, VR3_16H, VR3_17H, VR3_18H, VR3_19H, VR3_20H, VR3_21H, VR3_22H]

lenVR1 = numpy.arange(5, 8, 1)
lenVR2 = numpy.arange(12, 16, 1)
lenVR3 = numpy.arange(8, 23, 1)
lenVR = [lenVR1, lenVR2, lenVR3]

numVR1L = [0, 0, 0]
numVR1H = [0, 0, 0]
numVR2L = [0, 0, 0, 0]
numVR2H = [0, 0, 0, 0]
numVR3L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numVR3H = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

num_VR1 = [numVR1L, numVR1H]
num_VR2 = [numVR2L, numVR2H]
num_VR3 = [numVR3L, numVR3H]
num_VR = [num_VR1, num_VR2, num_VR3]

VR1_list = [VR1L_list, VR1H_list]
VR2_list = [VR2L_list, VR2H_list]
VR3_list = [VR3L_list, VR3H_list]
VR_list = [VR1_list, VR2_list, VR3_list]

VR1_comp = [VR1_Low, VR1_High]
VR2_comp = [VR2_Low, VR2_High]
VR3_comp = [VR3_Low, VR3_High]
VR_comp = [VR1_comp, VR2_comp, VR3_comp]

for k in range(len(VR_comp)): # Which VR section
    VR_now = VR_comp[k]
    VR_lis = VR_list[k]
    numVR = num_VR[k]
    len_VR = lenVR[k]
    for i in range(len(VR_now)): #Choosing High or Low
        vrnow = VR_now[i] #VR1_low
        vrlis = VR_lis[i]
        numvr = numVR[i]
        for position, line in enumerate(vrnow):
            print(position, line)
            for j in range(len(vrlis)):
                num = len_VR[j]
                if len(line) == num:
                    vrlis[j].append(line)
                    numvr[j] = numvr[j]+1

VarReg_Name = ['CDR1', 'CDR1', 'CDR1', 'CDR2', 'CDR2', 'CDR2', 'CDR2', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3', 'CDR3']
VarReg_Len = [5, 6, 7, 12, 13, 14, 15, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

VRL_list = [VR1_5L, VR1_6L, VR1_7L, VR2_12L, VR2_13L, VR2_14L, VR2_15L, VR3_8L, VR3_9L, VR3_10L, VR3_11L, VR3_12L, VR3_13L, VR3_14L, VR3_15L, VR3_16L, VR3_17L, VR3_18L, VR3_19L, VR3_20L, VR3_21L, VR3_22L]
VRH_list = [VR1_5H, VR1_6H, VR1_7H, VR2_12H, VR2_13H, VR2_14H, VR2_15H, VR3_8H, VR3_9H, VR3_10H, VR3_11H, VR3_12H, VR3_13H, VR3_14H, VR3_15H, VR3_16H, VR3_17H, VR3_18H, VR3_19H, VR3_20H, VR3_21H, VR3_22H]
print('len of VRlist:', len(VRH_list), len(VRL_list))
# Make the Position Weight Matrix for each for each
aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']
for k in range(22): #VRL_list = [VR1_5L, VR1_6L, VR1_7L, VR2_12L
    print(k)
    print('Num of amino acids:', len(VRL_list[k]), len(VRH_list[k]))
    if len(VRL_list[k]) >= 1 and len(VRH_list[k]) >= 1:
        # Can put another if statement for if there is one and not the other.
        gL = VRL_list[k]
        gH = VRH_list[k]
        s = (len(aa), len(gL[0]))
        matL = numpy.zeros(s, dtype=int)
        matH = numpy.zeros(s, dtype=int)
        pos = numpy.arange(1, len(gL[0])+1, 1)
        VarRegName = VarReg_Name[k]  # Which CDR region
        VarRegLen = VarReg_Len[k]  # Which variable region
        print(VarRegLen, VarRegName)
        for position, line in enumerate(gL):
            for j in range(len(gL[0])):
                for i in range(len(aa)):
                    aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']
                    j=j
                    if line[j] == aa[i]:
                        num = matL[i, j] + 1
                        matL[i, j] = num
        for position, line in enumerate(gH):
            for j in range(len(gH[0])):
                for i in range(len(aa)):
                    aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']
                    j=j
                    if line[j] == aa[i]:
                        num = matL[i, j] + 1
                        matH[i, j] = num
        NL = len(gL)
        NH = len(gH)
        print(matL, matH)
        ppmL = matL/ NL
        ppmH = matH/ NH
        print(ppmL, ppmH)
        b = 0.05
        pwmL = numpy.log2((ppmL / b))
        pwmH = numpy.log2((ppmH / b))
        pwm = pwmH-pwmL
        print(pwmL, pwmH)
        print(pwm)

        # Save the Matrix # Adjust name to fit path
        matLname = ('C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/Matrix/FreqMatrix/freqMatrix_Long_Low_%s_%d' % (VarRegName, VarRegLen))
        matHname = ('C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/Matrix/FreqMatrix/freqMatrix_Long_High_%s_%d' % (VarRegName, VarRegLen))
        ppmLname = ('C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/Matrix/PpmMatrix/ppmMatrix_Long_Low_%s_%d' % (VarRegName, VarRegLen))
        ppmHname = ('C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/Matrix/PpmMatrix/ppmMatrix_Long_High_%s_%d' % (VarRegName, VarRegLen))
        numpy.savetxt(matLname, matL, delimiter=',') # to convert to int also matL.astype(int)
        numpy.savetxt(matHname, matH, delimiter=',')
        numpy.savetxt(ppmLname, ppmL, delimiter=',')  # to convert to int also matL.astype(int)
        numpy.savetxt(ppmHname, ppmH, delimiter=',')
        print(matL, matH)

        # path = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/Matrix'
        # matLname = ('Matrix_ShortLow2_%s_%d.fasta' % (VarRegName, VarRegLen))
        # CompName = os.path.join(path, matLname)
        # file = open(CompName, 'w')
        # for b in range(len(matL)):
        #     file.write(matL[b] + "\n")
        # file.close()
        #
        # matHname = ('Matrix_ShortHigh2_%s_%d.fasta' % (VarRegName, VarRegLen))
        # CompName = os.path.join(path, matHname)
        # file = open(CompName, 'w')
        # for c in range(len(matH)):
        #     file.write(matH[c] + "\n")
        # file.close()


# Problem - k doesnt go till 22
# What happens when there is some amino acids in one and none in the other? (Ex amino acids in CDR8 for high and none for CDR8low)


# for i in range()  array_example[row1][2]]
# Y and G  YYEF as YYYY
# Numbers of Ys and Gs seen, position dominance
# Average No. of Ys and Gs, Nos. of Y's in the region
# Do a statistical test - chi-squared test
# Fourth to last position, look between E and G in the aaseq pos[-4]
