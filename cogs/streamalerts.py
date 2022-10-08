#send twitch stream alerts to a channel
from twitchAPI.twitch import Twitch

import discord
from discord.ext import commands

import asyncio
import config
import json

class StreamAlerts(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.twitch = Twitch(config.twitchid, config.twitchsecret)
        self.twitch.authenticate_app([])
        self.streamer = "screeeeeeem"
        self.channel = self.client.get_channel(965397925150736444)
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.stream_alerts())

    async def stream_alerts(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            stream = self.twitch.get_streams(user_login=self.streamer)

            if stream['data'] and stream["data"][0]["id"] not in json.load(open("./data/json/streams.json", "r")):
                # check if streamer is in the json file
                    print(f"{self.streamer} is live!")
                    await self.channel.send(f"{self.streamer} is live! https://twitch.tv/{self.streamer}\n\n<@&1026293611471568937>")
                    # add streamer to json file
                    json.dump(stream["data"][0]["id"], open("./data/json/streams.json", "w"))

            await asyncio.sleep(60)



def setup(bot):
    bot.add_cog(StreamAlerts(bot))

