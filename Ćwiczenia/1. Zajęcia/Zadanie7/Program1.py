# Simplest solution

given_num = int(input('> '))

if given_num == 0:
	print(True)
	exit()

fibs = [0, 1]
while fibs[-1] <= given_num:
	fibs.append(sum(fibs[-2:]))  # The same as: fibs[-1] + fibs[-2]
	quotient = given_num / fibs[-1]
	if quotient != int(quotient):
		continue

	quotient = int(quotient)
	if quotient in fibs[:-1]:
		print(True, f'{quotient} * {fibs[-1]} = {given_num}')
		break
else:
	print(False)
