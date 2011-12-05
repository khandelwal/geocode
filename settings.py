#Since we hit the Yahoo! PlaceFinder service to geocode things, you'll need an APP_ID from 
#the Yahoo! PlaceFinder service. 
YAHOO_APP_ID = ''

try:
	from local_settings import * 
except ImportError:
	pass
