from transformers import pipeline
import gradio as gr

def sentimentAnalysis(sentence):
    model = pipeline(task = 'sentiment-analysis',model = 'distilbert/distilbert-base-uncased-finetuned-sst-2-english')
    response = model(sentence)
    return response[0]['label'] #as the response is a list of one dictionary..




demo = gr.Interface(fn=sentimentAnalysis,
                    inputs=gr.Textbox(label='Write your thoughts here' ,placeholder='Ex : I am happy today.'),
                    outputs=gr.Textbox(label='Analysis'),
                    title = 'SENTIMENT ANALYSIS',
                    description = 'This will tell you whether your thought is positive thought or negative thought.')
demo.launch(share=True)




