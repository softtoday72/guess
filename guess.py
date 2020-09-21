import random
r = random.randint(1, 100)
while True: 
	g = input('請輸入數字: ')
	g = int(g)
	if g == r :
		print('猜對了')
		break
	elif g < r :
		print('再加一點')
	elif g > r :
		print('再少一點')