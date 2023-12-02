import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	
	return response.json()
	
output = query({
	"inputs": {
		#"past_user_inputs": ["Which movie is the best ?"],
		#"generated_responses": ["It is Die Hard for sure."],
		"text": "How are you ? "
	},
})

print(output)

