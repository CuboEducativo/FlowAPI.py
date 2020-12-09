import hmac
import hashlib
import json


def parseToStringDictionary(dictionary):
    new_dict = {}
    for key in sorted(dictionary.keys()):
        if isinstance(dictionary[key], str):
            new_dict[key] = dictionary[key]
        else:
            str_value = json.dumps(dictionary[key])
        new_dict[key] = str_value
    return new_dict


def stringToSign(_dictionary):
    dictionary = parseToStringDictionary(_dictionary)
    string = ""
    for key in sorted(dictionary.keys()):
        if isinstance(dictionary[key], str):
            string += key + dictionary[key]
    return string


def signParams(secret_key, params):
    message = stringToSign(params)
    signature = hmac.new(
        bytes(secret_key, 'latin-1'),
        msg=bytes(message, 'latin-1'),
        digestmod=hashlib.sha256
        ).hexdigest()
    return signature
