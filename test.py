#import requests
from dotenv import load_dotenv
import os

def config():
    load_dotenv()

config()

print (os.getenv('api_key'))
