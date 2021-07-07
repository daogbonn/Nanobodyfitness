# Plotting Histogram of data

import numpy
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Import Data
a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Long_High_VR\\Hist_Data.fasta"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Long_Low_VR\\Hist_Data.fasta"
d = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data'

# Long High
LongHigh_file = open(a)
Long_nb = LongHigh_file.read()
LongHigh_list = Long_nb.splitlines()
LongHigh_file.close()
print(LongHigh_list)

# Extract the amino acid sequence in the list
linea = []
posa = []
numLoHi= []
num_line = numpy.arange(1, len(LongHigh_list), 2)  # Note this might change
for position, line in enumerate(LongHigh_list):
    linea.append(line)
    posa.append(position)
    if position in num_line:
        numLoHi.append(float(line))
print(numLoHi)

# Long Low
LongLow_file = open(b)
Long_nb = LongLow_file.read()
LongLow_list = Long_nb.splitlines()
LongLow_file.close()
print(LongLow_list)

# Extract the amino acid sequence in the list
linea = []
posa = []
numLoLo= []
num_line = numpy.arange(1, len(LongLow_list), 2)  # Note this might change
for position, line in enumerate(LongLow_list):
    linea.append(line)
    posa.append(position)
    if position in num_line:
        numLoLo.append(float(line))
print(numLoLo)

print(type(numLoLo[1]))
VR_list = ['CDR1_5', 'CDR1_6', 'CDR1_7', 'CDR2_12', 'CDR2_13', 'CDR2_14', 'CDR2_15', 'CDR3_8', 'CDR3_9', 'CDR3_10', 'CDR3_11', 'CDR3_12', 'CDR3_13', 'CDR3_14', 'CDR3_15', 'CDR3_16', 'CDR3_17', 'CDR3_18', 'CDR3_19', 'CDR3_20', 'CDR3_21', 'CDR3_22']


# Plot of both side by side
x = numpy.arange(len(VR_list))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, numLoHi, width, label='High Fitness')
rects2 = ax.bar(x + width/2, numLoLo, width, label='Low Fitness')
ax.set_ylabel('Number of Sequences')
ax.set_xlabel('CDR region lengths')
ax.set_xticks(x)
ax.set_xticklabels(VR_list)
plt.xticks(rotation = 45)
plt.title('Histogram of Length of CDR Regions')
ax.legend()
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
fig.tight_layout()
save_path = d
file_name = ('Histogram of Lengths of VR Regions')
plt.savefig(os.path.join(save_path, file_name))
plt.show()

