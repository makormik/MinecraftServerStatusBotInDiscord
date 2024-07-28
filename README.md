# Discord Minecraft Server Status Bot

This Discord bot provides Minecraft server status information directly within Discord. It uses the `mcstatus` library to gather server data and `discord.py` for Discord interactions.

## Features

- Retrieve Minecraft server details:
  - IP address and port
  - Current and maximum player count
  - Server version
  - Server ping
  - MOTD (Message of the Day) saved as a text file

## Installation

1. Ensure Python 3.8 or higher is installed. [Download Python](https://www.python.org/downloads/) if needed.

2. Install the required libraries with pip:

    
    pip install discord.py mcstatus

   there might be more libraries, make sure you downloaded all of them.
    

4. Save the provided script to a file named `bot.py`.

5. Replace `YOUR_BOT_TOKEN` in the script with your Discord bot token. Ensure this token remains private.

6. Start the bot with:

    
    python bot.py
    

## Usage

- Use the `/ping <server_ip>` command in Discord to get Minecraft server status.
  - `<server_ip>` - The IP address of the Minecraft server.

