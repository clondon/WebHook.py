import json # Required because JSON format is used to send the rebuild request
import urllib.request  # Required to send the webhook ID via POST to the amplify instance for revuild

def lambda_handler(event, context):
    url = 'https://webhooks.amplify.eu-west-1.amazonaws.com/prod/webhooks'   #  Instance regional webhooks endpoint
    params = {
        'id': 'xxxxxxxxxxxxxxxxxxxxxxxxx',  # Amplify Build instance ID
        'token': 'rxxxxxxxxxxxxxxxxxxxxxxxxxx' # Amplify build instance token
    }

    # Create a dictionary for the URL
    # This will be packaged into a Python dictionary and sent using URLLIB as a \POST
    url_dict = {
        'url': url,
        'params': params
    }

    # Convert the dictionary to JSON and encode it
    data = json.dumps(url_dict).encode('utf8')

    headers = {
        'Content-Type': 'application/json'
    }

    # package the URL and it';s query parameters 
    query_params = urllib.parse.urlencode(params)
    full_url = f"{url}?{query_params}"

    request = urllib.request.Request(
        full_url,
        data=data,
        headers=headers
    )

    response = urllib.request.urlopen(request)

    return response.read()
  
  
 # Not required for Lambda but used if sent from another environment

if __name__ == "__main__":
    event = {}
    context = {}
    response = lambda_handler(event, context)
    print(response)
    
  
