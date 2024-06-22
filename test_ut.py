# a test file to test the image fetch

import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('KEY')
response = openai.images.generate(
  model="dall-e-3",
  prompt="a mountain house with serene scenery",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(image_url)

