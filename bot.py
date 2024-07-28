import discord
import mcstatus
from discord.ext import commands
import logging
import os
import socket

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Установите префикс команд
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.tree.command(name="ping", description="Get Minecraft server information")
async def ping(interaction: discord.Interaction, server_ip: str, server_port: int = 25565):
    if server_ip.lower() == "your.ip.net":
        embed = discord.Embed(title=f'Ошибка', color=0x7A288A)
        embed.description = f"Нельзя использовать адрес `{server_ip}`. Этот айпи находится в вайтлисте бота"
        await interaction.response.send_message(embed=embed)
        return

    try:
        # Resolve the domain name to an IP address
        numerical_ip = socket.gethostbyname(server_ip)
        is_valid_ip = True
    except socket.error:
        is_valid_ip = False

    if not is_valid_ip:
        embed = discord.Embed(title=f'Ошибка', color=0x7A288A)
        embed.description = f"Невозможно подключиться к серверу по адресу `{server_ip}`. Пожалуйста, введите корректный IP-адрес."
        await interaction.response.send_message(embed=embed)
        return

    try:
        # Получаем информацию о сервере
        server = mcstatus.JavaServer.lookup(f"{numerical_ip}:{server_port}")
        status = server.status()

        # Define the server_ip_with_port variable
        server_ip_with_port = f"{numerical_ip}:{server_port}"

        # Создаем embed сообщение
        embed = discord.Embed(title=f'Информация о сервере', color=0x7A288A)
        embed.add_field(name="Айпи: 🌐", value=server_ip_with_port, inline=False)
        embed.add_field(name="Игроки: 👥", value=f"{status.players.online}/{status.players.max}", inline=False)
        embed.add_field(name="Версия: 🛠️", value=f"{status.version.name} ({status.version.protocol})", inline=False)
        embed.add_field(name="Пинг: 📶", value=f"{status.latency} ms", inline=False)
        embed.set_footer(text=f"eclipse squad - {server_ip_with_port} 🌟")

        # Создаем новый файл motd для каждого запроса
        motd = status.description
        motd_file = f"motd_{server_ip}.txt"
        with open(motd_file, "w", encoding="utf-8") as file:
            file.write(motd)

        # Отправляем embed сообщение и файл motd
        await interaction.response.send_message(embed=embed, file=discord.File(motd_file))

        # Удаляем файл motd после отправки
        os.remove(motd_file)

    except Exception as e:
        await interaction.response.send_message(f"Не удалось получить данные сервера: {e}")

# Запуск бота
bot.run('YOUR_BOT_TOKEN')
