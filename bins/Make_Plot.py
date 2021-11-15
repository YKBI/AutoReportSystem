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
    def box_plot(self,fname,fPath):
        plt.figure(figsize=(15,15))
        plt.boxplot(self.df[self.cn].tolist())
        plt.xticks([]),plt.yticks(fontsize=20)
        plt.ylabel("Amount of %s"%self.cn,fontsize=30),plt.xlabel("%s"%self.cn,fontsize=30)
        plt.tight_layout()
        plt.savefig("%s/%s.boxplot.jpg"%(fPath,fname))
    def dist_plot(self,fname,fPath):
        plt.figure(figsize=(15,15))
        sns.distplot(self.df[self.cn].tolist(),bins=30)
        plt.ylabel("Probability Density of %s"%self.cn,fontsize=30),plt.xlabel("Amount of %s"%self.cn,fontsize=30)
        plt.xticks(fontsize=15),plt.yticks(fontsize=15)
        plt.tight_layout()
        plt.savefig("%s/%s.distplot.jpg"%(fPath,fname))
    def hist_plot(self,fname,fPath):
        plt.figure(figsize=(15,15))
        plt.hist(self.df[self.cn].tolist(),bins=30)
        plt.ylabel("Distribution of %s"%self.cn,fontsize=30),plt.xlabel("Amount of %s"%self.cn,fontsize=30)
        plt.xticks(fontsize=15),plt.yticks(fontsize=15)
        plt.tight_layout()
        plt.savefig("%s/%s.histogram.jpg"%(fPath,fname))
    def line_plot(self,fname,fPath,xt):
        tlist = self.df[self.cn].tolist()
        plt.figure(figsize=(30,15))
        sns.lineplot(data=self.df[self.cn].tolist())
        #plt.plot(tlist)
        plt.ylabel("%s"%self.cn,fontsize=30),plt.xlabel("Samples",fontsize=30)
        plt.yticks(fontsize=15)
        if xt == "n" or xt == "no":
            plt.xticks([])
        elif xt == "y" or xt == "yes":
            plt.xticks(fontsize=15)
        else:
            print("Please add condition xticks displaying")
            sys.exit(1)
        plt.tight_layout()
        plt.savefig("%s/%s.line.jpg"%(fPath,fname))
class make_plots_multi:
    def __init__(self,a,cname):
        self.cn = cname
        self.df = pd.DataFrame([a],columns=self.cn)
    def scatter_plot(self,cn1,cn2,fname,fPath):

        df = self.df
        print(type(df[cn1][0]))
        plt.figure(figsize=(15,15))
        plt.scatter(df[cn1][0],df[cn2][0])
        plt.show()


if __name__ == "__main__":
    np.random.seed(1)
    aa = np.random.normal(0,2.0,1000)
    np.random.seed(100)
    bb = np.random.normal(0,2.0,1000)
    np.random.seed(1000)
    cc = np.random.normal(0,2.0,1000)
    #print(pd.DataFrame([[aa,bb]]))
    pp = make_plots_multi([aa,bb,cc],["test1","test2","test3"])
    pp.scatter_plot("test1","test3","test","../out_image")
    #pp = make_plots_1D(aa,"test")
    #pp.box_plot("test","../out_image")
    #pp.dist_plot("test","../out_image")
    #pp.hist_plot("test","../out_image")
    #pp.line_plot("test","../out_image","n")