import requests

def getPageContent(url):
	return requests.get(url)