import json
import urllib.request

def lambda_handler(event, context):
    r = urllib.request.Request(
        'https://....amazonaws.com/prod/webhooks?id=...&token=...&operation=startbuild',
        data=json.dumps({}).encode('utf8'),
        headers={
            'Content-Type': 'application/json'
        },
        method='POST'
    )
    urllib.request.urlopen(r)
    return
