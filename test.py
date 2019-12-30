import os
from random import randrange
import time 

with open('./abuser.py', mode='w') as my_file:
	for i in range(30):
		rand_num = randrange(10)
		for i in range(rand_num):
			rand_num = randrange(10)
			my_file.write(str(rand_num))
			time.sleep(5)
			os.system("git add .")
			os.system(f'git commit --date="{rand_num} day ago" -m "Your commit message"')
			os.system("git push")