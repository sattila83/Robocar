#!/usr/bin/env python

from position import Position

class InputParser:

	@staticmethod
	def parse(filePath):
		positions = []
		with open(filePath, 'r') as file:
			for line in file.read().splitlines():
				parts = [part.strip() for part in line.split(',')]
				if 2 == len(parts):
					positions.append(Position(float(parts[0]), float(parts[1])))
		return positions
