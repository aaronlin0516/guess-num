import random
r = random.randint(1, 100)
x = 0
while True:
	num = input('請猜數字(1-100): ')
	num = int(num)
	x = x + 1
	if num == r:
		print('恭喜猜中了! 您共猜了', x,'次')
		break
	elif num < r:
		print('比答案小喔')
	else:
		print('比答案大喔')
	
	