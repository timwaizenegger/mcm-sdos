#!/usr/bin/python
# coding=utf-8

"""
	Project MCM - Micro Content Management
	SDOS - Secure Delete Object Store


	Copyright (C) <2016> Tim Waizenegger, <University of Stuttgart>

	This software may be modified and distributed under the terms
	of the MIT license.  See the LICENSE file for details.
"""

import logging
from mcm.sdos.crypto.CryptoLib import CryptoLib
HEADER = 'SDOS_ENCO_V1____'.encode(encoding='utf_8', errors='strict') # should always be 16 bytes long

class DataCrypt(object):
	"""
	classdocs
	"""


	def __init__(self, key):
		"""
		Constructor
		"""
		self.log = logging.getLogger(__name__)
		self.log.debug('initializing')
		self.key = key
		self.cl = CryptoLib(key, HEADER)

	###############################################################################
	###############################################################################



	###############################################################################
	###############################################################################
	def encryptBytesIO(self, plaintext):
		self.log.debug('encrypting data with key: {}'.format(self.key))
		return self.cl.encryptBytesIO(plaintext)

	def decryptBytesIO(self, ciphertext):
		self.log.debug('decrypting data with key: {}'.format(self.key))
		return self.cl.decryptBytesIO(ciphertext)
