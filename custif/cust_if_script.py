#!/usr/bin/env python3
# Creating your own code with if, elif, and else!
message = 'The category of Hurricane in your area is a Category'
print('What is the wind speed in your area?')
wind = float(input())
if wind >=130:
    message = message + '4.'
elif wind >= 111:
    message = message + '3.'
elif wind >= 96:
    message = message + '2.'
else:
    message = message + '1.'
print(message)
