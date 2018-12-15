import requests

def get_joke():
    r = requests.get('https://geek-jokes.sameerkumar.website/api')
    return r.text + ' Funny right ?'