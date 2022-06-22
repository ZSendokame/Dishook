# Dishook
**Dishook** it's a library who lets you controll Discord Webhooks via HTTP.<br>
Supports plain text and embeds, Parameters and JSON gives you more controll than other libraries.<br>
Dishook it's one of the lasts Discord webhook controll library that is mantained today.

# How to install
```
pip install git+https://github.com/ZSendokame/Dishook
```

# How to use
After download, here is a brief tutorial.<br>
```py
import dishook

webhook = dishook.Webhook(Webhook URL) # Create a Webhook() object, this class do all the work.

webhook.embed(
    description='This is a description',
    color=10000,
    image={
        'url': 'Image URL'
    }
)

webhook.send() # Here, you can add the parameters you wan't!. First check that they are valid.

# You also have some values!
webhook.json     # In case you have any error, you can check the generated JSON that the library sent.
webhook.response # More descriptive, if there's any error. Do a try-except and check discord's response (Here is the error.).
webhook.status   # Here is status code, if you search for it. Probably you will get information
```