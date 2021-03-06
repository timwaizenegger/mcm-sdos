#!/usr/bin/python
# coding=utf-8

"""
	Project MCM - Micro Content Management
	SDOS - Secure Delete Object Store


	Copyright (C) <2016> Tim Waizenegger, <University of Stuttgart>

	This software may be modified and distributed under the terms
	of the MIT license.  See the LICENSE file for details.
"""

from sys import argv
import io
from mcm.sdos.crypto.CryptoLib import CryptoLib

if __name__ == '__main__':
	print("SDOS decrypt tool")
	print("syntax: 1) keystring, 2) in-file")
	print("tool will create a new file with the decrypted content")
	print(argv[1])
	print(argv[2])

	keyString = argv[1]
	filePath = argv[2]

	cl = CryptoLib()
	cl.setKeyString(keyString)
	f = open(filePath, 'b+r')
	enc = io.BytesIO(f.read())
	f.close()
	dec = cl.decryptBytesIO(enc)
	f2 = open(filePath + '_decrypted', 'b+w')
	f2.write(dec.getvalue())
	f2.close()
