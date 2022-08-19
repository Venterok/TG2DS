# TG2DS

> RU

Бот был написан для личных нужд так как не нашёл альтернатив. Для работы требуется > 

| Переменная       | Описание                                       | Получение  |
|------------------|------------------------------------------------|------------|
| API_ID           | App Api_id Telegram                            | [[Здесь]](https://my.telegram.org)|
| API_HASH         | App api_hash Telegram                          | [[Здесь]](https://my.telegram.org)|
| SHORT_NAME       | App Short name                                 | [[Здесь]](https://my.telegram.org)|
| BOT_TOKEN        | Токен бота для получения сообщений             | [[Здесь]](https://telegram.me/BotFather)|
| CLIENT_ID        | Токен IMGUR для фото                           | [[Здесь]](https://api.imgur.com/)|

Пока что всё указывается в main.py, чтобы бот получал сообщения из чата его нужно _**пригласить в чат**_. Сделать это вроде как можно только с мобильной версии Telegram. Дабы можно было разделить сообщения по нескольким чатам, было сделано что для каждого чата нужен webhook link, так что указывается всё это так >
```Python
channels = {
    1696108040: [ # ID Телеграм чата, я сам не понял как его получать, если нужно можно найти информацию в интернете
        'webhook-link', # Discord Webhook Link Куда бот будет отправлять сообщения.
        'telegram-channel-link', # Ссылка на чат телеграмма, можно не указывать если не нужно
        'telegram-channel-avatar'], # Изображение для Footer Webhook'а
    1360155440: [
        'webhook-link',
        'telegram-channel-link',
        'telegram-channel-avatar']
}
```

![Frame 42 1](https://user-images.githubusercontent.com/67825103/185559199-55a0e224-56cb-486b-bf27-7c3c2c7997ac.png)
