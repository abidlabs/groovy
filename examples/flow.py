import gradio as gr

import groovy as gv

flow = gv.Flow("navigate to {}", [gr.Textbox("hf.co")])

if __name__ == "__main__":
    flow.launch()
