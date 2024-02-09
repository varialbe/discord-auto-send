# Discord Automation Script

## Description

Automates sending messages on Discord for educational purposes, handling channel slow modes, rate limits, and supports multiple channels and tokens.

## Requirements
- `python 3.x`
- `requests` library

## Setup

```bash
pip install requests
```

```git
git clone https://github.com/varialbe/discord-auto-send
cd discord-auto-send
```

## Configuration

- **Message Content**: Edit `text` variable for the message.
- **Channels**: Fill `channels` with channel IDs and slow modes.
- **Tokens**: Add Discord user tokens to `tokens`.

## Usage

```bash
python bot.py
```
## Advanced: Retrieving Discord Token (For Educational Purposes)

To view your Discord token for educational or debugging purposes, you can use the following method within the Chrome Developer Tools Console while on the Discord website. This script navigates through the app's modules to find and log the authentication token:

```javascript
(webpackChunkdiscord_app.push([
    [''], {},
    e => {
        m = [];
        for (let c in e.c) m.push(e.c[c])
    }
]), m).find(m => m?.exports?.default?.getToken !== void 0).exports.default.getToken()
```


### Important Disclaimer

- **Use With Caution**: Directly accessing or modifying Discord's client tokens can violate Discord's Terms of Service. This information is provided strictly for educational purposes.
- **Risk of Account Suspension**: Improper use of your Discord token or automating actions without permission could lead to account suspension or termination.
- **Security Risk**: Your token provides full access to your Discord account. Keep it secure and do not share it.

## Warning

Intended for educational use. Ensure compliance with Discord's Terms of Service. The use of automation and retrieval of sensitive information such as tokens must be handled with extreme caution.

## Contribution

Contributions are welcome. Submit PRs or open issues for discussion.

## License

[MIT License](LICENSE.md)
```
