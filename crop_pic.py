import os
from PIL import Image
import sys
os.chdir(r'C:\Users\user\Desktop\Project\yzm')
def get_bin_table(threshold=140):
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table
def get_point(pic,x,y):
	cut=0
	T=[]
	l=4
	start=0
	for j in range(y):
		for i in range(x):
			if pic.getpixel((i,j))==0:
				if cut<i:
					if i-cut>l:
						T.append(i)
						start=i
					cut=i
	return T
def get_crop(path):
	pic_list=os.listdir(path)
	for img in pic_list:
		flag=0
		try:
			ima=Image.open(path+'/'+img)
			pic=ima.convert('L')
			table=get_bin_table()
			out = pic.point(table, '1')
			width,height=out.size
			T=get_point(out,width,height)
			start=0
			tt=[]
			for i in T:
				tt.append(out.crop((start,0,i,20)))
				start=i-2
			tt.append(out.crop((start,0,width,20)))
			for i in tt:
				i=i.resize((14,20))
				i.save(r'C:\Users\user\Desktop\Project\yzm'+'/t/'+str(flag)+img)
				flag+=1
		except Exception as e:
			print(e)
	print('finsh crop')


if __name__=='__main__':
	path=r'C:\Users\user\Desktop\Project\yzm\test'
	get_crop(path)