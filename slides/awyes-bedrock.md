
<!--
theme: custom
class: invert
size: 4:3
-->


<style>
  section {
    background-color: #000;
    background-image: url(img/build-logo.svg);
    background-size: 200px 100px;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: bottom left; 
}
</style>
<!-- -->

## AWyeS Labs - Building GenAI demos with AWS Bedrock and Gradio

---

# Why?

"I had some doubts going into this, but looks like GenAI is the real deal"
-- Build Chicago Engineer

---

# Goal

- Create a quick demo that interact with AWS Bedrock using Python and Gradio

---

# Ground rules

  - There is no rules, please explore at wish
  - It is OK to play with prompt and do your own experimentation

---

## What's GenAI

Generative artificial intelligence is artificial intelligence capable of generating text, images, or other media, using generative models.

The current form of GenAI is based in Deep Learning which is based on Neural Networks which were invented in 1958. But they are based in techniques from 1800's.

---

## What's AWS Bedrock?

Amazon Bedrock is a fully managed service that makes large language models (LLMs) from leading AI companies available through a single application programming interface (API)

---

## What's Gradio?

Gradio is an open-source Python package that allows you to develop demos for machine learning applications

---

## What will we be doing?

#### Data genius demo
- Summary of a legacy code
- Convert code to python
- Confidence of the conversion (time permitting)

![bg right width:450px](img/data-genius.png)

---

## Requirements

- Access to InnovationLabs (aws.slalom.com)
- `aws-azure-login` installed and configured
- Download repo

---

## For `aws-azure-login` follow this guide

https://slalom.service-now.com/help?id=kb_article&table=kb_knowledge&sysparm_article=KB0015023

![bg right width:450px](img/qr-login.png)

---

## Download {repo}


---

## 1.- Call Bedrock service

---

## AWS Bedrock Playground

---

## TODO: Call Bedrock from our code

---

## TODO: Snippet empty gradio

---

## TODO: Craft prompt for Summary

#### Example:

```
I want you to act as a software engineer who is analyzing a legacy source code.
The goal is for you to identify the source code language, and explain on a high level what is the purpose of the program.
You will follow this following template replacing {programming_language} and {description}
 with your output. Do not output anything that is not a template.
Do not attempt to give explanations. Surround your answer with ` ` `

Programming language: {programming_language}
Description: {description}

Here is an example:
input: (define power (lambda (x, n) (if (= n 0) 1 (* x (expt x (- n 1))))))
output:
` ` `
Programming language: Scheme
Description: The program creates a function in Scheme to calculate recursively the power of a number
` ` `

input: {input}
```

---

## Put it all together

---

# testing

```python
print('hello world')
```


---

```
print ("hello")
```


## Let's jump into it:
- Check that you have access to AWS 
![bg right 25%](https://github.com/marp-team.png)
