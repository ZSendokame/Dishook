import requests

def check(request_object):
    if request_object.status_code >= 400:
        raise Exception(
            f'{request_object.url} returned ' \
            f'{request_object.status_code}, {request_object.reason}.'
        )

class Webhook():
    def __init__(self, webhook):
        self.status = 204
        self.response = ''
        self.webhook = webhook
        self.json = dict()

    def get_information(self):
        response = requests.get(self.webhook)

        check(response)
        return response.json()

    def modify_configuration(self, **kwargs):
        response = requests.patch(self.webhook, json=kwargs)

        check(response)
        return response.json()

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

        check(response)
        return True