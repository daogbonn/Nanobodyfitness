#!/usr/bin/env python3

import argparse
import pandas as pd
from sklearn.model_selection import train_test_split


def split_dataframes_train_test(class0_dataframe_csv, class1_dataframe_csv, test_size, drop_class=True,
                                random_state=1):
    """split data for each cass independently to keep the proportions of classes equal between train and test"""
    class0 = pd.read_csv(class0_dataframe_csv, index_col=0)
    class0.loc[:, 'class'] = 0
    class1 = pd.read_csv(class1_dataframe_csv, index_col=0)
    class1.loc[:, 'class'] = 1

    if test_size > 0:
        train_class0, test_class0 = train_test_split(class0, test_size=test_size, random_state=random_state)
        train_class1, test_class1 = train_test_split(class1, test_size=test_size, random_state=random_state)
        train = pd.concat([train_class0, train_class1])
        test = pd.concat([test_class0, test_class1])
        test_true_class = test.loc[:, 'class']
        if drop_class:
            test.drop(columns=['class'], inplace=True)
    else:
        train = pd.concat([class0, class1])
        test = pd.DataFrame()
        test_true_class = pd.DataFrame()
    train_true_class = train.loc[:, 'class']
    if drop_class:
        train.drop(columns=['class'], inplace=True)

    # make sure counts equal fasta files
    print('class0 count: {0}'.format(class0.shape))
    print('class1 count: {0}'.format(class1.shape))
    print('training set size: {0}'.format(train.shape))
    print('test set size: {0}'.format(test.shape))

    return train, train_true_class, test, test_true_class


def split_true_classes(onehot_csv_with_class,):
    """return two pandas dataframes - remove true class labels from input and return both"""
    df = pd.read_csv(onehot_csv_with_class, index_col=0)
    df_true_class = df.loc[:, 'class']
    df.drop(columns=['class'], inplace=True)

    return df, df_true_class


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""script containing functions for splitting one-hot encoded data
    into test, training, and cross validation sets""")
    required = parser.add_argument_group('required')
    required.add_argument('-d0', '--dataframe_csv0', required=True,
                          help='input dataframe csv from encode_one_hot_cdrs_from_fasta.')
    required.add_argument('-d1', '--dataframe_csv1', required=True,
                          help='input dataframe csv from encode_one_hot_cdrs_from_fasta.')
    parser.add_argument('-t', '--test_size', type=float, default=0.2)
    args = parser.parse_args()

    df_train, df_train_class, df_test, df_test_class = split_dataframes_train_test(
        args.dataframe_csv0, args.dataframe_csv1, args.test_size, drop_class=False)

    df_train.to_csv('train.csv')
    df_test.to_csv('test.csv')

