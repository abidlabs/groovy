import gradio as gr

def create_app(self, inputs, prompt, runner, _run_immediately):
    with gr.Blocks() as app:
        with gr.Tabs() as tabs:
            with gr.Tab("Setup"):
                for input in inputs:
                    input.render()

                prompt_box = gr.Textbox(label="Prompt", value=prompt)
                run_button = gr.Button("Run", variant="primary")

                @gr.on(triggers=[app.load] + [input.change for input in inputs], inputs=inputs, outputs=[prompt_box], trigger_mode="always_last")
                def construct_prompt(*input_values):
                    return prompt.format(*input_values)
                
            # with gr.Tab("Flow", id="flow", visible=False) as results_tab:
            #     chat_log = gr.Chatbot(label="Log")
            #     stop_button = gr.Button("Stop", variant="stop")

        run_triggers = [run_button.click]
        if _run_immediately:
            run_triggers.append(app.load)

        @gr.on(triggers=run_triggers, inputs=[prompt_box])
        def run_flow(prompt):
            # yield gr.Tabs(selected="flow"), gr.Tab(visible=True)
            runner(prompt)


    return app
