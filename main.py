from telethon import TelegramClient, events
from discord_webhook import DiscordWebhook

api_id = 10294483
api_hash = 'feef69d0322a4b4bd08f50f2e028903d'

my_channel_id = '-1696108040'
channels = [my_channel_id]

client = TelegramClient('Sunblogs', api_id, api_hash)
print("TeleDis запущен")


@client.on(events.NewMessage())
async def my_event_handler(event):
    webhook = DiscordWebhook(
        url='https://discord.com/api/webhooks/1008034602360778822/z9CBESdQFb28f_MSR0B1OaT3fpb5l9_dAMMbdh-7z70EruttvxsNzt4zoONvpJyJkWyl',
        content=event.message.text)
    response = webhook.execute()


client.start()
client.run_until_disconnected()
