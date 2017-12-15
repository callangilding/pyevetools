from urllib import urlopen
import simplejson as json

url = urlopen('https://esi.tech.ccp.is/dev/status/?datasource=tranquility').read()
url = json.loads(url)

print url.get('players') >> /dev/tty1 # Send to HDMI out
