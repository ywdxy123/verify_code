import os
from crop_pic import get_bin_table
from PIL import Image
import sys
sys.path.append('D:\soft\libsvm-3.22\python')
from svmutil import *
import pandas as pd
import numpy as np

from sklearn.datasets import dump_svmlight_file
table = get_bin_table()
vt=os.listdir('./test')
model = svm_load_model('abc.txt')
def get_predict():
	for i in vt:
		os.mkdir('./test/test/%s'%str(i).split('.')[0])
		pic=Image.open('./test/'+i)
		imgry = pic.convert('L')  # 转化为灰度图
		out = imgry.point(table, '1')
		width,height=out.size
		cut=0
		T=[]
		l=4
		start=0
		for y in range(height):
			for x in range(width)[start:]:
				if  out.getpixel((x,y))==0:
					if cut<x:
						if x-cut>l:
							T.append(x)
							start=x
						cut=x
		start=0
		tt=[]
		for ii in T[:]:
			tt.append(out.crop((start,0,ii,20)))
			start=ii-2
		tt.append(out.crop((start,0,width,20)))
		for img in tt:
			out=img.resize((14,20))
			width,height=out.size
			T_score=[]
			for wid in range(width):
				score=0
				for hei in range(height):		
					if out.getpixel((wid,hei))==0:
						score+=1
				T_score.append(score)
			for heii in range(height):
				score=0
				for widd in range(width):

					if out.getpixel((widd,heii))==0:
						score+=1
				T_score.append(score)
			
			df=pd.DataFrame([T_score],columns=[str(i) for i in range(34)]).join(pd.DataFrame([0],columns=['target']))
			X = df[np.setdiff1d(df.columns,['target'])]
			y = df.target
			dump_svmlight_file(X,y,'smvlight.dat',zero_based=True,multilabel=False)
			y, x = svm_read_problem('smvlight.dat')
			p_label, p_acc, p_val = svm_predict(y,x, model)
			
			img.save('./test/test/%s/%s.png'%(str(i).split('.')[0],str(p_label[0]).split('.')[0]))