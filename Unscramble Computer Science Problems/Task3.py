"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re


def bang_call(num):
    if re.search("\(080\)[0-9]+", num):
        return "fixed"
    elif re.search("[789]+[0-9]+ [0-9]+", num):
        return "mobile"
    elif re.search("140[0-9]+", num):
        return "telemarketer"
    return None


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    # calls format:
    # calling telephone number (string),
    # receiving telephone number (string),
    # start timestamp of telephone call (string),
    # duration of telephone call in seconds (string)
    numbers_that_received_calls = set()

    for call, rec, _, _ in calls:
        if bang_call(call):
            numbers_that_received_calls.add(rec)
    numbers_that_received_calls = [x for x in numbers_that_received_calls]
    numbers_that_received_calls.sort()

    print("The numbers called by people in Bangalore have codes:")
    for i in numbers_that_received_calls:
        print(i)

    total_fixed_bang_outgoing = 0
    total_fixed_bang_incoming = 0

    for c, r, _, _ in calls:
        if bang_call(c) == "fixed":
            total_fixed_bang_outgoing += 1
            if bang_call(r) == "fixed":
                total_fixed_bang_incoming += 1
    print("%s percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." % round(total_fixed_bang_outgoing / total_fixed_bang_incoming, 2))

# The time complexity of this is O(n), excluding lines of code other than the for loops it is roughly 4n.
# However, since 4 is a constant we can omit the 4 and realise that the time of the algorithm increases
# linearly with the size of n


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
