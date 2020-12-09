# FlowAPI.py

## Usage

```py
import FlowAPI from FlowAPI

FLOW_API_KEY = "YOUR_API_KEY"
FLOW_SECRET_KEY = "YOUR_SECRET_KEY" # get this in a secure way, don't hardcode it please

api = FlowAPI(FLOW_API_KEY,FLOW_SECRET_KEY)

payment = api.payment.create({
  'email':  "example@sdada.com",
})

```
