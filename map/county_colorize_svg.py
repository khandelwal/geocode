#!/usr/bin/env python

import csv
from BeautifulSoup import BeautifulSoup

twelve_color = ['#8E0152', '#A50026', '#D73027', '#F46D43', '#FDAE61', '#FEE08B', '#FFFFBF', 
		'#D9EF8B', '#A6D96A', '#66BD63', '#1A9850', '#006837']

THREE_COLOR = ['#FC8D59', '#FFFFBF', '#91BFDB']

def read_data(filename):
	""" The data file is a CSV file with county FIPS code, and an integer data point. Read in 
	this data into a dictionary. Also provide a set of the data values. """

	data = {}
	reader = csv.reader(open(filename, 'r'), delimiter=',')

	values = set()
	for row in reader:
		fips = "%05d" % int(row[0])
		datum = row[1].strip('\n').strip()

		data[fips] = datum
		values.add(datum)

	return(values, data)

if __name__ == '__main__':
	values, data = read_data('data/county_weighted.txt')

	svg = open('US_counties.svg', 'r').read()

	soup = BeautifulSoup(svg, selfClosingTags=['defs', 'sodipodi:namedview'])
	
	#You want to specify as many colors as you have values
	colors = twelve_color
	paths = soup.findAll('path')

	# County style
	path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1; stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt; marker-start:none;stroke-linejoin:bevel;fill:'

	for p in paths:
		if p['id'] not in ['State_Lines', 'seperator']:
			try: 
				datum = data[p['id']]
			except:
				continue	

			color = colors[int(datum)]
			p['style'] = path_style + color

	print soup.prettify()
