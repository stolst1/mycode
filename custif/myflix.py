#!/usr/bin/env python3
# The objective of this lab is to write your own custom script utilizing the if, elif, and else statements, along with any of the other Python coding tricks.
message = 'The movie is about to begin, we recommend '
print('What is your connection speed in Mbps?')
connection = float(input())
if connection >= 25:
    message = message + 'setting video to 4k.'
elif connection >= 5:
    message = message + 'setting video to 1080p.'
elif connection >= 2:
    message = message + 'setting video to 720p.'
else:
    message = message + 'finding another access network.'
print(message)