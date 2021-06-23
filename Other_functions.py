import numpy

def substrFinder(string1, string2):
    answer = ""
    anslist=[]
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                #if (len(match) > len(answer)):
                answer = match
                if answer != '' and len(answer) > 1:
                    anslist.append(answer)
                match = ""

        if match != '':
            anslist.append(match)
        # break
    return anslist

print(substrFinder("AHAMMAD", "AHAMAD"))

short_nb_file = open("Short_20200730_High_Fitness.fasta") #default - r - open for reading
short_nb = short_nb_file.read()
#print(short_nb)

# to split into lines
short_nb_list = short_nb.splitlines()
# use splitlines to split the line
short_nb_file.close()
print(short_nb_list)

linea = []
posa = []
aaseq = []
aaseq_line = numpy.arange(1, len(short_nb_list), 3) # Note this might change
for position, line in enumerate(short_nb_list):
    print(position, line)
    linea.append(line)
    # all the lines of the fasta file
    posa.append(position)
    # the position of the corresponding fasta lines
    if position in aaseq_line:
        aaseq.append(line)
        # To extract the aa lines

