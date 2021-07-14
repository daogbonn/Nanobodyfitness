
# EXTRACTION
# Goal - extract the data from the fasta file and organize into groups

# Start with High fitness data
# a = 'C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\short_high_20.fasta'
a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\combined_clean_aln_high.fasta"
save_path = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/Long_High_VR'
#save_path = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/Short_High_VR'

import numpy
import os.path
import matplotlib.pyplot as plt

# data_short = numpy.loadtxt(fname='20200730_High_Fitness.fasta', delimiter=',')
# print (data_short)
b = 'Short_20200730_Low_fitness.fasta'
short_nb_file = open(a)  # default - r - open for reading
short_nb = short_nb_file.read()
# print(short_nb)

# to split into lines
short_nb_list = short_nb.splitlines()
# use splitlines to split the line
short_nb_file.close()
print(short_nb_list)

linea = []
posa = []
aaseq = []
aaseq_line = numpy.arange(1, len(short_nb_list), 2)  # Note this might change
for position, line in enumerate(short_nb_list):
    print(position, line)
    linea.append(line)
    # all the lines of the fasta file
    posa.append(position)
    # the position of the corresponding fasta lines
    if position in aaseq_line:
        aaseq.append(line)
        # To extract the aa lines

print('line is :', linea)
print('position is:', posa)
print(aaseq_line)
print('Amino Acid Sequence:', aaseq)
print(len(short_nb_list)) #meant to be 42
print(len(aaseq)) # meanr to be 21

# Here - the data is loaded and split into its lines so position 1 has line 1
# linea has the lines
# aa seq occurs in multiples from line 1

# Need line to automatically find constant regions

# Confirm the constant regions
CR1 = 'QVQLVESGGGLVQAGGSLRLSCAASG'
CR2 = 'MGWYRQAPGKERE'
CR3 = 'YADSVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYC'
CR4 = 'WGQGTQVTVSS--'

# Possible things - c
# 5 and 3 should not be confirmed for the short
aaseq_ana = [] # Analyzed Amino Acids_High
aaseq_nana = [] # Unanalyzed amino acids
for position, line in enumerate(aaseq):
    if CR1 in line:
        if CR2 in line:
            if CR3 in line:
                if CR4 in line:
                    print('Constant Regions Confirmed in aa: ', position + 1)
                    aaseq_ana.append(line)
                else:
                    print('Constant Regions not confirmed in aa: ', position + 1)
                    aaseq_nana.append(line)
            else:
                print('Constant Regions not confirmed in aa: ', position + 1)
                aaseq_nana.append(line)
        else:
            print('Constant Regions not confirmed in aa: ', position + 1)
            aaseq_nana.append(line)
    else:
        print('Constant Regions not confirmed in aa: ', position + 1)
        aaseq_nana.append(line)

# Don't know why this is not working
# for position, line in enumerate(aaseq):
#     if CR1 and CR2 and CR3 and CR4 in line:
#         print('Constant Regions Confirmed in aa: ', position + 1)
#         aaseq_ana.append(line)
#     else:
#         print('Constant Regions not confirmed in aa: ', position + 1)
#         aaseq_nana.append(line)

print('Amino Acid Seq to Use:', aaseq_ana)
print('Amino Acid Seq not confirmed:', aaseq_nana)

# Find the points where the CR starts and stops
CR1_start = []  # Contains the start position of each CR1 position for each of the aaseq. index 1 is for aa 1 and so on
CR1_stop = []
CR2_start = []
CR2_stop = []
CR3_start = []
CR3_stop = []
CR4_start = []
CR4_stop = []
for position, line in enumerate(aaseq_ana):
    CR1_start.append(aaseq_ana[position].find(CR1))
    CR1_stop.append(aaseq_ana[position].find(CR1) + len(CR1))
    CR2_start.append(aaseq_ana[position].find(CR2))
    CR2_stop.append(aaseq_ana[position].find(CR2) + len(CR2))
    CR3_start.append(aaseq_ana[position].find(CR3))
    CR3_stop.append(aaseq_ana[position].find(CR3) + len(CR3))
    CR4_start.append(aaseq_ana[position].find(CR4))
    CR4_stop.append(aaseq_ana[position].find(CR4) + len(CR4))

