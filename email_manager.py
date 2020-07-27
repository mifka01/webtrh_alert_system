import requests
import os 
import json
from message import message_text
from access_token import ACCESS_TOKEN
from conf import login_data


def get_emails_to_send():
    response = requests.get('https://api.pushbullet.com/v2/pushes',
                            headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 'Content-Type': 'application/json'})
    
    json_data = json.loads(response.text)

    json_data.keys()
    last_pushes = [push for push in json_data['pushes'][:10] if push['active']]
    send_messages = [push for push in last_pushes if push['body'][-6:] == "..mail"]


    emails_to_send = []
    for send_message in send_messages:
        symbol = send_message['body'][-10:4]
        for push in last_pushes:
            if symbol == push['body'][-4:]:   
                print(symbol)
                emails_to_send.append({
                'recipient': push['body'].splitlines()[1],
                'title': push['body'].splitlines()[0],
                'iden': push['iden'],
                'resp_iden': send_message['iden']
                })
    return emails_to_send

def send_email(recipient, title, message):
    email_data = {
        "recipients": recipient,
        'bccrecipients': None,
        'title': f'Re: {title}',
        'message': message,
        'sbutton': 'Odeslat příspěvek',
        's': None,
        'securitytoken': 'saVvI-iULN8S7fKTSSWC5DNreJ3KUxor1-jLkZ8c9OjHGLU_7gMi0-y1WSDF5dMA1-B9L8nHb_bo',
        'receipt': 0,
        'savecopy': 1,
        'signature': 0,
        'parseurl': 1,
        'disablesmilies': 1,
        'do': 'insertpm',
        'pmid': None,
        'forward': None,
    }


    with requests.Session() as session:
        session.post("https://webtrh.cz/login.php?do=login", data=login_data)
        resp = session.post('https://webtrh.cz/private.php?do=insertpm&pmid=', data=email_data)
    
    session.close()



