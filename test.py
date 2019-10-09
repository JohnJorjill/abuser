import os
from random import randrange
import time 

day_counter = 0
write_counter = 0

with open('./abuser.py', mode='w') as my_file:
	for i in range(5):
		day_counter = day_counter + 1
		print(f'writing {i} day')
		rand_num = randrange(10)
		for i in range(rand_num):
			write_counter = write_counter + 1
			print(f'writing {write_counter} times')
			rand_num2 = randrange(10)
			my_file = open('./abuser.py', 'w')
			my_file.write(str(rand_num))
			print(f'wrote {rand_num2} to file')
			my_file.close()
			time.sleep(5)

			#os.system("git add .")
			#os.system(f'git commit --date="{rand_num2} day ago" -m "Your commit message"')
			#os.system("git push")