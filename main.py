import random, sys

SPINS = 10
STREAK_SIZE = 3
NUM_ZEROS = 1
PROPORTION_OF_ZEROES_IN_STREAK = 0.5

def single_spin():
	r = random.randint(1,36 + max([1, NUM_ZEROS]))
	if r > 36:
		return 'zero'
	if r % 2 == 0:
		return 'even'
	else:
		return 'odd'

def set_of_spins(n):
	spins = []
	for i in range(n):
		spins.append(single_spin())
	return spins

def parse_spins(spins):
	
	total = 0

	lastResult = 'zero'

	results = {
		'total': 0,
		'odd': 0,
		'even': 0}

	spinsSinceCounters = {
		'odd': 0,
		'even': 0,
		'zero': 0}

	def did_bet(outcome):
		more_than_streak_since = spinsSinceCounters[outcome] >= STREAK_SIZE
		return more_than_streak_since



	for result in spins:

		lastResult = result

		if result == "odd":
			if did_bet('odd'):
				results['total'] += 1	
				results['odd'] += 1
			elif did_bet('even'):
				results['total'] += 1
		
			spinsSinceCounters['odd'] = 0
			spinsSinceCounters['even'] += 1


		elif result == "even":
			if did_bet('even'):
				results['total'] += 1	
				results['even'] += 1
			elif did_bet('odd'):
				results['total'] += 1
				
			spinsSinceCounters['odd'] += 1
			spinsSinceCounters['even'] = 0


		elif result == 'zero':
			if did_bet('even') or did_bet('odd'):
				results['total'] += 1	
				
			spinsSinceCounters['odd'] += 1
			spinsSinceCounters['even'] += 1


		if SPINS <= 50:
			print("result: {}\tsince odd: {}\teven: {}\tzero: {}\ttotal: {}\tsuccessful: {}".format(result, spinsSinceCounters['odd'], spinsSinceCounters['even'], spinsSinceCounters['zero'], results['total'], results['odd'] + results['even']))

	return results

def main():
	
	spins = set_of_spins(SPINS)

	results = parse_spins(spins)

	print("odd: {}\teven {}\ttotal: {}\t{}".format(results['odd'], results['even'], results['total'], 100 *(results['odd'] + results['even'] )/ max([1,results['total']])))



if __name__ == '__main__':

	try:
		SPINS = int(sys.argv[1])
		STREAK_SIZE = int(sys.argv[2])
	except:
		pass
	main()