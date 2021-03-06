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
import sys

from mcm.sdos import configuration
from mcm.sdos.core import Frontend
from mcm.sdos.util import treeGeometry
from sdos.core import CascadeProperties
from sdos.swift import SwiftBackend

logging.basicConfig(level=configuration.log_level)
log = logging.getLogger()

###############################################################################
###############################################################################

if __name__ == '__main__':
	log.debug('geomtest start')
	log.debug(sys.version)
	log.debug(sys.flags)
	# frontend = Frontend.DirectFrontend(containerName='sdosTest1')
	# frontend = Frontend.CryptoFrontend(containerName='sdosTest1')
	sb = SwiftBackend.SwiftBackend(user='test:tester', key='testing')
	cp = CascadeProperties()
	frontend = Frontend.SdosFrontend(containerName='sdt1', swiftBackend=sb, cascadeProperties=cp)
	cascade = frontend.cascade

	print(treeGeometry.sdos_used_partitions(cascade=cascade))
	print(treeGeometry.sdos_partition_mapping(cascade=cascade))
	print(treeGeometry.sdos_cascade_stats(cascade=cascade))
	treeGeometry.print_reverse_slot_mapping(cascade=cascade)
	print(treeGeometry.sdos_slot_utilization(cascade=cascade))










