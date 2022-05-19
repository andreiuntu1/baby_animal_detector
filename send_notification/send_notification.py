import requests
import json

def _pushbullet_message(title, body):
    msg = {"type": "note", "title": title, "body": body}
    TOKEN = 'o.jd62vHJjpoH32eCL0GnC1n2ILJRsCslS'
    resp = requests.post('https://api.pushbullet.com/v2/pushes',
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Error',resp.status_code)
    else:
        print ('Message sent')

def main(title, text):
    _pushbullet_message(title, text)

if __name__ == '__main__':
    main()