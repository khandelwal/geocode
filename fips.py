#!/usr/bin/env python

import sys
import csv

import geocode

def get_FIPS_lookup():
	""" Reads in the FIPS codes, and returns a FIPS code, region name dictionary. """

	county_file = open('state-county-fips-codes.txt').readlines()
	counties = [l.strip('\n').strip().split(' ', 1) for l in county_file]

	county_lookup = {}

	for county in counties:
		fips_code = county[0]
		county_name = county[1].strip()

		county_lookup[fips_code] = county_name

	return county_lookup

def fips2centerlatlong(list_fips_codes):
	fips_lookup = get_FIPS_lookup()

	""" Geocode a a list of FIPS codes to a list of tuples providing the
	lat/long of the center of the region specified by the FIPS code. """

	geocode_results = []

	for fips_code in list_fips_codes:
		results = geocode.yahoo_geocode("%s, %s" % (fips_lookup[fips_code], 'US'))
		first_result = results['ResultSet']['Results'][0]
		latlong = (first_result['latitude'], first_result['longitude'])

		geocode_results.append((fips_code, latlong))
	return geocode_results

if __name__ == '__main__':
	results = fips2centerlatlong(['54031', '02'])
	print results
