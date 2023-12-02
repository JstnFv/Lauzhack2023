import requests
from flask import Flask, request, Response
from scihub import SciHub
import os
import re
import random
import json
import datetime
from bs4 import BeautifulSoup
from pyzotero import zotero
#from google.cloud import texttospeech as tts
import wave
import langchain
import torch
from transformers import AutoModel, AutoTokenizer
import numpy as np
from typing import Sequence
import openai
import matplotlib.pyplot as plt
from openai.embeddings_utils import get_embedding
import warnings
warnings.filterwarnings("ignore")
import langchain
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.python import PythonREPL
from langchain.chat_models import ChatOpenAI
from langchain.agents import tool
from datetime import date

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	
	return response.json()
	
output = query({
	"inputs": {
		"past_user_inputs": ["Which movie is the best ?"],
		"generated_responses": ["It is Die Hard for sure."],
		"text": "Can you explain why ?"
	},
})

print(output)


