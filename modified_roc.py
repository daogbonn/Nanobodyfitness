
# Goal - to Make the models after training
import pickle
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc, plot_roc_curve
import sklearn.metrics as metrics
import os.path
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import label_binarize
from sklearn.metrics import silhouette_score
from split_data import split_dataframes_train_test
from sklearn.metrics import confusion_matrix
from model_functions import clusterpred
import csv
import pandas as pd
from split_data import split_dataframes_train_test
from split_data import split_true_classes
import scikitplot as skplt

def plot_roc_curve(y_true, y_probas, title='ROC Curves',
                   curves=('micro', 'macro', 'each_class'),
                   ax=None, figsize=None, cmap='nipy_spectral',
                   title_fontsize="large", text_fontsize="medium"):
    """Generates the ROC curves from labels and predicted scores/probabilities
    Args:
        y_true (array-like, shape (n_samples)):
            Ground truth (correct) target values.
        y_probas (array-like, shape (n_samples, n_classes)):
            Prediction probabilities for each class returned by a classifier.
        title (string, optional): Title of the generated plot. Defaults to
            "ROC Curves".
        curves (array-like): A listing of which curves should be plotted on the
            resulting plot. Defaults to `("micro", "macro", "each_class")`
            i.e. "micro" for micro-averaged curve, "macro" for macro-averaged
            curve
        ax (:class:`matplotlib.axes.Axes`, optional): The axes upon which to
            plot the curve. If None, the plot is drawn on a new set of axes.
        figsize (2-tuple, optional): Tuple denoting figure size of the plot
            e.g. (6, 6). Defaults to ``None``.
        cmap (string or :class:`matplotlib.colors.Colormap` instance, optional):
            Colormap used for plotting the projection. View Matplotlib Colormap
            documentation for available options.
            https://matplotlib.org/users/colormaps.html
        title_fontsize (string or int, optional): Matplotlib-style fontsizes.
            Use e.g. "small", "medium", "large" or integer-values. Defaults to
            "large".
        text_fontsize (string or int, optional): Matplotlib-style fontsizes.
            Use e.g. "small", "medium", "large" or integer-values. Defaults to
            "medium".
    Returns:
        ax (:class:`matplotlib.axes.Axes`): The axes on which the plot was
            drawn.
    Example:
        >>> import scikitplot as skplt
        >>> nb = GaussianNB()
        >>> nb = nb.fit(X_train, y_train)
        >>> y_probas = nb.predict_proba(X_test)
        >>> skplt.metrics.plot_roc_curve(y_test, y_probas)
        <matplotlib.axes._subplots.AxesSubplot object at 0x7fe967d64490>
        >>> plt.show()
        .. image:: _static/examples/plot_roc_curve.png
           :align: center
           :alt: ROC Curves
    """
    y_true = np.array(y_true)
    y_probas = np.array(y_probas)
    if 'micro' not in curves and 'macro' not in curves and \
            'each_class' not in curves:
        raise ValueError('Invalid argument for curves as it '
                         'only takes "micro", "macro", or "each_class"')
    classes = np.unique(y_true)
    probas = y_probas
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(len(classes)):
        fpr[i], tpr[i], _ = roc_curve(y_true, probas[:, i],
                                      pos_label=classes[i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    # Compute micro-average ROC curve and ROC area
    micro_key = 'micro'
    i = 0
    while micro_key in fpr:
        i += 1
        micro_key += str(i)
    y_true = label_binarize(y_true, classes=classes)
    if len(classes) == 2:
        y_true = np.hstack((1 - y_true, y_true))
    fpr[micro_key], tpr[micro_key], _ = roc_curve(y_true.ravel(),
                                                  probas.ravel())
    roc_auc[micro_key] = auc(fpr[micro_key], tpr[micro_key])
    # Compute macro-average ROC curve and ROC area
    # First aggregate all false positive rates
    all_fpr = np.unique(np.concatenate([fpr[x] for x in range(len(classes))]))
    # Then interpolate all ROC curves at this points
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(len(classes)):
        mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])
    # Finally average it and compute AUC
    mean_tpr /= len(classes)
    macro_key = 'macro'
    i = 0
    while macro_key in fpr:
        i += 1
        macro_key += str(i)
    fpr[macro_key] = all_fpr
    tpr[macro_key] = mean_tpr
    roc_auc[macro_key] = auc(fpr[macro_key], tpr[macro_key])
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.set_title(title, fontsize=title_fontsize)
    if 'each_class' in curves:
        for i in range(len(classes)):
            color = plt.cm.get_cmap(cmap)(float(i) / len(classes))
            ax.plot(fpr[i], tpr[i], lw=2, color=color,
                    label='ROC curve of class {0} (area = {1:0.2f})'
                    ''.format(classes[i], roc_auc[i]))
    if 'micro' in curves:
        ax.plot(fpr[micro_key], tpr[micro_key],
                label='micro-average ROC curve '
                      '(area = {0:0.2f})'.format(roc_auc[micro_key]),
                color='deeppink', linestyle=':', linewidth=4)
    if 'macro' in curves:
        ax.plot(fpr[macro_key], tpr[macro_key],
                label='macro-average ROC curve '
                      '(area = {0:0.2f})'.format(roc_auc[macro_key]),
                color='navy', linestyle=':', linewidth=4)
    ax.plot([0, 1], [0, 1], 'k--', lw=2)
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('False Positive Rate', fontsize=text_fontsize)
    ax.set_ylabel('True Positive Rate', fontsize=text_fontsize)
    ax.tick_params(labelsize=text_fontsize)
    ax.legend(loc='lower right', fontsize=text_fontsize)
    return ax


a = "C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test.csv"
b = 'C:/Users/ITSloaner/PycharmProjects/Nanobodyfitness/data/ROC_Curves'


df = pd.read_csv(r'C:\\Users\\ITSloaner\\PycharmProjects\\Nanobodyfitness\\data\\test.csv')

# Testing Class
clas = df.iloc[1:, -1]
print(clas.shape)
# Test data
test = df.iloc[1:, 1:-1]
print(test.shape)
test1 = np.asarray(test)

modelname = ['kmeans', 'Decision Tree','Decision Tree 20', 'Neural Network', 'Neural Network 100 Layers', 'Neural Network 200 Layers', 'Logistic Regression', 'Iterated Logistic Regression']
modelfile = ["kmeans_model_20210714_08.22.15.p", "decision_tree_model_depthNone_leaf_min1_20210714_08.18.53.p", "decision_tree_model_depthNone_leaf_min20_20210727_09.38.15.p","neural_network_classifier_20210714_10.52.p", "neural_network_classifier_layers_100_25_20210714_13.04.p","neural_network_classifier_layers_200_50_10_20210714_22.42.p", "logsitic_regression_classifier_20210718_17.29.p", "logsitic_regression_classifier_iter1000_20210718_17.57.p"]

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
        plot_roc_curve(clas, prob)
        plt.title('Receiving Operating Curve for %s' % modelname[i])
        plt.show()

