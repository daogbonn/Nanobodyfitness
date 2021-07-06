#Goal - Make script to transform amino acids to variables to use for learning


import numpy
import os.path
import matplotlib.pyplot as plt

# Import Sequences
a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\Short_20200730_Low_Fitness.fasta"
short_nb_file = open(a)  # default - r - open for reading
short_nb = short_nb_file.read()
short_nb_list = short_nb.splitlines()
short_nb_file.close()

aaseq = []
aaseq_line = numpy.arange(1, len(short_nb_list), 3)  # Note this might change
for position, line in enumerate(short_nb_list):
    if position in aaseq_line:
        aaseq.append(line)


# First - Matrix
# say seq is all the amino acid sequences (not just one)

aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'Y', '-']
s = (len(aaseq), len(aaseq[0])) # the size of the matrix
mat = [[] for a in range(len(aaseq))]
print(mat)

for i in range(len(aaseq)): # For each line of seq
    for j in range(len(aaseq[i])): #Each character in the sequence
        for k in range(len(aa)): # For each amino acid
            if aaseq[i][j] == aa[k]:
                line = numpy.zeros(len(aa))
                line[k] = 1
                mat[i].append(line)

print(len(mat))
print(len(aaseq))
print(len(mat[0]))
print(len(aaseq[0]))
print(mat[0][1])


# Split data into a test or training set.
# kmeans.fit(X)
# Arguments: X(input), hyperparameter_example
# trained_model = kmeans.fit(X)
# trained_model.test(testdatamatrix)  Output - Vector of predicted value
# predicted values - array of 0s and 1s based on what the input is.
# Supervised - give input and correct output
# Unsupervised - computer never knows w