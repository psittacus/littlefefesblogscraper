from bs4 import BeautifulSoup
import requests

r = requests.get("http://blog.fefe.de/") #Liest den HTML-Code der Seite http://blog.fefe.de/ aus

soup = BeautifulSoup(r.content, "html.parser") # Übergibt den HTML Code Beautifulsoup

links = soup.find_all("h3") # Sucht im Code nach dem HTML-Tag <h3> und liefert einen Array zurück

for link in links:
	print ("%s" %(link.text)) # Gibt alle mit h3 getaggten Werte aus
