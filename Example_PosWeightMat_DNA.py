# Goal - Make a position Weight Matris and plot it using seaborn
# Matrix - x-axis(amino acids), y-axis(position on aa seq)
import numpy
import seaborn
import matplotlib.pyplot as plt

a = ['GAGGTAAAC', 'TCCGTAAGT', 'CAGGTTGGA', 'ACAGTCAGT', 'TAGGTCATT', 'TAGGTACTG', 'ATGGTAACT', 'CAGGTATAC',
     'TGTGTGAGT', 'AAGGTAAGT']
len_xter = len(a[1])

# Make the matrix
s = (4, len(a[1]))
mat = numpy.zeros(s)  # matrix of 20 rows and length in column
# rows: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, W, Y, Z
aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'Y', 'Z']
pos = numpy.arange(1, len(a), 1)
DNA = ['A', 'C', 'G', 'T']

# for position, line in enumerate(a):
#     for i in range(len(a[1])):
#         if line[i] == 'A':
#             num = mat[0, i] + 1
#             mat[0, i] = num
#         elif line[i] == 'C':
#             num = mat[1, i] + 1
#             mat[1, i] = num
#         elif line[i] == 'G':
#             num = mat[2, i] + 1
#             mat[2, i] = num
#         elif line[i] == 'T':
#             num = mat[3, i] + 1
#             mat[3, i] = num

for position, line in enumerate(a):
    for j in range(len(a[1])):
        for i in range(len(DNA)):
            if line[j] == DNA[i]:
                num = mat[i, j] +1
                mat[i, j] = num

print(mat)

N = len(a)  # Number of sequences
I = len(a[1])  # Length of sequences

ppm = mat / N
print(ppm)

b = 0.25 # for nucleotides, for aa it is 1/20 = 0.05
pwm = numpy.log2((ppm/b))
print('pwm:', pwm)


# Plot as a heat wave plot
# weimat = seaborn.load_dataset(pwm)
# pwm_df = weimat.pivot('DNA Nucleotide', 'Position', 'Position Probability')
seaborn.heatmap(pwm, yticklabels=DNA, xticklabels=pos)
plt.show()