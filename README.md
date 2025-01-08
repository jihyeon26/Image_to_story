# IMS prototype

This project extracts GPS data from images, converts it into location information, analyzes the image content, and generates a travel log using GPT. This repository is a prototype version of IMS, the second project by the 5th cohort of the Microsoft AI School. It differs slightly from the final version.

This project won **1st place** among the 10 teams in the second project.

1. **EXIF Metadata Extraction**: Extracts GPS metadata from image files.
2. **Location Conversion**: Converts GPS coordinates into address information.
3. **Vision Analysis**: Uses Azure Computer Vision to analyze the visual content of images and create descriptive prompts.
4. **GPT Travel Log Generation**: Generates travel logs using Azure Open AI, based on image content and location information.

## Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/jihyeon26/Image_to_story.git
```

2. **Set Up Environment Variables**: Create a .env file in the project root directory and add the following information.
```
GPT_ENDPOINT=<Your GPT Endpoint>
GPT_API_KEY=<Your GPT API Key>
VISION_ENDPOINT=<Your Vision Endpoint>
VISION_KEY=<Your Vision Key>
```

3. **Run the Main Script**:

- Update the image_path variable in main.py to your desired image file path.

- Execute the script:
```bash
python main.py
```

## Project Structure

```project/
│
├── EXIF_extract.py           # Module for extracting GPS metadata from images
├── EXIF_to_location.py       # Module for converting GPS data into address information
├── request_gpt.py            # Module for interacting with GPT to generate travel logs
├── computer_vision.py        # Module for generating image captions
├── main.py                   # Main script to run the entire pipeline
└── .env                      # Environment variables file (not included in the repository)
```

## Notes
    - Please use images that include GPS metadata.