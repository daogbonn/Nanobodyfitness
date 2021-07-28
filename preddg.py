# Goal - Test to read out the occurence of aa

a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\LowNumberaa.fasta"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\HighNumberaa.fasta"
savepath = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/Structure/Figures/Occurence'


import numpy
import os
import matplotlib.pyplot as plt

def percentnumlohi(a, b):
    # Read out the fasta file
    fname = [a, b]
    taanumlo, taanumhi = [], []
    taan = [taanumlo, taanumhi]

    for g in range(len(taan)):
        high_nb_file = open(fname[g])  # default - r - open for reading
        high_nb = high_nb_file.read()
        high_nb_list = high_nb.splitlines()
        high_nb_file.close()
        #print(high_nb_list)

        aaseq = []
        taa = []
        num_line = numpy.arange(3, len(high_nb_list), 2)  # Note this might change
        for position, line in enumerate(high_nb_list):
            line = line[:-1]
            # print(position, line)
            if position in num_line:
                aaseq.append(line)
                sp = line.split(",")
                taa.append(sp)
                # print(sp)
                # print(len(sp))

        #print(taa)
        # Convert to integers
        taanum = taan[g]
        for a in range(len(taa)): # Positions in aa like 32, 45
            numa = a
            #print(taanum)
            cent = []
            for b in range(len(taa[a])):
                st = int(taa[a][b])
                cent.append(st)
            #print(cent)
            taanum.append(cent)

        # print(taa)
        # print('taanum:', taanum)
        # print(len(taanum))

    print(taanumlo)
    print(len(taanumlo))
    aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']
    posaa = [32, 47, 48, 49, 57, 58, 59, 60, 124, 125, 126]

    # Pernumlo, pernumhi
    sumnumlo = [0]*len(taanumlo)
    sumnumhi = [0]*len(taanumlo)
    for i in range(len(taanumlo)):
        talo = taanumlo[i]
        sumnumlo[i] = sum(talo)
        tahi = taanumhi[i]
        sumnumhi[i] = sum(tahi)

    # Get percent
    pernumlo = []
    pernumhi = []
    for i in range(len(taanumlo)):
        arrlo, arrhi = [], []
        for z in range(len(taanumlo[0])):
            arrlo.append(taanumlo[i][z]*100/sumnumlo[0])
            arrhi.append(taanumhi[i][z]*100/sumnumhi[0])
        pernumlo.append(arrlo)
        pernumhi.append(arrhi)

    print(pernumlo)
    print(pernumhi)
    print(len(pernumhi))
    return pernumlo, pernumhi

aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']

pernumlo, pernumhi = percentnumlohi(a, b)

print(pernumlo, pernumhi)
posaa = [32, 47, 48, 49, 57, 58, 59, 60, 124, 125, 126]
# Plot - 32
for i in range(len(pernumlo)): # amino acid examples eg 32, 41
    # Plot of both side by side
    x = numpy.arange(len(aa))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, pernumhi[i], width, label='High Fitness')
    rects2 = ax.bar(x + width / 2, pernumlo[i], width, label='Low Fitness')
    ax.set_ylabel('Percent (%)')
    ax.set_xlabel('Amino Acids')
    ax.set_xticks(x)
    ax.set_xticklabels(aa)
    plt.xticks(rotation=45)
    plt.title('Histogram of Occurences for aa%d' % posaa[i])
    ax.legend()
    file_name = ('occurence_aa%d.png' % posaa[i])
    plt.savefig(os.path.join(savepath, file_name))
    plt.show()
