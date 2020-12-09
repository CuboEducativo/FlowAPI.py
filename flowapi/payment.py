import requests
import helpers


class Payment:
    def __init__(self, api_key, secret_key, api_url='https://www.flow.cl/api'):
        self.api_key = api_key
        self.secret_key = secret_key
        self.api_url = api_url

    def signParams(self, params):
        return helpers.signParams(self.secret_key, params)

    def get_status(self, token):
        params = {
            'apiKey': self.api_key,
            'token': token
        }
        params['s'] = self.signParams(params)
        status = requests.get(
          '{}/payment/getStatus'.format(self.api_url),
          params=params
          )
        return status.json()

    def create(self, params):
        params = helpers.parseToStringDictionary(params)
        params['apiKey'] = self.api_key
        params['s'] = self.signParams(params)
        response = requests.post(
          '{}/payment/create'.format(self.api_url),
          data=params)

        return response.json()

    def get_status_by_commerce_id(self, commerce_id):
        params = {
            'apiKey': self.api_key,
            'commerceId': commerce_id
        }
        params['s'] = self.signParams(params)
        status = requests.get(
          '{}/payment/getStatusByCommerceId'.format(self.api_url),
          params=params
          )
        return status.json()
