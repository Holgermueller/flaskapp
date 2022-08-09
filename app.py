from urllib import request
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from googleapiclient import discovery
import json

app = Flask(__name__)

def config():
    load_dotenv()

config()

api_key = os.getenv('api_key')

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_data_from_form():
    if request.method == 'POST':

        client = discovery.build(
        "commentanalyzer",
        "v1alpha1",
        developerKey=api_key,
        discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
        static_discovery=False,
        )

        # analyze_request = {
        # 'comment': { 'text': 'friendly greetings from python' },
        # 'requestedAttributes': {'TOXICITY': {}}
        # }

        analyze_request = {
            'comment': {'text': 'request.form'},
            'requestedAttributes': {'TOXICITY': {}}
        }

        response = client.comments().analyze(body=analyze_request).execute()
        print(json.dumps(response, indent=2))

        result = response
        return render_template('index.html', result=result)



if __name__ == "__main__":
    app.run()