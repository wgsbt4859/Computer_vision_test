from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import json

with open("secret.json") as f:
    secret = json.load(f)

KEY = secret["KEY"]
ENDPOINT = secret["ENDPOINT"]

'''
Authenticate
Authenticates your credentials and creates a client.
'''
computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

'''
END - Authenticate
'''

def get_tags(filepath):
    local_image = open(filepath, "rb")

    image_features = ["Tags"]
    tag_results = computervision_client.analyze_image_in_stream(local_image, image_features) #_instreamを忘れないようにする！

    tags = tag_results.tags
    tags_name=[]

    for tag in tags:
        tags_name.append(tag.name)
    return tags_name

def detect_objects(filepath):

    local_image = open(filepath, "rb")

    detect_objects_results = computervision_client.detect_objects_in_stream(local_image)

    objects = detect_objects_results.objects

    return objects

import streamlit as st

st.title