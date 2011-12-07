#!/usr/bin/env python

import sys
from BeautifulSoup import BeautifulSoup

import mapper

def colorize(datafilename):
	values, data = mapper.read_data(datafilename, 2)

	svg = open('Blank_US_Map.svg', 'r').read()
	soup = BeautifulSoup(svg, selfClosingTags=['defs', 'sodipodi:namedview'])

	paths = soup.findAll('path')

	abbr2fips, states = mapper.get_state_information()

	path_style = 'stroke:#ffffff;stroke-opacity:1;stroke-width:0.75;stroke-miterlimit:4;stroke-dasharray:none;fill:'

	colors = mapper.THREE_COLOR

	for p in paths:
		if p['id'] in states:
			try:
				datum = data[abbr2fips[p['id']]]
			except:
				continue
			color = colors[int(datum)]
			p['style'] = path_style + color

	print soup.prettify()


if __name__ == '__main__':
	colorize(sys.argv[1])
