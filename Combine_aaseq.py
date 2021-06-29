# This is to combine the amino acid sequences that meet the criteria so as to combine them into one file.

# EXTRACTION
#a = 'C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Short_20200730_High_Fitness.fasta'
a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\20200730_MiSeqv3_Low_fitness.fasta"
save_path = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/Long_Low_VR'

import numpy
import os.path
import matplotlib.pyplot

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
for position, line in enumerate(aaseq):
    if CR1 and CR2 and CR3 and CR4 in line:
        print('Constant Regions Confirmed in aa: ', position + 1)
        aaseq_ana.append(line)
    else:
        print('Constant Regions not confirmed in aa: ', position + 1)
        aaseq_nana.append(line)

print('Amino Acid Seq to Use:', aaseq_ana)
print('Amino Acid Seq not confirmed:', aaseq_nana)

# List: VR_list[i] = [“>low_fitness_1\n”, “GFGFGF\n”]

name = 'aaseq_Long_Low.fasta'
CompName = os.path.join(save_path, name)
file = open(CompName, 'w')
for k in range(len(aaseq_ana)):
    num = str(k + 1)
    file.write(">Low_fitness" + num + "\n" + aaseq_ana[k] + "\n")
file.close()