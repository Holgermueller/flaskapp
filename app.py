from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from googleapiclient import discovery
import json
import math

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

        comment_to_rate = request.form['input']
       

        analyze_request = {
            'comment': {'text': 'comment_to_rate'},
            'requestedAttributes': {'TOXICITY': {},
            # 'SEVERE_TOXICITY':{},
            # 'IDENTITY_ATTACK':{},
            # 'INSULT':{},
            # 'PROFANITY':{},
            # 'THREAT':{}
            },
        }

        response = client.comments().analyze(body=analyze_request).execute()
        print(json.dumps(response, indent=2))

        result_from_json = response['attributeScores']['TOXICITY']['summaryScore']['value']

        result_to_percentage = math.ceil(result_from_json * 100)


        return render_template('index.html', result=result_to_percentage, comment_to_rate=comment_to_rate)



if __name__ == "__main__":
    app.run()