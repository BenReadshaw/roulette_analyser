import random, sys

SPINS = 10000
STREAK_SIZE = 5

def spin():
	r = random.randint(0,36)
	if r % 2 == 1:
		return True
	return False

def main():
	
	remaining = SPINS
	spins = []
	while remaining > 0:
		spins.append(spin())
		remaining -= 1

	total = 0
	successful = 0

	lastResult = True
	consecutiveFalse = 0
	for result in spins:
		lastResult = result
		if result:
			if consecutiveFalse >= STREAK_SIZE:
				total += 1
				successful += 1
			consecutiveFalse = 0
		else:
			if consecutiveFalse >= STREAK_SIZE:
				total += 1
			consecutiveFalse += 1
		if SPINS <= 50:
			print("result: {}\tconsecutive: {}\ttotal: {}\tsuccessful: {}".format(result, consecutiveFalse, total, successful))

	print("Spun {} times\n{} Ouf of {} bets were successful\t{}% success rate".format(SPINS, successful, total, 100*successful/total))



if __name__ == '__main__':

	try:
		SPINS = int(sys.argv[1])
		STREAK_SIZE = int(sys.argv[2])
	except:
		pass
	main()