print('Start positions of CR1 for each aaseq:', CR1_start)
print('Stop positions of CR1 for each aaseq:', CR1_stop)
print('Start positions of CR2 for each aaseq:', CR2_start)
print('Stop positions of CR2 for each aaseq:', CR2_stop)
print('Start positions of CR3 for each aaseq:', CR3_start)
print('Stop positions of CR3 for each aaseq:', CR3_stop)
print('Start positions of CR4 for each aaseq:', CR4_start)
print('Stop positions of CR4 for each aaseq:', CR4_stop)

# Extract VR and check if it is within the limits
VR1, VR2, VR3, VR4 = [], [], [], []
lvr1, lvr2, lvr3, lvr4 = [], [], [], []
exvr1, exvr2, exvr3 = [], [], []
lexvr1, lexvr2, lexvr3 = [], [], []
for position, line in enumerate(aaseq_ana):
    vr1 = line[CR1_stop[position]:CR2_start[position]]
    vr2 = line[CR2_stop[position]:CR3_start[position]]
    vr3 = line[CR3_stop[position]:CR4_start[position]]
    if 7 >= len(vr1) >= 5:
        VR1.append(vr1)
        lvr1.append(len(vr1))
    else:
        lexvr1.append(position)
        exvr1.append(vr1)
    if 15 >= len(vr2) >= 12:
        VR2.append(vr2)
        lvr2.append(len(vr2))
    else:
        lexvr2.append(position)
        exvr2.append(vr3)
    if 30 >= len(vr3) >= 20:
        VR3.append(vr3)
        lvr3.append(len(vr3))
    else:
        lexvr3.append(position)
        exvr3.append(vr3)
# Question - When one of the VR does not fit do we remove the entire line of aaseq

print('1st Variable Regions: ', VR1, '\n and the Length of VR1 is', len(VR1))
print('2nd Variable Regions: ', VR2, '\n and the Length of VR2 is', len(VR2))
print('3rd Variable Regions: ', VR3, '\n and the Length of VR3 is', len(VR3))
print('Length of Characters in VR1 is', lvr1)
print('Length of Characters in VR2 is', lvr2)
print('Length of Characters in VR3 is', lvr3)

print(exvr1, exvr2, exvr3)
print(lexvr1, lexvr2, lexvr3)

# Save each of the variable regions in their own fasta file
# Example -
# >1
# CDR1
# >2
# CDR1 for aa 2e.t.c

# Write into a fasta file

CompName = os.path.join(save_path, 'VR1.fasta')
file = open(CompName, 'w')
for i in range(len(VR1)):
    num = str(i + 1)
    file.write(">" + num + "\n" + VR1[i] + "\n")
file.close()

oCompName = os.path.join(save_path, 'VR2.fasta')
ofile = open(oCompName, 'w')
for i in range(len(VR2)):
    num = str(i + 1)
    ofile.write(">" + num + "\n" + VR2[i] + "\n")
ofile.close()

iCompName = os.path.join(save_path, 'VR3.fasta')
ifile = open(iCompName, 'w')
for i in range(len(VR3)):
    num = str(i + 1)
    ifile.write(">" + num + "\n" + VR3[i] + "\n")
ifile.close()

zCompName = os.path.join(save_path, 'rmvd_aaseq.fasta')
zfile = open(zCompName, 'w')
for i in range(len(aaseq_nana)):
    num = str(i + 1)
    zfile.write(">" + num + "\n" + aaseq_nana[i] + "\n")
zfile.close()

# Tabulate the amount of amino acids per position
# Question - do they differ between all groups (LOW AND HIGH)

# Not of the same length; keep track of length of VR regions
# take to multiple sequence alignment and then weblogo


# Sort by length and save and plot histogram
# VR1 (length: 5 to 7)
VR1_5, VR1_6, VR1_7 = [], [], []
VR1_list = [VR1_5, VR1_6, VR1_7]
lenVR1 = numpy.arange(5, 8, 1)
numVR1 = [0, 0, 0] #Total number of aaseq per length
print(numVR1)
for position, line in enumerate(VR1):
    print(position, line)
    for i in range(len(VR1_list)):
        num = lenVR1[i]
        print(num)
        if len(line) == num:
            VR1_list[i].append(line)
            print(numVR1[i])
            numVR1[i] = numVR1[i] + 1


