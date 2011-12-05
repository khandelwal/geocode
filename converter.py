#!/usr/bin/env python

import sys
import csv

import geocode


def get_county_lookup():
	""" Reads in the FIPS codes, and returns a county fips code, county name dictionary. """
	county_file = open('state-county-fips-codes.txt').readlines()
	counties = [l.strip('\n').strip().split(' ', 1) for l in county_file]

	county_lookup = {}

	for county in counties:
		fips_code = county[0]
		county_name = county[1].strip()

		county_lookup[fips_code] = county_name

	return county_lookup

def convert(list_fips_codes):

if __name__ == '__main__':

	county_lookup = get_county_lookup()
	result = geocode.yahoo_geocode("%s, %s" % (county_lookup[fips_code], 'US') )

	results = result['ResultSet']['Results']
	print results
