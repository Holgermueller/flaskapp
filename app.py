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

API_KEY = os.getenv('api_key')

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_data_from_form():
    if request.method == 'POST':
        client = discovery.build(
        "commentanalyzer",
        "v1alpha1",
        developerKey=API_KEY,
        discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
        static_discovery=False,
        )

        comment_to_rate = request.form['input']
       
        analyze_request = {
            'comment': {'text': comment_to_rate},
            'requestedAttributes': {'TOXICITY': {},
            'SEVERE_TOXICITY':{},
            'IDENTITY_ATTACK':{},
            'INSULT':{},
            'PROFANITY':{},
            'THREAT':{}
            },
        }

        response = client.comments().analyze(body=analyze_request).execute()
        print(json.dumps(response, indent=2))

        toxicity_result_from_json = response['attributeScores']['TOXICITY']['summaryScore']['value']

        toxicity_result_to_percentage = math.ceil(toxicity_result_from_json * 100)

        severe_result_from_json = response['attributeScores']['SEVERE_TOXICITY']['summaryScore']['value']

        severe_result_to_precentage = math.ceil(severe_result_from_json * 100)

        identity_result_from_json = response['attributeScores']['IDENTITY_ATTACK']['summaryScore']['value']

        identity_result_to_precentage = math.ceil(identity_result_from_json * 100)

        insult_result_from_json = response['attributeScores']['INSULT']['summaryScore']['value']

        insult_result_to_precentage = math.ceil(insult_result_from_json * 100)

        profanity_result_from_json = response['attributeScores']['PROFANITY']['summaryScore']['value']

        profanity_result_to_precentage = math.ceil(profanity_result_from_json * 100)

        threat_result_from_json = response['attributeScores']['THREAT']['summaryScore']['value']

        threat_result_to_precentage = math.ceil(threat_result_from_json * 100)



        return render_template('index.html', toxicity_result=toxicity_result_to_percentage,
        insult_result=insult_result_to_precentage,
        comment_to_rate=comment_to_rate,
        severe_result=severe_result_to_precentage, 
        identity_result=identity_result_to_precentage,
        profanity_result=profanity_result_to_precentage,
        threat_result=threat_result_to_precentage )



if __name__ == "__main__":
    app.run()