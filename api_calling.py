from google import genai
import os, io
from gtts import gTTS


# setting up the environment variable for the API key
from dotenv import load_dotenv
load_dotenv()
my_api_key = os.getenv("gemini_api_key")


#   initializing the genai client with the API key
my_client = genai.Client(api_key=my_api_key)


#note generation function
def generate_note_summary(images, selected_lang="English"):


    prompt = f"Generate a concise summary of the notes in the images in {selected_lang}. Focus on key points and main ideas. Avoid unnecessary details. Provide a clear and structured summary that captures the essence of the images at max 100 words. make sure to cover all the important aspects of the notes in the images. The summary should be easy to understand and should highlight the most relevant information from the notes. Use bullet points or numbered lists if necessary to organize the summary effectively. Ensure that the summary is coherent and flows well, providing a comprehensive overview of the content in the images. Follow necessary formatting guidelines to enhance readability and clarity. The summary should be concise yet informative, providing a clear understanding of the key concepts and ideas presented in the notes. Avoid including any irrelevant information or personal opinions in the summary. Focus on delivering a well-structured and informative summary that effectively captures the main points from the images."

    response = my_client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= [images, prompt]
    )
    return response.text




#audio generation function
def generate_audio_from_text(text, lang_code):
    speech = gTTS(text=text, lang=lang_code, slow=False)
    audio_file = io.BytesIO()
    speech.write_to_fp(audio_file)
    return audio_file


 #quiz

def quiz_generator(image,difficulty, selected_lang):

    prompt = f"Generate 3 quizzes based on the {difficulty},in {selected_lang}.Add markdown to differentiate the options. Add correct answer too,after the quiz with the heading 'Answer' and make it bold. The quiz should be based on the content of the image and should be relevant to the topic. The quiz should be designed to test the understanding of the content in the image and should be appropriate for the selected difficulty level. The quiz should be engaging and should encourage critical thinking. The quiz should be well-structured and should provide clear instructions for answering. The quiz should be designed to assess the knowledge and comprehension of the content in the image effectively."

    response = my_client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[image,prompt]
    )

    return response.text 