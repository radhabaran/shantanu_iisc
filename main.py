import gradio as gr
from app import chatbot

iface = gr.Interface(
    fn=chatbot,
    inputs=["text", gr.State()],
    outputs=["text", gr.State()],
    title="🛍️ E-commerce Assistant",
    description="Ask about products, pricing, or general customer service queries."
)

if __name__ == "__main__":
    iface.launch()