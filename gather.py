
import time
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back
init(autoreset=True) #Para que colorama resetee siempre el color ( a blanco ) sin tener que escribirlo nosotros

#COMIENZO CREACIÓN FICHERO PROXIES.TXT
print (Fore.CYAN+"[X]"+Fore.YELLOW+" Creando archivo"+Fore.MAGENTA+""" "proxies.txt" """)
try:
	f = open("proxies.txt","w+")
	print (Fore.CYAN+"[X]"+Fore.YELLOW+" Archivo creado satisfactoriamente.")
except:
	pass

#FIN CREACIÓN FICHERO PROXIES.TXT

		
	


url = "https://free-proxy-list.net/anonymous-proxy.html"
r = requests.get(url)
rhtml = r.content
soup = BeautifulSoup(rhtml,"html.parser")

tabla = soup.find("table", {"id" : "proxylisttable"})
cuenta  = 0


formatoip="IP:PUERTO"
formatopais="PAÍS"
formatoweb="WEB"

ippuertolista = []


#print ("%-30s %-30s %s"%(formatoip,formatopais,formatoweb))
for columna in tabla.find_all("tr"):
	columnas = columna.find_all("td")
	try:
		ip = columnas[0].get_text()
		puerto = columnas[1].get_text()
		ippuerto = Fore.MAGENTA+ip+":"+puerto
		pais = Fore.YELLOW+columnas[3].get_text()
		webs= Fore.CYAN+"from "+Fore.RED+"https://free-proxy-list.net/anonymous-proxy.html"
		print ("\n"+"%-30s %-30s %s"%(ippuerto,pais,webs))
		cuenta = cuenta+1

		#añadir a archivo
		puertoip = "\n"+ip+":"+puerto
		ippuertolista.append(puertoip)


	except:
		pass

print ("-"*30+"\n"+Back.WHITE+Fore.BLACK+"[X]Proxies conseguidos: "+Fore.RED+str(cuenta))





for x in ippuertolista:
	f.write(x)
f.close()
