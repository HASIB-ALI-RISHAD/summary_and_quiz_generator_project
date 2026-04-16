import streamlit as st
from PIL import Image
import string
from api_calling import generate_audio_from_text, generate_note_summary, quiz_generator


#title and description
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto three images of your notes and get a concise summary along with a quiz to test your understanding!")
st.divider()

with st.sidebar:
    st.header("Controls")

    #image upload section
    images = st.file_uploader("Upload your note images (up to 3)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    pil_images = [Image.open(img) for img in images]

    if images:
        st.success(f"{len(images)} image(s) uploaded successfully!")
        if len(images) > 3:
            st.warning("Upload at max 3 images.")
        else:
            st.subheader("Uploaded Note Images")
            col = st.columns(len(images))
            for i, img in enumerate(images):
                with col[i]:
                  st.image(img)

    #difficulty level selection

    selected_option = st.selectbox("Select Quiz Difficulty Level", options=("Easy", "Medium", "Hard"), index=None)

    selected_lang = st.selectbox("Select Language", options=("English", "Bangla", "French", "Spanish" ), index=None)

    lang_map = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Bengla": "bn"
    }
    lang_code = lang_map.get(selected_lang, "en")
    pressed = st.button("Generate Summary and Quiz")
 
if pressed:
    if not images:
        st.error("Please upload at least one image of your notes to generate the summary and quiz.")
    elif not selected_option:
        st.error("Please select a difficulty level for the quiz.")

if images and selected_option and pressed and selected_lang and len(images) <= 3:

    #note
    with st.container(border= True):
        st.subheader("Summary")

        with st.spinner("Generating summary..."):
            generated_notes = generate_note_summary(pil_images, selected_lang)
            st.markdown(generated_notes)

    #audio transcription
    with st.container(border= True):
        st.subheader("Audio Transcription")
        with st.spinner("Generating audio transcription..."):
            #clearing the markdown

            for i in string.punctuation:
                if i == "+" or i == "-" or i == "/" or i == "=":
                    continue
                generated_notes = generated_notes.replace(i, "")
             
            audio_file = generate_audio_from_text(generated_notes, lang_code)
        st.audio(audio_file)

    #quiz generation
    with st.container(border= True):
        st.subheader(f"Quiz - {selected_option} difficulty")
        with st.spinner("Generating quizzes..."):
            generated_quiz = quiz_generator(pil_images, selected_option, selected_lang)
            st.markdown(generated_quiz)
