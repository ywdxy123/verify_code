import requests
import os
def get_Pic(n,url):
	for i in range(n):
		pic=requests.get(url)
		with open ('Pic_'+str(i)+'.jpg','wb+') as f:
			f.write(pic.content)
		print('下载第%s次'%i)
if __name__=='__main__':
	url='xxx'
	os.chdir(r'C:\Users\user\Desktop\Project\yzm\test')
	get_Pic(100,url)

