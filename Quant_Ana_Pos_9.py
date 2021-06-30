# Quant Analysis
#
# Goal - Analyze data at position9


import numpy
import os
import matplotlib.pyplot as plt
import statistics
import scipy.stats
from scipy import stats

save_path = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data'

varRegLen = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] # len:15
varRegFit = ['High', 'Low']
files_freq = []
files_ppm = []

for i in range(len(varRegFit)):
    for j in range(len(varRegLen)):
        fnamefreq = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Matrix\\FreqMatrix\\freqMatrix_Long_%s_CDR3_%d" % (varRegFit[i], varRegLen[j])
        fnameppm = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Matrix\\PpmMatrix\\ppmMatrix_Long_%s_CDR3_%d" % (varRegFit[i], varRegLen[j])
        files_freq.append(fnamefreq)
        files_ppm.append(fnameppm)

print(files_freq)
print(files_ppm)

# Read all the lines into a file
# masmat = numpy.zeros([1, len(varRegLen)])
# masppm = numpy.zeros([1, len(varRegLen)])


masmat = [[] for a in range(2*len(varRegLen)) ]
masppm = [[] for a in range(2*len(varRegLen))]

print(masmat, masppm)
print(len(masmat), len(masppm))

for i in range(len(files_freq)):
    open_file = open(files_freq[i])
    nb = open_file.read()
    lis = nb.splitlines()
    masmat[i] = lis
    open_file.close()
    #ppm open file
    open_file = open(files_ppm[i])
    nb = open_file.read()
    lis = nb.splitlines()
    masppm[i] = lis
    open_file.close()

# Convert strings to floats
# Assumption: masmat and masppm are of the same length
for i in range(len(masmat)):
    for k in range(len(masmat[i])):
        arr = masmat[i][k]
        brr = arr.split(',')
        masmat[i][k] = numpy.array(brr, dtype=float)
        arr2 = masppm[i][k]
        brr2 = numpy.array(arr2.split(','))
        # print(brr2)
        # print(brr2.astype(numpy.float))
        # masppm[i][k] = brr2.astype(numpy.float)
        masppm[i][k] = numpy.array(brr2, dtype=float)

# print(len(masppm))
# print(len(masppm[0]))
# print(len(masppm[0][0]))

# Dissociate into high and low
# Ordering in matrix is High first then low
matLnames = []
matHnames = []
ppmLnames = []
ppmHnames = []

for i in range(len(varRegLen)):
    mL = 'matL_%d' % (varRegLen[i])
    matLnames.append(mL)
    mH = 'matH_%d' % (varRegLen[i])
    matHnames.append(mH)
    pL = 'ppmL_%d' % (varRegLen[i])
    ppmLnames.append(pL)
    pH = 'ppmH_%d' % (varRegLen[i])
    ppmHnames.append(pH)

for i in range(len(matLnames)):
    matLnames[i], matHnames[i], ppmHnames[i], ppmLnames[i] = [], [], [], []

lenH = numpy.arange(0, 15)
lenL = numpy.arange(15, 30)

for i in range(len(masmat)):
    if i in lenH:
        matHnames[i] = masmat[i]
        ppmHnames[i] = masppm[i]
    elif i in lenL:
        for k in range(len(matLnames)):
            j = k+15
            if i == j:
                # print(i)
                # print(k)
                matLnames[k] = masmat[i]
                ppmLnames[k] = masppm[i]


aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']

# print(len(ppmLnames))
print(len(ppmLnames[0]))
print(len(ppmLnames[0][0]))
print(len(masppm[15][0]))


# Analysis - look at position 9
# Extract all the ppms at position 9


# list of lists with each CDR region
pos9ppmL = [[] for a in range(len(varRegLen))]
pos9ppmH = [[] for a in range(len(varRegLen))]

for i in range(len(ppmLnames)): #len 8 - 22
     for k in range(len(ppmLnames)): # CDR regions on the receiving side
         for j in range(len(ppmLnames[i])):  # Amino Acids
             if i== k:
                pos9ppmL[k].append(ppmLnames[i][j][-4])
                pos9ppmH[k].append(ppmHnames[i][j][-4])

print(len(pos9ppmL))
print(len(pos9ppmL[0]))


# Find the average between high and low across the columns
avepos9ppmL = []
avepos9ppmH = []

#print(pos9ppmL[0])
for i in range(len(pos9ppmL[0])): # Per Amino Acid
    avL, avH = 0, 0
    for j in range(len(pos9ppmL)): # per CDR
        avL = pos9ppmL[j][i] + avL
        avH = pos9ppmH[j][i] + avL
    avepos9ppmL.append(avL/len(pos9ppmL))
    avepos9ppmH.append(avH/len(pos9ppmH))

print(avepos9ppmH)
print(avepos9ppmL)

# # Plot
plt.plot(aa, avepos9ppmL)
plt.plot(aa, avepos9ppmH)
plt.legend(['Low Fitness', 'High Fitness'])
plt.xlabel('Amino Acids')
plt.ylabel('Proportion')
plt.title('Plot of proportion of Amino Acids in CDR3 at position -4')
file_name = ('Prop of AA at pos -4')
plt.savefig(os.path.join(save_path, file_name))
plt.show()

# T-test
t = stats.ttest_ind(avepos9ppmH, avepos9ppmL,equal_var=False)
print(t)
# p-value = 0.7533791222248756
# Can't say that there is a difference between the means
# Can you compare both because they are not normally distributed

# Man White Test
# assume it is not normally distributed
mw = scipy.stats.mannwhitneyu(avepos9ppmH, avepos9ppmL)
print(mw)
# p-value = 0.6597609090632409
# Can't say that there is a difference between the means
