#standalone script to test stream alerts

from twitchAPI.twitch import Twitch
import asyncio

#ask user for streamer name and return if they are live or not
def stream_alerts():
    twitch = Twitch('qwjesmnaxdftd0at1f1zdjiidulct3', 'qx1c49w72rt8r38kme9sqi438tcjr6')
    twitch.authenticate_app([])
    #streamer = input("Enter streamer name: ")
    streamer = "oxpsie"
    stream = twitch.get_streams(user_login=streamer)
    if stream['data']:
        print(f"{streamer} is live!")
    else:
        print(f"{streamer} is not live.")

# run every 60 seconds
def run_function():
    try:
        stream_alerts()
        print("\n\n")
        # run every 60 seconds
        asyncio.sleep(60)
    finally:
        asyncio.run(run_function())

asyncio.run(run_function())



