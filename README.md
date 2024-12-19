# MammaMia
A Stremio Addon for high quality HTTPS Streams in Italian
Movies, Series, Anime and Live TV are supported.
While hosting, this project, remember that Filmpertutti uses Mixdrop. Mixdrop only allows seeing the videos from the same IP where they were generated so, if you want to scrape filmpertutti, you will have to host this project locally. Else, you can only scrape other providers.
Hosting your own instance is suggested, but you can use the public instance [linked](https://mammamia-ig0e.onrender.com/) in the About Page of the repo.

# Installation
## Local
1. Install required packages
``pip install -r requirements.txt ``
2. Create a .env file and fill it (look at example.env)
3. Then to start the Fast API app server just execute:
``python3 run.py``

## Render
To install this project on [Render](https://render.com/) follow these steps:
1. Create an Account
2. Create a Web Service
3. Fork the repo and then connect it to Render
4. Among the other environment variables, put PORT = 8080. This is needed because Render needs the Port given as an environment variable. Remember to put TMDB_KEY as an enviroment variable.
5. As build command put `` pip install -r requirements `` and as run command put ``python3 run.py ``
6. Then just finish Render Setup and you are done :)

Remember, load_env and Public Instance needs to be disabled in the config.json

# How to add to Stremio
Open your instance URL and configure MammaMia. Once you are done you can click on INSTALL Button. If it doesn't work click on Generate Manifest and copy it. Then paste it  in Stremio Search Bar. If you are on Mac or on Web go to addons, click Add an Addon, and paste it there.

# Enviroment Variables
| Enviroment Variable | Value |
|-------------------------|---|
|TMDB_KEY|INSERT YOUR API KEY HERE|
Here is [linked](https://www.themoviedb.org/settings/api) a tutorial about how to get a TMDB KEY

# Config
In the repo there is a config.json that you can modify to change some aspects of the addon like the domains of the sites. Down here all explained:
| Config | Value |
|-------------------------|---|
| Domain | The domain of the site, must be a string |
|enabled | If the site is enabled or not. "1" means true. "0" means false. Remember, there is no point in enabling filmpertutti on a remote server since it's IP-LOCKED|
|fast_search|"1" for enabled, "0" for disabled. It enables a faster search for supported providers but it is less accurate|
|load_env|Put "1" if enabled, "0" if disabled. It needs to be enabled if you need to load a .env file. On remote hosting services, like Hugging Face or Render, it needs to be disabled. |
|HOST| The host for the Fast API APP|
|PORT| The port for the Fast API APP. Default: 8080 |

For now Mysterius must be kept disabled if you do not know what you are doing.
For now Tantifilm, even if its player is not IP-Locked, does not work on Hugging Face.

Check those links to get the new Domain for the providers.

[FILMPERTUTTI](https://filmpertuttiiii.nuovo.live/)

[STREAMINGCOMMUNITY](https://t.me/+jlXmmprhtakxYWJh)

[TANTIFILM](https://tantinuovo.com/tantifilm-nuovo-indirizzo/)

[STREAMINGWATCH](https://t.me/streamingwatch)

[LORDCHANNEL](https://t.me/+5MQwrb3eqb81NGI0)

[ANIMEWORLD](https://t.me/AnimeWorldITA2)

## Credits
- This project is a fork of the official MammaMia adddon created by [UrloMythus](https://github.com/UrloMythus/MammaMia).
- Big thanks to [Lovi0](https://github.com/Lovi-0), the creator of StreamingCommunity downloader, for helping me with some aspects of this project.
- This project uses [MediaFlowProxy](https://github.com/mhdzumair/mediaflow-proxy/) in order to be able to play some Live TV channels. Big thanks to his creator, [mhdzumair](https://github.com/mhdzumair)

## Disclaimer
This project does not host any  illegal content on his servers, if you want any content  to be taken down, please contact the actual owners of those sites.  
The Live TV sources are taken from online sites, avaiable on the web and indixed by Google. 


