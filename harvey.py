import requests
import json

r = requests.get('https://shopharveys.com/products.json?limit=20000000')
products = json.loads((r.text))['products']

#def availibilitycheck():
for product in products:
	print(product['title'])
	#productname = product['title']

	#if productname == 'Cali Bear / Chambray (Pre-Order Ship Date 8/28/2020)':
	
	#	producturl = 'https://shopharveys.com/products/' + product['handle']
	#	print(producturl)
			#return producturl
			
	#return False