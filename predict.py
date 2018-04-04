import sys
sys.path.append('D:\soft\libsvm-3.22\python')
from svmutil import *
def predict(dataset):	
	y, x = svm_read_problem(dataset)
	p_label, p_acc, p_val = svm_predict(y,x, model)
	img.save('./test/test/%s/%s.png'%(str(i).split('.')[0],str(p_label[0]).split('.')[0]))

if __name__ == '__main__':
	dataset='smvlight.dat'
	predict(dataset)