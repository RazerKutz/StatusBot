import config
import requests
from io import BytesIO
from  bs4 import BeautifulSoup
from PIL import Image
import urllib.request
from discord.ext import commands

TOKEN = config.beta_app_token
BOT_PREFIX = "!"
client = commands.Bot(command_prefix=commands.when_mentioned_or(BOT_PREFIX))

@client.event
async def on_ready():
    print ("Logged in as")
    print (client.user.name)
    print (client.user.id)
    print ("------")


@client.command(pass_context=True)
async def status(ctx, stuff=""):
    """Send Status"""

    url = 'https://www.gametracker.com/server_info/108.61.118.183:2302/'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    content = urllib.request.urlopen(req).read()

    soup = BeautifulSoup(content, features="html.parser")

    last_scan = soup.find("div", {"id": "last_scanned"})
    response = requests.get("http://cache.gametracker.com/server_info/108.61.118.183:2302/b_560_95_1.png")
    pic = Image.open(BytesIO(response.content))

    pic.save("pic.png")
    # print(testImage)
    await client.upload("pic.png")
    await client.say(last_scan.text)
client.run(TOKEN)