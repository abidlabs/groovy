import groovy as gv
import gradio as gr

flow = gv.Flow("navigate to {}", [gr.Textbox("hf.co")])

if __name__ == "__main__":
  flow.launch()
