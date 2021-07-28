# Goal - create the score rmsd plot
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import os

a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\structure\\combined.sc"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\structure\\combined8.sc"
savepath = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/Structure/Figures'

fname = [a,b]
name = ['Nb06: High Fitness','Nb08: Low Fitness']
sname = ['Nb06','Nb08']

scores6, rmsd6, scores8, rmsd8 = [], [], [], []

for z in range(len(fname)):
    nam = fname[z]
    lis = pd.read_csv(nam, skiprows=0, keep_default_na=bool)
    #print(lis)

    header = []
    actual = []
    for i in range(len(lis)):
        unwan = 'SCORE:     score     fa_atr     fa_rep     fa_sol    fa_intra_rep    fa_intra_sol_xover4    lk_ball_wtd    fa_elec    pro_close    hbond_sr_bb    hbond_lr_bb    hbond_bb_sc    hbond_sc    dslf_fa13      omega     fa_dun    p_aa_pp    yhh_planarity        ref    rama_prepro    Filter_Stage2_aBefore    Filter_Stage2_bQuarter    Filter_Stage2_cHalf    Filter_Stage2_dEnd    co        rms     maxsub    clashes_total    clashes_bb       time description'
        ln = len(unwan)
        line = lis.iloc[i]
        lits = pd.array(line, dtype="string")[0]
        # print(lits)
        if unwan in lits:
            header.append(lits)
        else:
            un = 'SCORE:  '
            linn = lits[len(un):]
            lists1 = linn.split()
            actual.append(lists1)
            #print(lists1)

    #print(header)
    print(len(header))
    #print(actual)
    print(len(actual))
    print(len(actual[1]))

    # Get the Scores and the rmsd
    labels = 'score     fa_atr     fa_rep     fa_sol    fa_intra_rep    fa_intra_sol_xover4    lk_ball_wtd    fa_elec    pro_close    hbond_sr_bb    hbond_lr_bb    hbond_bb_sc    hbond_sc    dslf_fa13      omega     fa_dun    p_aa_pp    yhh_planarity        ref    rama_prepro    Filter_Stage2_aBefore    Filter_Stage2_bQuarter    Filter_Stage2_cHalf    Filter_Stage2_dEnd    co        rms     maxsub    clashes_total    clashes_bb       time description'.split()
    print(labels)

    scores = []
    rmsd = []
    scormsd = [[],[]]
    for i in range(len(actual)):
        line = actual[i]
        scormsd[0].append(float(line[0]))
        scormsd[1].append(float(line[25]))
        scores.append(float(line[0]))
        rmsd.append(float(line[25]))

    print('scores:',len(scores))


    def sort_np_array(x, column=None, flip=False):
        x = x[numpy.argsort(x[:, column])]
        if flip:
            x = numpy.flip(x, axis=0)
        return x

    # Sort scormsd
    sr = sort_np_array(numpy.array(scormsd).transpose(), column=0, flip=False)

    # print the first 5000
    sr2 = sr[0:5000].transpose()
    if z == 0:
        scores6 = sr2[0]
        rmsd6 = sr2[1]
    elif z == 1:
        scores8 = sr2[0]
        rmsd8 = sr2[1]

# Plot
# plt.plot(rmsd, scores, 'k.')
plt.plot(rmsd6, scores6, 'k.', label='High Fitness')
plt.plot(rmsd8, scores8, 'r.', label='Low Fitness')
plt.legend()
plt.xlabel('rmsd')
plt.ylabel('Score')
plt.title('Score versus rmsd for Nb06 and Nb08')
file_name = ('Scoregraph.png')
plt.savefig(os.path.join(savepath, file_name))
plt.show()




