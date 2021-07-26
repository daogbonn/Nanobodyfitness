# Read output files and extract needed values

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy
import re
c = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\structure\\ddg\\ddg_predictions_32.out"
d = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\structure\\ddg\\ddg_predictions_47.out"
e = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\structure\\ddg\\ddg_predictions_48.out"
f = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\structure\\ddg\\ddg_predictions_49.out"
g = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\structure\\ddg\\ddg_predictions_57.out"
h = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\structure\\ddg\\ddg_predictions_58.out"
savepath = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/Structure/Figures'


# Get the total values
tot32, tot47, tot48, tot49, tot57, tot58 = [], [], [], [], [], []
tot = [tot32, tot47, tot48, tot49, tot57, tot58]
names = [c, d, e, f, g, h]

for a in range(len(names)):
    fields = ["ddG: description" "total" "fa_atr" "fa_rep" "fa_sol" "fa_intra_rep" "fa_intra_sol_xover4" "lk_ball_wtd" "fa_elec" "pro_close" "hbond_sr_bb" "hbond_lr_bb" "hbond_bb_sc" "hbond_sc dslf_fa13" "omega fa_dun" "p_aa_pp" "yhh_planarity" "ref rama_prepro"]
    fname = names[a]
    lis = pd.read_csv(fname, skiprows=0, keep_default_na=bool, names=fields)
    lia = []
    for i in range(len(lis)):
        print(i)
        lists = lis.iloc[i]
        lits = pd.array(lists, dtype="string")
        lists1 = lits[0].split("   ", 21)
        lia.append(lists1)
    for i in range(len(lia) - 1):
        toa = tot[a]
        k = i + 1
        ddg_tot = lia[k][1]
        if " " in ddg_tot:
            ddg_tot = ddg_tot.replace(" ", "")
        elif "  " in ddg_tot:
            ddg_tot = ddg_tot.replace("  ", "")
        toa.append(float(ddg_tot))



aa = ['A', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
labels = ['aa 32', 'aa 47', 'aa 48', 'aa 49', 'aa 57', 'aa 58'] # Highlight the original value
aaorig = ['N', 'L', 'V', 'A', 'I', 'T']
aaono = [9, 8, 15, 0, 6, 14]
# Plot
for i in range(len(names)):
    n = aaono[i]
    plt.plot(aa, tot[i])
    plt.plot(aa[n], tot[i][n], 'rx', label='Original aa')
    plt.legend()
    plt.xlabel('Amino Acids')
    plt.ylabel('ddg (REU)') #units
    # plt.legend(labels)
    plt.title('Plot of change in amino acids versus ddg in %s' % labels[i])
    file_name = ('ddg_%s.png' % labels[i])
    plt.savefig(os.path.join(savepath, file_name))
    plt.show()

# idea - plot individually and use the original position as a point of reference in compating others
# Position 47 49 important due to the high difference in energy with change in aa
