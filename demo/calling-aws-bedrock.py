import boto3
import json

br = boto3.client(service_name="bedrock-runtime", region_name="us-west-2")
myprompt = "Human: \\n\\nHuman: You are a helpful assistant that assist me in translating phrases to Spanish. My first phrase is: How do I eat?\\n\\nAssistant:"

body = {
    'prompt': myprompt,
    'max_tokens_to_sample': 1000,
    'temperature': 0.3,
    'top_k': 250,
    'top_p': 0.999,
    'stop_sequences': ["\\n\\nHuman:"],
    'anthropic_version': 'bedrock-2023-05-31'
}

kwargs = {
        "modelId": "anthropic.claude-v1",
        "contentType": "application/json",
        "accept": "*/*",
        "body": json.dumps(body)
        }

response = br.invoke_model(**kwargs)
response_body = json.loads(response.get('body').read())
print(response_body)

"""
Exercise: 
- Play with different values for temperature, and different prompts.
"""