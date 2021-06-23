# Goal - Make a position Weight Matris and plot it using seaborn
# Matrix - x-axis(amino acids), y-axis(position on aa seq)
import numpy
import seaborn
import matplotlib.pyplot as plt

# Import Data
b = 'VR3_Low_clustal.fasta'
nb_file = open(b)  # default - r - open for reading
nb = nb_file.read()
nb_list = nb.splitlines()
nb_file.close()
len_xter = len(nb_list[1])
print(nb_list)

#Cut out the aaseq
linea = []
posa = []
aaseq = []
aaseq_line = numpy.arange(1, len(nb_list), 2)  # Note this might change
for position, line in enumerate(nb_list):
    print(position, line)
    linea.append(line)
    # all the lines of the fasta file
    posa.append(position)
    # the position of the corresponding fasta lines
    if position in aaseq_line:
        aaseq.append(line)
        # To extract the aa lines
a = aaseq
print('aaseq:',a)

# Make the matrix
aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']
s = (len(aa), len(a[1]))
mat = numpy.zeros(s)  # matrix of 20 rows and length in column
# rows: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, W, Y, Z
pos = numpy.arange(1, len(a[1])+1, 1)

for position, line in enumerate(a):
    for j in range(len(a[1])):
        for i in range(len(aa)):
            aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']
            j=j
            if line[j] == aa[i]:
                num = mat[i, j] + 1
                mat[i, j] = num


print(mat)

N = len(a)  # Number of sequences
I = len(a[1])  # Length of sequences

ppm = mat / N
print(ppm)

b = 0.05 #for aa it is 1/20 = 0.05
pwm = numpy.log2((ppm/b))
print('pwm:', pwm)


# Plot as a heat wave plot
# weimat = seaborn.load_dataset(pwm)
# pwm_df = weimat.pivot('DNA Nucleotide', 'Position', 'Position Probability')
seaborn.heatmap(pwm, yticklabels=aa, xticklabels=pos, vmin=0, vmax=5)
plt.title('Heat Map for Amino Acids in CDR3 for the Low Nanobodies (10 seq)')
plt.show()

#Incorporate a pseudo count value