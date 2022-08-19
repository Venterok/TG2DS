import os
import random
import shutil

import pyimgur
from colorthief import ColorThief
from discord_webhook import DiscordWebhook, DiscordEmbed
from telethon import TelegramClient, events, utils

api_id = 'api_id'   # Client Telegram api_id
api_hash = 'api_hash'  # Client Telegram api_hash
CLIENT_ID = 'CLIENT_ID'  # Imgur Client ID

channels = {
    1696108040: [
        'webhook-link',
        'telegram-channel-link',
        'telegram-channel-avatar'],
    1360155440: [
        'webhook-link',
        'telegram-channel-link',
        'telegram-channel-avatar']
}

client = TelegramClient('telegramClientName', api_id, api_hash)


def rgbttohex(colortuple):
    return ''.join(f'{i:02X}' for i in colortuple)


@client.on(events.NewMessage())
async def my_event_handler(event):
    # Getting settings from dict
    channeldata = channels[event.message.peer_id.channel_id]
    webhook = DiscordWebhook(url=channeldata[0])
    # Random Hex Color
    hexcolor = "{:06x}".format(random.randint(0, 0xFFFFFF))  # TODO Hex color from image

    # Get Chat Name
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)

    # Set text to embed
    embed = DiscordEmbed(description=event.message.text + "\n\n" + channeldata[1])

    # If message contain photo
    if event.photo:
        saved_path = await event.download_media('temp')
        PATH = saved_path

        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
        embed.set_image(url=uploaded_image.link)

        # Dominant Color of image
        dominantcolor = ColorThief(saved_path)
        dominant_color = dominantcolor.get_color(quality=1)

        embed.set_color(rgbttohex(dominant_color))
    else:
        embed.set_color(hexcolor)

    # If author & footer & timestamp
    embed.set_footer(text=chat_title, icon_url=channeldata[2])
    embed.set_author(name='Новый постs!')
    embed.set_timestamp()

    # Send this shit
    webhook.add_embed(embed)
    response = webhook.execute()

    # Clear all files in package temp
    folder = 'temp'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


client.start()
client.run_until_disconnected()
