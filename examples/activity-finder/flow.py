import gradio as gr

import groovy as gv

flow = gv.Flow(
    # task="Find me some events in San Francisco related to board games using Meetup.",
    task="Find me some events in {} related to {} using Meetup.",
    inputs=[
        gr.Dropdown(
            ["San Francisco", "New York", "Chicago", "Los Angeles", "Boston"],
            allow_custom_value=True,
        ),
        gr.Dropdown(
            ["board games", "cooking", "hiking", "reading", "writing"],
            allow_custom_value=True,
        ),
    ],
)

if __name__ == "__main__":
    flow.launch()
