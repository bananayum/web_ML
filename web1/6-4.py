# -*- coding:utf-8 -*-

import re
import matplotlib.pyplot as plt
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score
import os
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pydotplus


def load_one_flle(filename):
    x=[]
    with open(filename) as f:
        line=f.readline()
        line=line.strip('\n')
    return line

def load_adfa_training_files(rootdir):
    x=[]
    y=[]
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            x.append(load_one_flle(path))
            y.append(0)
    return x,y

def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile

def load_adfa_hydra_ftp_files(rootdir):
    x=[]
    y=[]
    allfile=dirlist(rootdir,[])
    for file in allfile:
        if re.match(r"/Users/banana/Desktop/1book-master/data/ADFA-LD/Attack_Data_Master/Hydra_FTP_\d+/UAD-Hydra-FTP*",file):
            x.append(load_one_flle(file))
            y.append(1)
    return x,y



if __name__ == '__main__':

    x1,y1=load_adfa_training_files("/Users/banana/Desktop/1book-master/data/ADFA-LD/Training_Data_Master/")
    x2,y2=load_adfa_hydra_ftp_files("/Users/banana/Desktop/1book-master/data/ADFA-LD/Attack_Data_Master/")

    x=x1+x2
    y=y1+y2
    #print x
    vectorizer = CountVectorizer(min_df=1)
    x=vectorizer.fit_transform(x)
    x=x.toarray()
    #print y
    clf1 = tree.DecisionTreeClassifier()
    score=cross_val_score(clf1, x, y, n_jobs=-1, cv=10)
    print(np.mean(score))
    clf2 = RandomForestClassifier(n_estimators=10, max_depth=None,min_samples_split=2, random_state=0)
    score=cross_val_score(clf2, x, y, n_jobs=-1, cv=10)
    print(np.mean(score))
    # clf1 = clf1.fit(x, y)
    # dot_data = tree.export_graphviz(clf1, out_file=None)
    # graph = pydotplus.graph_from_dot_data(dot_data)
    # graph.write_pdf("/Users/banana/Desktop/ftp.pdf")




