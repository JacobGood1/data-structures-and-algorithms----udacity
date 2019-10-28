"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

call_durations = {}

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for c, r, _, duration in calls:
        if c in call_durations:
            call_durations[c] += int(duration)
        else:
            call_durations[c] = int(duration)
        if r in call_durations:
            call_durations[r] += int(duration)
        else:
            call_durations[r] = int(duration)
    max_call_time = 0
    max_call_num = ""
    for num, dur in call_durations.items():
        if dur > max_call_time:
            max_call_time = dur
            max_call_num = num
    print("%s spent the longest time, %s seconds, on the phone during September 2016." % (max_call_num, max_call_time))

# this algorithm is O(n) or linear

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

