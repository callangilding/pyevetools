from urllib import urlopen
import simplejson as json
import os

url = urlopen('https://esi.tech.ccp.is/dev/status/?datasource=tranquility').read()
url = json.loads(url)

intro = """
_______________   _______________ ________         .__  .__               
\_   _____/\   \ /   /\_   _____/ \_____  \   ____ |  | |__| ____   ____  
 |    __)_  \   Y   /  |    __)_   /   |   \ /    \|  | |  |/    \_/ __ \ 
 |        \  \     /   |        \ /    |    \   |  \  |_|  |   |  \  ___/ 
/_______  /   \___/   /_______  / \_______  /___|  /____/__|___|  /\___  >
        \/                    \/          \/     \/             \/     \/
"""

clear = lambda: os.system('clear')
clear()

print(intro)
print 'Players Online: ', url['players']
