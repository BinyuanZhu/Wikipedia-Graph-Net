"""
This file contains all the WikiMedia API request related functions. A sample call would look like:
https://en.wikipedia.org/w/api.php?action=query&titles=Albert%20Einstein&prop=links
for the query Albert Eintein
"""
import json
mockTitle = "Dog"

def get_links(title: str) -> str:
	"""
	Given a query that can be assumed to be a Wikipedia Article Title, get the JSON for links back.
	"""
	baseURL = "https://en.wikipedia.org/w/api.php?action=query&titles=TEMP&prop=links"
	query = title.replace(" ", "%20")
	return baseURL.replace("TEMP", query)

def get_title(link):
	pass
