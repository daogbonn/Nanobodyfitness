# Goal - create the score rmsd plot

import pandas as pd
import matplotlib.pyplot as plt
import os

a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\structure\\combined.sc"
b = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\structure\\combined8.sc"
savepath = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/Structure/Figures'

fname = [a,b]
name = ['Nb06: High Fitness','Nb08: Low Fitness']
sname = ['Nb06','Nb08']


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
    for i in range(len(actual)):
        line = actual[i]
        scores.append(float(line[0]))
        rmsd.append(float(line[25]))

    print(len(scores))
    print(len(rmsd))

    # Plot
    plt.plot(rmsd, scores, 'k.')
    plt.xlabel('rmsd')
    plt.ylabel('Score')
    plt.title('Score versus rmsd for %s'% name[z])
    file_name = ('Scoregraph_%s.png' % sname[z])
    plt.savefig(os.path.join(savepath, file_name))
    plt.show()




