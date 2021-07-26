# Structural modelling
# Goal - Extract amino acids from sequences in the aligned clean fasta file

# a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\short_high_20.fasta"
# b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\short_low_20.fasta"

#switch low and high
a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\combined_clean_aln_low.fasta"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\combined_clean_aln_high.fasta"

save_path = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data'


import numpy
import os.path
import matplotlib.pyplot as plt

name = ['LowNumberaa.fasta', 'HighNumberaa.fasta']
fname = [a, b]

for b in range(len(name)):
    high_nb_file = open(fname[b])  # default - r - open for reading
    high_nb = high_nb_file.read()
    high_nb_list = high_nb.splitlines()
    high_nb_file.close()
    print(high_nb_list)

    linea = []
    posa = []
    aaseq = []
    aaseq_line = numpy.arange(1, len(high_nb_list), 2)  # Note this might change
    for position, line in enumerate(high_nb_list):
        print(position, line)
        linea.append(line)
        posa.append(position)
        if position in aaseq_line:
            aaseq.append(line)

    print('line is :', linea)
    print('position is:', posa)
    print(aaseq_line)
    print('Amino Acid Sequence:', aaseq)
    print(len(high_nb_list)) #meant to be 42
    print(len(aaseq)) # meanr to be 21

    # Get the positions
    # positions needed - 32, 47, 48, 49, 58, 59, 60, 125, 126

    aa_32, aa_47, aa_48, aa_49, aa_58, aa_59, aa_60, aa_124, aa_125, aa_126 = [], [], [], [], [], [], [], [], [], []
    needaa = [aa_32, aa_47, aa_48, aa_49, aa_58, aa_59, aa_60, aa_124, aa_125, aa_126]
    posaa = [32, 47, 48, 49, 58, 59, 60, 124, 125, 126]
    nameaa = ['aa_32', 'aa_47', 'aa_48', 'aa_49', 'aa_58', 'aa_59', 'aa_60', 'aa_124', 'aa_125', 'aa_126']


    for z in range(len(needaa)):
        for i in range(len(aaseq)):
            pos = posaa[z]
            needaa[z].append(aaseq[i][pos])
        print(nameaa[z], ':', needaa[z])

    # Count the number of amino acids
    taa32, taa47, taa48, taa49, taa58, taa59, taa60, taa124, taa125, taa126 = [0]*21, [0]*21, [0]*21, [0]*21, [0]*21, [0]*21, [0]*21, [0]*21, [0]*21, [0]*21
    taa = [taa32, taa47, taa48, taa49, taa58, taa59, taa60, taa124, taa125, taa126]
    aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']

    for i in range(len(taa)): # Position like 32 etc
        for z in range(len(aaseq)): # Length of aa
            for a in range(len(aa)):
                if aa[a] == needaa[i][z]:
                    taa[i][a] = taa[i][a]+1
        print('number', nameaa[i], ':', taa[i])

    # Save number
    CompName = os.path.join(save_path, name[b])
    file = open(CompName, 'w')
    file.write("Amino Acids" +"\n")
    for a in range(len(aa)):
        file.write(aa[a] + ',')
    file.write("\n")
    for i in range(len(taa)): #  For each position
        ta = taa[i]
        file.write(">" + nameaa[i] + "\n")
        for z in range(len(ta)): #len(aaseq)
            file.write(str(ta[z]) + ',')
        file.write("\n")
    file.close()
