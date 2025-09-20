# NOTES : RUN ONLY ONE CODE AT A TIME..

# to check torch work properly
import torch
print(torch.__version__)

# to check gradio work properly
import gradio as gr
def work(InpuT):
    return 'Gradio is working perfectly..'
demo = gr.Interface(fn=work,inputs=gr.Textbox(placeholder='Type Anything...')
    ,outputs=gr.Textbox(),
    title = 'TESTING',
    description = 'to check whether gradion is working on your pc')
demo.lauch(share=True)

# to check transformer and langchain work perfectly
from transformers import pipeline
model = pipeline(task='sentiment-analysis',model='GIVE ANY MODEL NAME')
response= model('I am happy today.')
print(response[0]['label'])
