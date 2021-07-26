# Goal
# 1 - Extract the Variable regions from the aaseq (CDR)
# 2 - Extract the CDR regions by length
# 3 - Count the number of CDR regions per length
# 4 - Plot the length diversity on a histogram
# 5 - Plot the amino acid sequence on a heatmap


# EXTRACTION
#a = 'C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Short_20200730_High_Fitness.fasta'
a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\20200730_MiSeqv3_High_fitness.fasta"
save_path = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/Long_High_VR'

import numpy
import os.path
import matplotlib.pyplot

# file_object = open(“filename”, “r”)

# Extract the file into a variable
short_nb_file = open(a)
short_nb = short_nb_file.read()
short_nb_list = short_nb.splitlines()
short_nb_file.close()
print(short_nb_list)

# Extract the amino acid sequence in the list
linea = []
posa = []
aaseq = []
aaseq_line = numpy.arange(1, len(short_nb_list), 3)  # Note this might change
for position, line in enumerate(short_nb_list):
    print(position, line)
    linea.append(line)
    posa.append(position)
    if position in aaseq_line:
        aaseq.append(line)


print('Amino Acid Sequence:', aaseq)


# Constant Regions
CR1 = 'QVQLVESGGGLVQAGGSLRLSCAASG'
CR2 = 'MGWYRQAPGKERE'
CR3 = 'YADSVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYC'
CR4 = 'WGQGTQVTVSS'

# Divide aaseq with and without constant region
aaseq_ana = [] # aaseq with constant region
aaseq_nana = [] # aaseq without constant region
# for position, line in enumerate(aaseq):
#     if CR1 in line:
#         if CR2 in line:
#             if CR3 in line:
#                 if CR4 in line:
#                     print('Constant Regions Confirmed in aa: ', position + 1)
#                     aaseq_ana.append(line)
#                 else:
#                     print('Constant Regions not confirmed in aa: ', position + 1)
#                     aaseq_nana.append(line)
#             else:
#                 print('Constant Regions not confirmed in aa: ', position + 1)
#                 aaseq_nana.append(line)
#         else:
#             print('Constant Regions not confirmed in aa: ', position + 1)
#             aaseq_nana.append(line)
#     else:
#         print('Constant Regions not confirmed in aa: ', position + 1)
#         aaseq_nana.append(line)

# Don't know why this is not working
for position, line in enumerate(aaseq):
    if CR1 and CR2 and CR3 and CR4 in line:
        print('Constant Regions Confirmed in aa: ', position + 1)
        aaseq_ana.append(line)
    else:
        print('Constant Regions not confirmed in aa: ', position + 1)
        aaseq_nana.append(line)

print('Amino Acid Seq to Use:', aaseq_ana)
print('Amino Acid Seq not confirmed:', aaseq_nana)

# Find the start and stop position for CDR
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

print('Start and stop pos', CR1_start, CR1_stop, CR2_start, CR2_stop, CR3_start, CR3_stop, CR4_start, CR4_stop)

# Extract VR, extract VR by length and sort
VR1, VR2, VR3 = [], [], []
lvr1, lvr2, lvr3 = [], [], []
exvr1, exvr2, exvr3 = [], [], []
lexvr1, lexvr2, lexvr3 = [], [], []

# VR1 (length: 5 to 7)
VR1_5, VR1_6, VR1_7 = [], [], []
VR1_list = [VR1_5, VR1_6, VR1_7]
lenVR1 = numpy.arange(5, 8, 1)
numVR1 = [0, 0, 0] #Total number of aaseq per length

# VR2 (length: 12 to 15)
VR2_12, VR2_13, VR2_14, VR2_15 = [], [], [], []
VR2_list = [VR2_12, VR2_13, VR2_14, VR2_15]
lenVR2 = numpy.arange(12, 16, 1)
numVR2 = [0, 0, 0, 0]

