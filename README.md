# 📝 Note Summary and Quiz Generator

An AI-powered web application designed to help students and professionals study more effectively. By simply uploading images of typed or handwritten notes, the app extracts the core concepts, generates a concise summary, and creates a customized quiz to test your knowledge.

## 🚀 Live Demo

**[Summary and Quiz Generator](https://summaryquizgen.streamlit.app/)**

## ✨ Features

  * **Image-to-Text AI Processing:** Upload up to 3 images of your notes (JPG, JPEG, PNG) per session.
  * **Instant Summarization:** Get a clear, concise breakdown of the key points from your study materials.
  * **Dynamic Quiz Generation:** Test your comprehension with quizzes automatically tailored to your notes.
  * **Customizable Difficulty:** Adjust the quiz difficulty level to suit your learning needs.
  * **Multi-Language Support:** Generate summaries and quizzes in your preferred language.

## 🛠️ Tech Stack

  * **Frontend:** [Streamlit](https://streamlit.io/)
  * **Backend:** Python
  * **AI Engine:** Google GenAI (Gemini)

## 💻 Local Installation & Setup

To run this project on your local machine, follow these steps:

**1. Clone the repository:**
```bash
git clone https://github.com/HASIB-ALI-RISHAD/summary_and_quiz_generator_project.git
cd summary_and_quiz_generator_project
```

**2. Create a virtual environment (Recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables:**
Create a `.env` file in the root directory and add your Google Gemini API key:

```env
gemini_api_key="your_api_key_here"
```

**5. Run the application:**

```bash
streamlit run app.py
```

## 🎯 How to Use

1.  Open the app via the live link or your local server.
2.  Use the sidebar to upload your note images (up to 3 images, 200MB per file).
3.  Select your desired **Quiz Difficulty Level**.
4.  Choose your preferred **Language** from the dropdown menu.
5.  Click the **Generate Summary and Quiz** button and let the AI process your study materials\!

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\! Feel free to check the issues page to contribute.
