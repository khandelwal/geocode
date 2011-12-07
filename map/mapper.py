import csv

TWELVE_COLOR = ['#8E0152', '#A50026', '#D73027', '#F46D43', '#FDAE61', '#FEE08B', '#FFFFBF', 
		'#D9EF8B', '#A6D96A', '#66BD63', '#1A9850', '#006837']

THREE_COLOR = ['#FC8D59', '#91BFDB', '#FFFFBF',]

def read_data(filename, width):
	""" The data file is a CSV file with county FIPS code, and an integer data point. Read in 
	this data into a dictionary. Also provide a set of the data values. """

	data = {}
	reader = csv.reader(open(filename, 'r'), delimiter=',')

	values = set()
	for row in reader:
		fips = row[0].zfill(width)
		datum = row[1].strip('\n').strip()

		data[fips] = datum
		values.add(datum)

	return(values, data)

def get_state_information():
	""" Return a FIPS code to state abbreviation mapping, as well a list of all the state 
	abbreviations."""
	reader = csv.reader(open('state_fips_codes.txt', 'r'), delimiter=',')

	abbr2fips = {}
	states = []

	for row in reader:
		fips = row[0].strip()
		two_letter = row[2].strip('\n').strip()
		abbr2fips[two_letter] = fips 
		states.append(two_letter)

	return (abbr2fips, states)
