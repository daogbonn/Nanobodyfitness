# Quant Analysis
#
# Goal - Analyze the data at each position using the pfm and conducting tests
# What - Obtain the pfm (in this case it is mat)
#       - For each position or column, calculate the proportion of amino acids
#       - Carry out test to see the proportion and the siginificance score


import numpy
import matplotlib.pyplot as plt

a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Matrix\\FreqMatrix\\freqMatrix_Long_Low_CDR3_12"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Matrix\\FreqMatrix\\freqMatrix_Long_High_CDR3_12"
c = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Matrix\\PpmMatrix\\ppmMatrix_Long_Low_CDR3_12"
d = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Matrix\\PpmMatrix\\ppmMatrix_Long_High_CDR3_12"

# Read all the files into a line
file_loc = [a, b, c, d] # Location of the files
matL, matH, ppmL, ppmH = [], [], [], []
mat = [matL, matH, ppmL, ppmH] # an array of 4 with each having 21 lines
pfm = [matL, matH]
ppm = [ppmL, ppmH]

for i in range(len(file_loc)):
    open_file = open(file_loc[i])
    nb = open_file.read()
    lis = nb.splitlines()
    mat[i] = lis
    print(type(lis))
    open_file.close()

# Convert strings to floats
for i in range(len(mat)):
    for k in range(len(mat[i])):
        arr = mat[i][k]
        brr = arr.split(',')
        mat[i][k] = numpy.array(brr, dtype=float)

matL, matH, ppmL, ppmH = mat[0], mat[1], mat[2], mat[3]

# Note for each matrix rows are amino acids and columns are positions
# Note - matL - 21  to get to position matL[][9]

aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']

# First: look at position 9

# Extract all the ppms at position 9
pos9ppmL, pos9ppmH = [], []
for i in range(len(ppmL)):
    pos9ppmL.append(ppmL[i][9])
    pos9ppmH.append(ppmH[i][9])

print(pos9ppmL)
print(pos9ppmH)

# Plot
plt.plot(aa, pos9ppmL)
plt.plot(aa, pos9ppmH)
plt.legend(['Low Fitness', 'High Fitness'])
plt.xlabel('Amino Acids')
plt.ylabel('Proportion(%)')
plt.title('Plot of proportion of Amino Acids in CDR3_12 at position 9')
plt.show()
