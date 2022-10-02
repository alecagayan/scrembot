#send twitch stream alerts to a channel
from twitchAPI.twitch import Twitch

import discord
from discord.ext import commands

import asyncio
import config

class StreamAlerts(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.twitch = Twitch(config.twitch_client_id, config.twitch_client_secret)
        self.twitch.authenticate_app([])
        self.streamer = "screeeeeeem"
        self.channel = self.client.get_channel(config.stream_alerts_channel)
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.stream_alerts())

    async def stream_alerts(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            for streamer in self.streamers:
                stream = self.twitch.get_streams(user_login=streamer)
                if stream['data']:
                    await self.channel.send(f"{streamer} is live! https://twitch.tv/{streamer}")
            await asyncio.sleep(60)


