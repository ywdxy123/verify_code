import os
from crop_pic import get_bin_table
from PIL import Image
import sys
sys.path.append('D:\soft\libsvm-3.22\python')
from svmutil import *
import pandas as pd
import numpy as np

from sklearn.datasets import dump_svmlight_file
def get_score(path='.'):
	tt=[]
	for i in os.listdir('./dataset'):
		for j in os.listdir('./dataset/'+i):
			ptt=Image.open('./dataset/'+str(i)+'/'+j)
			table = get_bin_table()
			out = ptt.point(table, '1')
			T=[]
			width,height=out.size
			for iii in range(width):
				score=0
				for jjj in range(height):		
					if out.getpixel((iii,jjj))==0:
						score+=1
				T.append(score)
			for ii in range(height):
				score=0
				for jj in range(width):

					if out.getpixel((jj,ii))==0:
						score+=1
				T.append(score)
			T.append(i)
			tt.append(T)
	pd.DataFrame(tt).to_csv(path+'/'+'dataset.csv',index=False)

def csv2libsvm(df,path='.'):
	df.rename(columns={'34':'target'},inplace=True)
	X = df[np.setdiff1d(df.columns,['target'])]
	y = df.target
	dump_svmlight_file(X,y,path+'/'+'score.dat',zero_based=True,multilabel=False)
def train(dataset,path='.'):
	y, x = svm_read_problem(dataset)
	m =  svm_train(y[:1000], x[:1000], '-c 4' )
	model = svm_train(y, x)
	svm_save_model(path+'/'+'abc.txt', model)


if __name__ == '__main__':
	get_score()
	path='.'
	df=pd.read_csv(path+'/'+'dataset.csv')
	csv2libsvm(df)
	dataset='score.dat'
	train(dataset)
	print('ok')