# 🧠 SkillSmith: AI-Powered Learning Companion

SkillSmith is an intelligent tool that transforms any YouTube course into a **personalized learning experience** — complete with:

- 📍 Roadmaps
- 🧾 Flashcards
- ❓ Quizzes

All automatically generated using LLMs. Just input a YouTube video URL, and SkillSmith does the rest!

---

## 🚀 Features

- 🔗 **YouTube Integration**: Input any video URL to extract the transcript.
- 🧠 **Roadmap Generator**: Creates a step-by-step curriculum from the content.
- 🧾 **Flashcard Maker**: Summarizes concepts into flashcards for spaced repetition.
- ❓ **Quiz Builder**: Generates MCQs to test your knowledge.
- 💡 **Gradio Frontend**: Easy-to-use web interface for instant interaction.

---

## 📸 Demo

> Coming soon — upload a short screen recording to your GitHub or add [screenshots](#) here.

---

## 📂 Project Structure

skillsmith/
├── backend/
│ ├── transcript_extractor.py # Extracts transcript from YouTube videos
│ ├── roadmap_gen.py # Generates a learning roadmap
│ ├── flashcard_quiz_gen.py # Creates flashcards and quizzes
│ ├── backend_gen.py # Integrates pipeline
├── frontend/
│ └── app.py # Gradio UI for interaction
├── course_transcripts/
│ ├── transcript.txt
│ ├── roadmap.txt
│ ├── flashcards.txt
│ └── quizzes.txt
├── requirements.txt
└── README.md
