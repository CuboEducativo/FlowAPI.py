from flowapi.payment import Payment


class FlowAPI:
    def __init__(self, api_key, secret_key, api_url='https://www.flow.cl/api'):
        self.payment = Payment(api_key, secret_key, api_url)
