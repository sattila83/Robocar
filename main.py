#!/usr/bin/env python

import sys
from robocar import Robocar
from input_parser import InputParser

if __name__ == "__main__":
	if 2 == len(sys.argv):
		positions = InputParser.parse(sys.argv[1])
		Robocar(positions).start()
		exit(0)
	else:
		print "Usage: %s <input_coords_file_path>" % sys.argv[0]
		exit(1)