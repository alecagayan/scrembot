#standalone script to test stream alerts

from twitchAPI.twitch import Twitch

#ask user for streamer name and return if they are live or not
def stream_alerts():
    twitch = Twitch('qwjesmnaxdftd0at1f1zdjiidulct3', 'qx1c49w72rt8r38kme9sqi438tcjr6')
    twitch.authenticate_app([])
    streamer = input("Enter streamer name: ")
    stream = twitch.get_streams(user_login=streamer)
    if stream['data']:
        print(f"{streamer} is live!")
    else:
        print(f"{streamer} is not live.")

stream_alerts()


