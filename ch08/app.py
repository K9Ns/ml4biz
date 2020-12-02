from chalice import Chalice
import json
import boto3
from slugify import slugify
# from blingfire import text_to_words

app = Chalice(app_name='tweet_escalator')

@app.route('/')
def index():
    return 'Hello world!'


@app.route('/tweet/{tweet}')
def return_tweet(tweet):
    tokenized_tweet = [slugify(tweet, separator=' ')]
    payload = json.dumps({"instances" : tokenized_tweet})

    endpoint_name = 'customer-support-slugify'

    runtime = boto3.Session().client(service_name='sagemaker-runtime', region_name='us-east-1')

    response = runtime.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/json', Body=payload)

    response_list = json.loads(response['Body'].read().decode())
    response = response_list[0]

    if '1' in response['label'][0]:
        escalate = 'Yes'
    else:
        escalate = 'No'

    full_response = {
        'Tweet': tweet,
        'Tokenised tweet': tokenized_tweet,
        'Escalate': escalate,
        'Confidence': response['prob'][0]
    }
    return full_response


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
