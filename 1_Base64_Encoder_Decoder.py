'''Python script to encode and decode a string using Base64'''

import base64

word = b'Apple' # Byte string to encode

e1 = base64.b64encode(word)
e2 = e1.decode('UTF-8')
print('Encoded -',e2)

d2 = (base64.b64decode(e2)).decode('UTF-8')
print('Decoded -',d2)