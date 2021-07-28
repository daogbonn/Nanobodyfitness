# Goal - to Make the models after training
import pickle
import numpy
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc, plot_roc_curve
import sklearn.metrics as metrics
import os.path
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from split_data import split_dataframes_train_test
from sklearn.metrics import confusion_matrix
from model_functions import clusterpred
import csv
import pandas as pd
from split_data import split_dataframes_train_test
from split_data import split_true_classes
import scikitplot as skplt



a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test.csv"
b = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/ROC_Curves'


df = pd.read_csv(r'C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test.csv')

# Testing Class
clas = df.iloc[1:, -1]
print(clas.shape)
# Test data
test = df.iloc[1:, 1:-1]
print(test.shape)
test1 = numpy.asarray(test)


# modelname = ['kmeans', 'Decision Tree','Decision Tree 20', 'Neural Network', 'Neural Network 100 Layers', 'Neural Network 200 Layers', 'Logistic Regression', 'Iterated Logistic Regression']
# modelfile = ["kmeans_model_20210714_08.22.15.p", "decision_tree_model_depthNone_leaf_min1_20210714_08.18.53.p", "decision_tree_model_depthNone_leaf_min20_20210727_09.38.15.p","neural_network_classifier_20210714_10.52.p", "neural_network_classifier_layers_100_25_20210714_13.04.p","neural_network_classifier_layers_200_50_10_20210714_22.42.p", "logsitic_regression_classifier_20210718_17.29.p", "logsitic_regression_classifier_iter1000_20210718_17.57.p"]
modelname = ['kmeans', 'Decision Tree', 'Neural Network', 'Logistic Regression']
modelfile = ["kmeans_model_20210714_08.22.15.p", "decision_tree_model_depthNone_leaf_min1_20210714_08.18.53.p","neural_network_classifier_20210714_10.52.p",  "logsitic_regression_classifier_20210718_17.29.p"]

suc = [0]*len(modelname)
probtot = []
for i in range(len(modelname)):
    model = pickle.load(open(modelfile[i], 'rb'))
    sol = model.predict(test1)
    conf = confusion_matrix(clas, sol)
    sucno = (conf[0][0] + conf[1][1])/conf.sum()
    suc[i] = sucno*100
    print(modelname[i], 'Sucess Criteria:', sucno*100, '%')
    if modelname[i] != 'kmeans':
        prob = model.predict_proba(test1)
        probtot.append(prob)
        #Plot
        skplt.metrics.plot_roc_curve(clas, prob, curves=('each_class'), figsize=(6,6))
        plt.title('Receiving Operating Curve for %s' % modelname[i])
        save_path = b
        file_name = ('ROC curve for %s' % modelname[i])
        plt.savefig(os.path.join(save_path, file_name))
        plt.show()

print(probtot)
skplt.metrics.plot_roc_curve(clas, probtot[0])
skplt.metrics.plot_roc_curve(clas, probtot[2])
plt.title('Total ROC curve)')
plt.show()
# Plot Success Criteria
#mdlname = ['kmeans', 'DT','DT20', 'NT', 'NT150', 'NT250', 'LR', 'iLR']
mdlname = ['kmeans', 'Decision \n Tree', 'Neural \n Network',  'Logistic \n Regression']
sc = [80]*len(modelname)
rg = [50]*len(modelname)
plt.plot(mdlname, suc, 'ro')
plt.plot(mdlname, sc, 'b', label='Success Criteria')
plt.plot(mdlname, rg, 'k', label='Random Guess')
plt.legend()
plt.xlabel('Models Used')
plt.ylabel('Accuracy (%)')
plt.title('Plot of models versus Accuracy')
save_path = b
file_name = ('Success Criteria Graph')
plt.savefig(os.path.join(save_path, file_name))
plt.show()

