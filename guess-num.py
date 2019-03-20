import random
	r = random.randint(1, 100)
while True:
	num = input('請猜數字(1-100): ')
	num = int(num)
	if num == r:
		print('恭喜猜中了!')
		break
	elif num < r:
		print('比答案小喔')
	else:
		print('比答案大喔')
	
	