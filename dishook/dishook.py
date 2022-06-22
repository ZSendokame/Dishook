import requests

class Webhook():
    def __init__(self, webhook):
        self.status = 204
        self.response = ''
        self.webhook = webhook
        self.json = {}

    def embed(self, **kwargs):
        self.json['embeds'] = [
            {
                **kwargs
            }
        ]

    def send(self, **kwargs):
        self.json.update(kwargs)

        response = requests.post(
            self.webhook,
            json=self.json
        )

        self.status = response.status_code
        self.response = response.content

        if self.status == 401:
            raise Exception(f'{self.webhook} Is not valid webhook URL.')

        elif self.status == 400:
            raise Exception(
                f'Discord couldn\'t understand the JSON ' \
                f'that you sent, you can check it using the "json" variable.'
            )

        return True