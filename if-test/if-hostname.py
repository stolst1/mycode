#!/usr/bin/env python3
# The objective of this lab is to write a program to collect data from a user, and test if that data matches an expected value.
hostname = input ('Please enter the hostname:')
print('You told me the hostname is: ' + hostname)
if hostname.lower() == 'mtg': # to include upper and lower case letters
	print('The hostname matches the expected config')
print ('Exiting the script.')