# VR3 (length: 8 to 22)
VR3_8, VR3_9, VR3_10, VR3_11, VR3_12, VR3_13, VR3_14, VR3_15, VR3_16, VR3_17, VR3_18, VR3_19, VR3_20, VR3_21, VR3_22 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
VR3_list = [VR3_8, VR3_9, VR3_10, VR3_11, VR3_12, VR3_13, VR3_14, VR3_15, VR3_16, VR3_17, VR3_18, VR3_19, VR3_20, VR3_21, VR3_22]
lenVR3 = numpy.arange(8, 23, 1)
numVR3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
    if 22 >= len(vr3) >= 8:
        VR3.append(vr3)
        lvr3.append(len(vr3))
    else:
        lexvr3.append(position)
        exvr3.append(vr3)

# Question - When one of the VR does not fit do we remove the entire line of aaseq

print('1st Variable Regions: ', VR1, '\n and the Length of VR1 is', len(VR1))
print('2nd Variable Regions: ', VR2, '\n and the Length of VR2 is', len(VR2))
print('3rd Variable Regions: ', VR3, '\n and the Length of VR3 is', len(VR3))

for position, line in enumerate(VR1):
    print(position, line)
    for i in range(len(VR1_list)):
        num = lenVR1[i]
        if len(line) == num:
            VR1_list[i].append(line)
            numVR1[i] = numVR1[i] + 1
for position, line in enumerate(VR2):
    print(position, line)
    for i in range(len(VR2_list)):
        num = lenVR2[i]
        if len(line) == num:
            VR2_list[i].append(line)
            numVR2[i] = numVR2[i] + 1
for position, line in enumerate(VR3):
    print(position, line)
    for i in range(len(VR3_list)):
        num = lenVR3[i]
        if len(line) == num:
            VR3_list[i].append(line)
            numVR3[i] = numVR3[i] + 1
print('The final count:\n', 'VR1', numVR1, '\nVR2', numVR2, '\nVR3', numVR3)


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

# Saving the aaseq into their respective files
VR_list = [VR1_5, VR1_6, VR1_7, VR2_12, VR2_13, VR2_14, VR2_15, VR3_8, VR3_9, VR3_10, VR3_11, VR3_12, VR3_13, VR3_14, VR3_15, VR3_16, VR3_17, VR3_18, VR3_19, VR3_20, VR3_21, VR3_22]
VR_list_Name = ['VR1_5.fasta', 'VR1_6.fasta', 'VR1_7.fasta', 'VR2_12.fasta', 'VR2_13.fasta', 'VR2_14.fasta', 'VR2_15.fasta', 'VR3_8.fasta', 'VR3_9.fasta', 'VR3_10.fasta', 'VR3_11.fasta', 'VR3_12.fasta', 'VR3_13.fasta', 'VR3_14.fasta', 'VR3_15.fasta', 'VR3_16.fasta', 'VR3_17.fasta', 'VR3_18.fasta', 'VR3_19.fasta', 'VR3_20.fasta', 'VR3_21.fasta', 'VR3_22.fasta']
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
        print(VR)
        file.close()



# Create a histogram image for the length
numVR = numpy.concatenate((numVR1, numVR2, numVR3), axis=None)
name = 'Hist_Data.fasta'
VR_list_Name = ['VR1_5', 'VR1_6', 'VR1_7', 'VR2_12', 'VR2_13', 'VR2_14', 'VR2_15', 'VR3_8', 'VR3_9', 'VR3_10', 'VR3_11', 'VR3_12', 'VR3_13', 'VR3_14', 'VR3_15', 'VR3_16', 'VR3_17', 'VR3_18', 'VR3_19', 'VR3_20', 'VR3_21', 'VR3_22']
CompName = os.path.join(save_path, name)
file = open(CompName, 'w')
for i in range(len(numVR)):
    print(VR_list_Name[i], numVR[i])
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

#
# name = 'VR1_7_ex.fasta'
# CompName = os.path.join(save_path, name)
# file = open(CompName, 'w')
# for i in range(len(g)):
#     print(g[i])
#     file.write(str(g[i]) + "\n")
# file.close()
