#LOAD THE CONFIG
import json

# Open the configuration file
with open('config.json') as f:
    # Load JSON data from file
    config = json.load(f)

# Accessing SC_DOMAIN
SITE = config["Siti"]
FT_DOMAIN = SITE["Filmpertutti"]['domain']
SC_DOMAIN = SITE["StreamingCommunity"]['domain']
TF_DOMAIN = SITE["Tantifilm"]['domain']
LC_DOMAIN = SITE["LordChannel"]['domain']
SW_DOMAIN = SITE["StreamingWatch"]['domain']
AW_DOMAIN = SITE['AnimeWorld']['domain']
SKY_DOMAIN = SITE['SkyStreaming']['domain']
MYSTERIUS = SITE['Mysterius']['enabled']
DLHD = SITE['DaddyLiveHD']['enabled']
#General
GENERAL = config['General']
dotenv = GENERAL["load_env"]
HOST = GENERAL["HOST"]
PORT = GENERAL["PORT"]
Public_Instance = GENERAL["Public_Instance"]
MediaProxy = GENERAL["MediaProxy"]
ForwardProxy = GENERAL["ForwardProxy"]