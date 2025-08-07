# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()

# testing out gradio

# importing gradio
import gradio as gr

# making the function to use for the "fn" argument
def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

# using the Interface class
demo = gr.Interface(
    # fn: "the function to wrap a user interface (UI) around"
    fn = greet,
    # inputs: "the Gradio component(s) to use for the
    # input. The number of components should match the number of
    # arguments in your function."
    inputs = ["text","slider"],
    # outputs: "the Gradio component(s) to use for the output.
    # The number of components should match the number of
    # return values from your function."
    outputs = ["text"],
)



demo.launch(share=True) # using share=True to make a public URL for sharing

# More notes:
# "Custom Demos with gr.Blocks"
# "Chatbots with gr.ChatInterface"
# "You can also build Gradio applications without writing any code.
#  Simply type gradio sketch into your terminal to open up an editor
#  that lets you define and modify Gradio components, adjust their
#  layouts, add events, all through a web editor. "