# VR2 (length: 12 to 15)
VR2_12, VR2_13, VR2_14, VR2_15 = [], [], [], []
VR2_list = [VR2_12, VR2_13, VR2_14, VR2_15]
lenVR2 = numpy.arange(12, 16, 1)
numVR2 = [0, 0, 0, 0] #Total number of aaseq per length
for position, line in enumerate(VR2):
    print(position, line)
    for i in range(len(VR2_list)):
        num = lenVR2[i]
        if len(line) == num:
            VR2_list[i].append(line)
            numVR2[i] = numVR2[i] + 1


# VR2 (length: 8 to 22)
VR3_20, VR3_21, VR3_22, VR3_23, VR3_24, VR3_25, VR3_26, VR3_27, VR3_28, VR3_29, VR3_30 = [], [], [], [], [], [], [], [], [], [], []
VR3_list = [VR3_20, VR3_21, VR3_22, VR3_23, VR3_24, VR3_25, VR3_26, VR3_27, VR3_28, VR3_29, VR3_30]
lenVR3 = numpy.arange(20, 31, 1)
numVR3 =  [0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Total number of aaseq per length
for position, line in enumerate(VR3):
    print(position, line)
    for i in range(len(VR3_list)):
        num = lenVR3[i]
        if len(line) == num:
            VR3_list[i].append(line)
            numVR3[i] = numVR3[i] + 1


# Saving the aaseq into their respective files
VR_list = [VR1_5, VR1_6, VR1_7, VR2_12, VR2_13, VR2_14, VR2_15, VR3_20, VR3_21, VR3_22, VR3_23, VR3_24, VR3_25, VR3_26, VR3_27, VR3_28, VR3_29, VR3_30]
VR_list_Name = ['VR1_5.fasta', 'VR1_6.fasta', 'VR1_7.fasta', 'VR2_12.fasta', 'VR2_13.fasta', 'VR2_14.fasta', 'VR2_15.fasta', 'VR3_20.fasta', 'VR3_21.fasta', 'VR3_22.fasta', 'VR3_23.fasta', 'VR3_24.fasta', 'VR3_25.fasta', 'VR3_26.fasta', 'VR3_27.fasta', 'VR3_28.fasta', 'VR3_29.fasta', 'VR3_30.fasta']
print('VR_List:', VR_list)

for i in range(len(VR_list)):
    if len(VR_list[i]) >= 1:
        name = VR_list_Name[i]
        print(name)
        CompName = os.path.join(save_path, name)
        file = open(CompName, 'w')
        for k in range(len(VR_list[i])):
            num = str(k + 1)
            VR = VR_list[i]
            file.write(">" + num + "\n" + VR[k] + "\n")
        file.close()


# Create a histogram image for the length
numVR = numpy.concatenate((numVR1, numVR2, numVR3), axis=None)
name = 'Hist Data'
VR_list_Name = ['VR1_5', 'VR1_6', 'VR1_7', 'VR2_12', 'VR2_13', 'VR2_14', 'VR2_15', 'VR3_20', 'VR3_21', 'VR3_22', 'VR3_23', 'VR3_24', 'VR3_25', 'VR3_26', 'VR3_27', 'VR3_28', 'VR3_29', 'VR3_30']
CompName = os.path.join(save_path, name)
file = open(CompName, 'w')
for i in range(len(numVR)):
    file.write(">" + VR_list_Name[i] + "\n" + str(numVR[i]) + "\n")
file.close()


# Loop through sequence only once
# Create object to store all sequences, and CDR
# put together the list of strings that you want to write out
# Open all the files you want to open and write in each individual ones and close
# Call write lines - writes all items to the list. (For faster output)
# writelines(List) List = 'aaseq1', '/n', 'aaseq2' ...
# List: VR_list[i] = [“>low_fitness_1\n”, “GFGFGF\n”]
# VR1_7_file.writelines(VR_list[i])
# Update github

# print(numVR)
# VR_list_Name = ['VR1_5', 'VR1_6', 'VR1_7', 'VR2_12', 'VR2_13', 'VR2_14', 'VR2_15', 'VR3_8', 'VR3_9', 'VR3_10', 'VR3_11', 'VR3_12', 'VR3_13', 'VR3_14', 'VR3_15', 'VR3_16', 'VR3_17', 'VR3_18', 'VR3_19', 'VR3_20', 'VR3_21', 'VR3_22']
# n, bins, patches = plt.hist( x=numVR, bins=len(VR_list_Name))
# # plt.show()
