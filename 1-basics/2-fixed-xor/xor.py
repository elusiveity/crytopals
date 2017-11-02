#!/bin/python

thing1 = "1c0111001f010100061a024b53535009181c"
thing2 = "686974207468652062756c6c277320657965"

def fixedxor(a,b):

	for c,d in a,b:
		print c + ":" + d

fixedxor(thing1,thing2)
