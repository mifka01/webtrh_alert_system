import requests
from access_token import ACCESS_TOKEN

def delete_message(iden):
    requests.delete(url=f"https://api.pushbullet.com/v2/pushes/{iden}",headers={'Access-Token':ACCESS_TOKEN})
