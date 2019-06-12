import os
from random import randint
import os.path
from pathlib import Path
def shuffle():
	i=0
	for i in range(25001):
		k=randint(0,25000)
		if(k==i):
			continue
		print(i)
		print(k)
		os.rename('images/A/T'+str(k)+'.jpg','images/A/temp.jpg')
		os.rename('images/B/L'+str(k)+'.jpg','images/B/temp.jpg')
		os.rename('images/A/T'+str(i)+'.jpg', 'images/A/T'+str(k)+'.jpg')
		os.rename('images/B/L'+str(i)+'.jpg', 'images/B/L'+str(k)+'.jpg')
		os.rename('images/A/temp.jpg','images/A/T'+str(i)+'.jpg')
		os.rename('images/B/temp.jpg','images/B/L'+str(i)+'.jpg')
	#print("shuffling")
if __name__ == '__main__':
	
	shuffle()
	k=[]
	for i in range(25001):
		file=Path('images/A/T'+str(i)+'.jpg')
		file1=Path('images/B/L'+str(i)+'.jpg')
		if(file.is_file()):
			if(file1.is_file()):
				continue
			else:
				print('Missing Label at :',i)
		else:
			k.append(i)
			print('Missing at ', i)
