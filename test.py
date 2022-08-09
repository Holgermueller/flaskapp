#import requests
from dotenv import load_dotenv
import os
from googleapiclient import discovery
import json

def config():
    load_dotenv()

config()

api_key = os.getenv('api_key')


client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=api_key,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

analyze_request = {
  'comment': { 'text': 'friendly greetings from python' },
  'requestedAttributes': {'TOXICITY': {}}
}

response = client.comments().analyze(body=analyze_request).execute()
print(json.dumps(response, indent=2))