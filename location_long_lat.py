#!/usr/bin/python3

import requests

#Prints The IP string, ex: 198.975.33.4
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']
print(my_ip)

#Look up the GeoIP information from a database for the user's ip
geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
print(geo_data)