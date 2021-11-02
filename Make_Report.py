import pandas as pd
import numpy as np
import scipy.stats as ss

import matplotlib.pyplot as plt
import seaborn as sns

import os,sys,glob
from tqdm import tqdm

class make_plots_1D:
    def __init__(self,a,cname):
        self.cn = cname
        self.df = pd.DataFrame(a)
        self.df.columns = [self.cn]
        plt.figure(figsize=(10,10))
    def box_plot(self,fname,fPath):
        plt.boxplot(self.df[self.cn].tolist())
        plt.xticks([]),plt.yticks(fontsize=20)
        plt.ylabel("Amount of %s"%self.cn,fontsize=30),plt.xlabel("%s"%self.cn,fontsize=30)
        plt.savefig("%s/%s.boxplot.png"%(fPath,fname))

if __name__ == "__main__":
    np.random.seed(1)
    aa = np.random.normal(0,2.0,1000)
    pp = make_plots_1D(aa,"test")
    pp.box_plot("test","./")