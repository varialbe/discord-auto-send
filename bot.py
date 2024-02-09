import requests
import json
import time

text = """
Message content here.
"""

channels = {
    # ChannelID (Str) : Slowmode (Int)
}


tokens = [
    # Token (Str)
]


next_send_time = {channel: 0 for channel in channels}

def send(channel, token, text):
    url = f"https://discord.com/api/v9/channels/{channel}/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    # Dont touch the body.
    body = {
        "content": text,
        "tts": False,
        "embeds": [{
            "title": "Hello, Embed!",
            "description": "This is an embedded message."
        }]
    }

    response = requests.post(url=url, headers=headers, data=json.dumps(body))
    print(response.status_code, channel)
    return response.status_code

while True:
    current_time = time.time()
    for channel, cooldown in channels.items():
        if current_time >= next_send_time[channel]:
            for token in tokens:
                status_code = send(channel, token, text)
                if status_code == 200:
                    next_send_time[channel] = current_time + cooldown
                elif status_code == 429:
                    print("Rate limited. Adjusting cooldown...")
                    next_send_time[channel] = current_time + cooldown + 60
                elif status_code == 403:
                    print("Timed out. Adjusting cooldown...")
                    next_send_time[channel] = current_time + cooldown + 200
                elif status_code == 404:
                    print("Channel has been deleted or does not exist.")
    time.sleep(1)  
