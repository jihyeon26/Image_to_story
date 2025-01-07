from EXIF_extract import get_gps_info  
from EXIF_to_location import get_location_from_gps_data
from request_gpt import request_gpt
from computer_vision import request_vision
import gradio as gr

def change_image(image_path, write_style, gender, companion):
    # Extract GPS information
    gps_data = get_gps_info(image_path)

    # Retrieve address information
    location = get_location_from_gps_data(gps_data)

    # Define prompt, location, and writing style
    prompt = request_vision(image_path)
   
    response = request_gpt(prompt, location, write_style, gender, companion)
    return response


# UI for gradio
with gr.Blocks() as demo:
    
    with gr.Row():
        gender_radio = gr.Radio(label="Please select your gender.", choices=["Male", "Female"], value="Male") 
    with gr.Row():
        companion_radio = gr.Radio(label="Who did you go with?", choices=["Alone", "With siblings", "With a partner", "With parents", "with friends", "others"], value="Alone")              
    with gr.Row():    
        write_style_radio = gr.Radio(label="Choose the tone of the writing.", choices=["Informative", "Emotional", "Poetic", "Letter style"], value="Informative")              
             
           
    with gr.Row():
        input_image = gr.Image(label="Input Image", type="filepath")
        result_text = gr.TextArea(label="Output text")


    input_image.change(fn=change_image, 
                       inputs=[input_image,  write_style_radio, gender_radio, companion_radio], 
                       outputs=[result_text])
    
demo.launch()