import os
import sys
import time
import datetime

INFO_START_PING = 'Initiating ping operation to the specified IP address '
INFO_CONTINUE_PING = '(Press CTRL+C to stop)...'
INFO_STATS = 'Ping operation completed. Statistics:'
PACKETS_PER_SECOND = 1
PACKET_LENGTH = 98
DATA_LENGTH = 1

def get_current_time():
    return '[' + datetime.datetime.now().strftime('%H:%M:%S') + ']'
def calculate_time_difference():
    return datetime.datetime.now() - start_time
def generate_statistics():
    elapsed_time = calculate_time_difference()
    packets_sent = int(elapsed_time.total_seconds() * PACKETS_PER_SECOND * PACKET_LENGTH / DATA_LENGTH)
    return ('Elapsed Time: ' + str(elapsed_time) + '\n' +' Data Sent: ' + str(packets_sent))

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    print(INFO_START_PING + sys.argv[1] + ' ' + INFO_CONTINUE_PING)
    os.system('ping -W 0.1 ' + sys.argv[1])
    print('\n\n' + get_current_time() + INFO_STATS + '\n\n' + generate_statistics())
