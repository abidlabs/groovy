from pathlib import Path

import gradio as gr
from gradio.themes.utils import colors

from groovy.app_utils import add_step_counter
from groovy.types import Image, StepMessage, raw_value_to_step_message

theme = gr.themes.Base(
    primary_hue="purple",
)

theme.set(
    button_cancel_background_fill=colors.red.c500,
    button_cancel_background_fill_dark=colors.red.c700,
    button_cancel_background_fill_hover=colors.red.c600,
    button_cancel_background_fill_hover_dark=colors.red.c800,
)


def create_app(self, inputs, prompt, streamer, run_immediately, save_recording):
    with gr.Blocks(theme=theme) as app:
        with gr.Accordion(
            "Input parameters (used to construct the task)",
            open=True,
            visible=bool(inputs),
        ) as inputs_accordion:
            for input in inputs:
                input.render()

        with gr.Group():
            prompt_box = gr.Textbox(label="🕺 Constructed Task", value=prompt)
            with gr.Row():
                run_button = gr.Button("Start Flow", variant="primary")
                stop_button = gr.Button("Stop Flow", variant="stop", visible=False)

        chat_log = gr.Chatbot(
            label="Log",
            type="messages",
            group_consecutive_messages=False,
            visible=False,
        )

        @gr.on(
            triggers=[app.load] + [input.change for input in inputs],
            inputs=inputs,
            outputs=[prompt_box],
            trigger_mode="always_last",
        )
        def construct_prompt(*input_values):
            return prompt.format(*input_values)

        run_triggers = [run_button.click]
        if run_immediately:
            run_triggers.append(app.load)

        def run_flow_ui_changes():
            return {
                run_button: gr.Button(value="Running...", interactive=False),
                chat_log: gr.Chatbot(visible=True, type="messages"),
                inputs_accordion: gr.Accordion(open=False),
            }

        def reset_ui():
            return {
                run_button: gr.Button(value="Start Flow", interactive=True),
                inputs_accordion: gr.Accordion(open=True, visible=bool(inputs)),
            }

        def run_flow(prompt):
            chat_messages = [gr.ChatMessage(content=prompt, role="user")]
            yield chat_messages

            images_for_gif = []

            for step_message in streamer(prompt):
                if not isinstance(step_message, StepMessage):
                    step_message = raw_value_to_step_message(step_message)
                chat_messages.append(step_message.as_chat_message())

                # Any returned gv.Image messages are automatically added to the recording
                if (
                    isinstance(step_message, Image)
                    and step_message.save_in_recording
                    and save_recording
                ):
                    img_with_text = add_step_counter(
                        step_message.value, len(images_for_gif) + 1
                    )
                    images_for_gif.append(img_with_text)
                    if len(images_for_gif) > 0:
                        gif_dir = Path.cwd() / ".groovy"
                        gif_dir.mkdir(exist_ok=True)
                        gif_path = gif_dir / "recording.gif"
                        images_for_gif[0].save(
                            gif_path,
                            save_all=True,
                            append_images=images_for_gif[1:],
                            duration=500,
                            loop=0,
                        )
                yield chat_messages

        gr.on(
            fn=run_flow_ui_changes,
            triggers=run_triggers,
            outputs=[run_button, stop_button, chat_log, inputs_accordion],
        ).then(
            fn=run_flow,
            inputs=[prompt_box],
            outputs=[chat_log],
        ).then(
            fn=reset_ui,
            outputs=[run_button, stop_button, chat_log, inputs_accordion],
        )

    return app
