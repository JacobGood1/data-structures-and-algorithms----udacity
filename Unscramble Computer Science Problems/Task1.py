"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

nums = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for call_from, call_to, _ in texts:
        nums.add(call_from)
        nums.add(call_to)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call_from, call_to, _, _ in calls:
        nums.add(call_from)
        nums.add(call_to)
    print("There are %s different telephone numbers in the records." % (len(nums)))

# The algorithm is O(n), linear time
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
