
Storyteller readme · MD
Copier

# StoryTeller AI 🎙️📚

An AI-powered educational storytelling application that generates engaging stories on any topic and converts them to natural-sounding audio using IBM WatsonX and Google Text-to-Speech.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![IBM WatsonX](https://img.shields.io/badge/IBM-WatsonX-052FAD.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Overview

StoryTeller AI transforms any topic into an educational story perfect for beginners. Simply provide a topic, and the application will:
- Generate an engaging, beginner-friendly story using IBM's Mistral Large model
- Convert the story to high-quality audio speech
- Save the audio as an MP3 file for offline listening

Perfect for educators, students, content creators, and anyone who loves learning through storytelling!

## Features

✨ **AI-Powered Story Generation**: Uses IBM WatsonX Mistral Large model for creative, educational content  
🎯 **Beginner-Friendly**: Stories are written in simple, clear language with interesting facts  
🔊 **Text-to-Speech**: Converts stories to natural-sounding audio using Google TTS  
💾 **Audio Export**: Saves stories as MP3 files for easy sharing and offline listening  
📖 **Educational Focus**: Each story includes a summary of key learning points  
⚡ **Fast Generation**: Creates complete stories in seconds

## Demo

**Input:**
```python
topic = "the life cycle of butterflies"
```

**Output:**
- Printed story text (200-300 words)
- Audio player widget (in Jupyter notebooks)
- `generated_story.mp3` file ready to play

## Prerequisites

- Python 3.8 or higher
- IBM WatsonX account with API access
- Internet connection for API calls

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/StoryTeller.git
cd StoryTeller
```

2. **Install required dependencies:**
```bash
pip install ibm-watsonx-ai
pip install gTTS
pip install ipython
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

3. **Set up IBM WatsonX credentials:**
   - Sign up at [IBM WatsonX](https://www.ibm.com/watsonx)
   - Get your API credentials
   - Update the `project_id` in `StoryTeller.py` if needed

## Usage

### Basic Usage

1. **Run the script:**
```bash
python StoryTeller.py
```

2. **Customize the topic:**
```python
# Edit this line in StoryTeller.py
topic = "your desired topic here"
```

### In Jupyter Notebook

```python
from StoryTeller import generate_story
from gtts import gTTS
from IPython.display import Audio

# Generate story
topic = "the solar system"
story = generate_story(topic)
print(story)

# Create audio
tts = gTTS(story)
tts.save("my_story.mp3")
```

### Example Topics

- "the water cycle"
- "how photosynthesis works"
- "the history of computers"
- "ancient Egyptian pyramids"
- "how airplanes fly"
- "the human digestive system"

## Project Structure

```
StoryTeller/
│
├── StoryTeller.py           # Main application script
├── generated_story.mp3      # Sample generated audio file
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore file
└── LICENSE                 # MIT License
```

## Configuration

### Model Parameters

You can customize the story generation by modifying these parameters in `StoryTeller.py`:

```python
params = {
    GenParams.DECODING_METHOD: "greedy",  # Options: "greedy", "sample"
    GenParams.MAX_NEW_TOKENS: 1000,       # Adjust story length (500-2000)
}
```

### Story Prompt Customization

Modify the prompt in the `generate_story()` function to change:
- Target audience (beginners, intermediate, advanced)
- Story length (100-500 words)
- Tone (formal, casual, enthusiastic)
- Content focus (facts, narrative, tutorial)

### Audio Settings

Customize text-to-speech output:

```python
# Change language
tts = gTTS(story, lang='en')  # Options: 'en', 'es', 'fr', 'de', etc.

# Change speech speed
tts = gTTS(story, slow=False)  # Set to True for slower speech
```

## API Information

### IBM WatsonX Models

**Current Model**: `mistralai/mistral-large`

To see all available models:
```python
client.foundation_models.TextModels.show()
```

**Other Compatible Models:**
- `ibm/granite-3-2-8b-instruct`
- `meta-llama/llama-3-70b-instruct`
- `google/flan-t5-xxl`

## Output

### Console Output
The generated story is printed to the console with proper formatting.

### Audio File
- **Format**: MP3
- **Filename**: `generated_story.mp3`
- **Location**: Same directory as the script
- **Quality**: Standard TTS quality suitable for educational use

### Jupyter Notebook
Interactive audio player widget for immediate playback.

## Use Cases

🎓 **Education**: Create audio lessons for students  
📱 **Content Creation**: Generate podcast material  
♿ **Accessibility**: Convert educational content to audio for visually impaired learners  
🌍 **Language Learning**: Practice listening comprehension  
👨‍👩‍👧‍👦 **Parenting**: Create bedtime stories for children  
📚 **Research**: Quick summaries of complex topics

## Limitations

- Requires active internet connection for API calls
- Story generation depends on IBM WatsonX API availability
- Audio quality is limited by Google TTS capabilities
- English language output by default (customizable)

## Troubleshooting

### Common Issues

**"Authentication failed"**
- Verify your IBM WatsonX credentials
- Check if your project ID is correct
- Ensure API access is enabled

**"Module not found"**
- Install missing dependencies: `pip install -r requirements.txt`
- Verify Python version is 3.8+

**"No audio output"**
- Check if the MP3 file was created in the directory
- Verify gTTS installation
- Try running with administrator/sudo privileges

**"Story is too short/long"**
- Adjust `MAX_NEW_TOKENS` parameter
- Modify the prompt to request specific length

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions
- Add support for multiple languages
- Create a web interface with Flask/Gradio
- Implement batch story generation
- Add voice customization options
- Create a story library/database

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **IBM WatsonX** for providing powerful AI models
- **Google Text-to-Speech (gTTS)** for audio conversion
- **Mistral AI** for the Mistral Large language model

## Roadmap

- [ ] Web-based user interface
- [ ] Multiple voice options
- [ ] Story templates for different subjects
- [ ] Multi-language support
- [ ] Batch processing for multiple topics
- [ ] Custom voice speed and pitch controls
- [ ] Story rating and feedback system
- [ ] Integration with educational platforms

## Contact

For questions, suggestions, or issues, please open an issue in the GitHub repository.

---

**Made with ❤️ for learners everywhere**

*Transform any topic into an engaging audio story with the power of AI!*
