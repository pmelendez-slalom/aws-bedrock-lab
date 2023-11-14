import gradio as gr

def process_input(input_value):
    return f"my output is: {input_value}"

demo = gr.Interface(fn=process_input, inputs="text", outputs="text")
demo.launch()

"""
Exercise:
- Try adding allow_flagging="never" as a parameter for Interface
- Try changing inputs to an array and add a second text element
- Try doing the same for outputs
- Consider that inputs can be expressed as object instances:
    - e.g. gr.Textbox(label="Input 1")
    Change the interface object so it would receive an object as an input
"""
