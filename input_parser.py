#!/usr/bin/env python

from position import Position

class InputParser:

	@staticmethod
	def parse(filePath):
		positions = []
		file = open(filePath, 'r')
		for line in file:
			parts = [part.strip() for part in line.split(',')]
			if 2 == len(parts):
				positions.append(Position(float(parts[0]), float(parts[1])))
		return positions