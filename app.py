import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import gradio as gr

# Load Stable Diffusion pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)

# Move the model to GPU
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Logo generation function
def generate_logo(company_name, industry, colors):
    prompt = f"A professional logo for {company_name} in the {industry} industry with colors {colors}"
    image = pipe(prompt).images[0]
    return image

# Define the Gradio interface
iface = gr.Interface(
    fn=generate_logo,
    inputs=[
        gr.Textbox(label="Company Name"),
        gr.Textbox(label="Industry"),
        gr.Textbox(label="Preferred Colors")
    ],
    outputs=gr.Image(type="pil"),
    title="AI Logo Generator",
    description="Enter company name, industry, and preferred colors to generate a logo using AI (Stable Diffusion)."
)

# Launch the interface
if __name__ == "__main__":
    iface.launch(share=True)
