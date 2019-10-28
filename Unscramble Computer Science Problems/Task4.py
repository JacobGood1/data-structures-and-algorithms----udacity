"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

not_telemarketers = set()
telemarketers = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    # sending telephone number (string),
    # receiving telephone number (string),
    # timestamp of text message (string).
    for s,r,_ in texts:
        not_telemarketers.add(s)
        not_telemarketers.add(r)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    # calling telephone number (string),
    # receiving telephone number (string),
    # start timestamp of telephone call (string),
    # duration of telephone call in seconds (string)
    for _,r,_,_ in calls:
        not_telemarketers.add(r)
    for c,_,_,_ in calls:
        if c not in not_telemarketers:
            telemarketers.add(c)
    telemarketers = [x for x in telemarketers]
    telemarketers.sort()
    print("These numbers could be telemarketers:")
    for i in telemarketers:
        print(i)

# This algorithm is O(n^2) since one of the for loops makes another loop for each item in not_telemarketers

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

