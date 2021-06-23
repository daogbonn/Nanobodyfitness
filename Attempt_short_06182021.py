
# EXTRACTION
# Goal - extract the data from the fasta file and organize into groups

# Start with High fitness data
a = 'C:/Users/ITSloaner/OneDrive/Documents/Nanobodyfitnenss/20200730_MiSeqv3_low_fitness.fasta'

import numpy

# data_short = numpy.loadtxt(fname='20200730_High_Fitness.fasta', delimiter=',')
# print (data_short)
b = 'Short_20200730_Low_fitness.fasta'
short_nb_file = open(b)  # default - r - open for reading
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
aaseq_line = numpy.arange(1, len(short_nb_list), 3)  # Note this might change
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

# Here - the data is loaded and split into its lines so position 1 has line 1
# linea has the lines
# aa seq occurs in multiples from line 1

# Need line to automatically find constant regions


# Confirm the constant regions
CR1 = 'QVQLVESGGGLVQAGGSLRLSCAASG'
CR2 = 'WYRQAPGKERE'
CR3 = 'YADSVKGRFTISRDNAKNTVYLQMNSLKPE'
CR4 = 'WGQGTQVTVSS'

# Possible things - c

for position, line in enumerate(aaseq):
    if CR1 and CR2 and CR3 and CR4 in line:
        print('Constant Regions Confirmed in aa: ', position + 1)
    else:
        print('Constant Regions not confirmed in aa: ', position + 1)
# Include a check line

print(aaseq[1])
print(aaseq[1].find(CR1))

# Find the points where the CR starts and stops
CR1_start = []  # Contains the start position of each CR1 position for each of the aaseq. index 1 is for aa 1 and so on
CR1_stop = []
CR2_start = []
CR2_stop = []
CR3_start = []
CR3_stop = []
CR4_start = []
CR4_stop = []
for position, line in enumerate(aaseq):
    CR1_start.append(aaseq[position].find(CR1))
    CR1_stop.append(aaseq[position].find(CR1) + len(CR1))
    CR2_start.append(aaseq[position].find(CR2))
    CR2_stop.append(aaseq[position].find(CR2) + len(CR2))
    CR3_start.append(aaseq[position].find(CR3))
    CR3_stop.append(aaseq[position].find(CR3) + len(CR3))
    CR4_start.append(aaseq[position].find(CR4))
    CR4_stop.append(aaseq[position].find(CR4) + len(CR4))

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
for position, line in enumerate(aaseq):
    vr1 = line[CR1_stop[position]:CR2_start[position]]
    vr2 = line[CR2_stop[position]:CR3_start[position]]
    vr3 = line[CR3_stop[position]:CR4_start[position]]
    if 9 >= len(vr1) >= 7:
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
    if 29 >= len(vr3) >= 17:
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

file = open("VR3_low.fasta", 'w')
for i in range(len(VR3)):
    num = str(i + 1)
    file.write(">" + num + "\n" + VR3[i] + "\n")
file.close()

ofile = open("VR2_low.fasta", 'w')
for i in range(len(VR2)):
    num = str(i + 1)
    ofile.write(">" + num + "\n" + VR2[i] + "\n")
ofile.close()

ifile = open("VR1_low.fasta", 'w')
for i in range(len(VR1)):
    num = str(i + 1)
    ifile.write(">" + num + "\n" + VR1[i] + "\n")
ifile.close()

# Tabulate the amount of amino acids per position
# Question - do they differ between all groups (LOW AND HIGH)

# Not of the same length; keep track of length of VR regions
# take to multiple sequence alignment and then weblogo
