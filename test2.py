from random import randrange
import os

rand_day = randrange(50,100)

for i in range(5):
	rand_num = randrange(10)
	my_file = open('./abuser.py', 'a')
	my_file.write(str(rand_num))
	my_file.close()
	os.system("git status")
	os.system("git add .")
	os.system(f'git commit --date="{rand_day} day ago" -m "Your commit message {rand_num}"')
	os.system("git push")
	os.system("git status")