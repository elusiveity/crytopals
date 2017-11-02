#!/bin/python

import base64

ccfrom = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
ccto = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

decoded = ccfrom.decode('hex')
encoded = base64.b64encode(decoded)

print "HEX: " + ccfrom
print "Base64: " + encoded
print "Decoded: " + decoded
