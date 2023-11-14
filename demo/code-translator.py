import gradio as gr
import boto3
import json

"""
We are now going to put everything together. 

Below, there is a code that creates a gradio interface, makes a call to Anthropic Claude model through Amazon Bedrock,
and will ask the model to have a summary of what the original code uses.

"""

br = boto3.client(service_name="bedrock-runtime", region_name="us-west-2")

prompt_template  = """Human: \\n\\nHuman: You are a software engineer that assist me in understanding source code and 
providing a nice summary of what the code does. Please identify the programming language and provide a summary of the following code:  
{code}
\\n\\nAssistant:"""


def get_code_summary(source_code):
    myprompt = prompt_template.format(code=source_code)  
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
    
    return response_body.get('completion')

demo = gr.Interface(fn=get_code_summary, inputs="text", outputs="text", allow_flagging= 'never')
demo.launch()


"""

Try running the code. Remember to renew the SSO token using aws-azure-login script before running this.
You can use any code from any language, but also you could try with:
(define mystery (lambda (x) (* x x x)))

- Exercise: Modify the code to include another call to our LLM and ask to translate the source code to Python and show the output
using a Code textbox (https://www.gradio.app/docs/code)

"""