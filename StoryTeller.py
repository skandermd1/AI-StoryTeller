from ibm_watsonx_ai import Credentials
import os

credentials = Credentials(
    url="https://us-south.ml.cloud.ibm.com",
    )

project_id="skills-network"
from ibm_watsonx_ai import APIClient

client = APIClient(credentials)
# GET TextModels ENUM
client.foundation_models.TextModels

# PRINT dict of Enums
client.foundation_models.TextModels.show()
model_id = 'mistralai/mistral-large'
import os
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams


params = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 1000,
}

model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=project_id,
    params=params,
)
# Function to generate an educational story using the Mistral model
def generate_story(topic):
    # Construct a detailed prompt that guides the model to:
    # - Write for beginners
    # - Use simple language
    # - Include interesting facts
    # - Keep a specific length
    # - End with a summary
    prompt = f"""Write an engaging and educational story about {topic} for beginners. 
            Use simple and clear language to explain basic concepts. 
            Include interesting facts and keep it friendly and encouraging. 
            The story should be around 200-300 words and end with a brief summary of what we learned. 
            Make it perfect for someone just starting to learn about this topic."""
    
    # Generate text using the model with our carefully crafted prompt
    response = model.generate_text(prompt=prompt)
    return response

# Example usage of the generate_story function
# Here we use butterflies as a topic since it's an engaging and 
# educational subject that demonstrates the function well
topic = "the life cycle of butterflies"
story = generate_story(topic)
print("Generated Story:\n", story)
from gtts import gTTS
from IPython.display import Audio
import io

# Initialize text-to-speech with the generated story
tts = gTTS(story)

# Save the audio to a bytes buffer in memory
audio_bytes = io.BytesIO()
tts.write_to_fp(audio_bytes)
audio_bytes.seek(0)

# Create and display an audio player widget in the notebook
Audio(audio_bytes.read(), autoplay=False)
# Save as MP3 file
tts.save("generated_story.mp3")

