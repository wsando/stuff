import requests
import json

r = requests.get('https://shopharveys.com/products.json?limit=20000000')
products = json.loads((r.text))['products']

#def availibilitycheck():
for product in products:
	#print(product['title'])
	productname = product['title']

	if productname == 'Limited Edition Medium Tote / Saved By The Belle':
	
		producturl = 'https://shopharveys.com/products/' + product['handle']
		print(producturl)
			#return producturl
			
	#return False