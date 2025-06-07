import gradio as gr
import os
import subprocess

def process_youtube_video(video_url):
    # Save the video URL
    with open("backend/video_url.txt", "w") as f:
        f.write(video_url)

    # Step 1: Extract Transcript
    subprocess.run(["python", "backend/transcript_extractor.py"])

    # Step 2: Generate Roadmap
    subprocess.run(["python", "backend/roadmap_gen.py"])

    # Step 3: Generate Flashcards and Quizzes
    subprocess.run(["python", "backend/flashcard_quiz_gen.py"])

    # Read the outputs
    with open("course_transcripts/roadmap.txt", "r", encoding="utf-8") as f:
        roadmap = f.read()

    with open("course_transcripts/flashcards.txt", "r", encoding="utf-8") as f:
        flashcards = f.read()

    with open("course_transcripts/quizzes.txt", "r", encoding="utf-8") as f:
        quizzes = f.read()

    return roadmap, flashcards, quizzes

# Gradio UI
demo = gr.Interface(
    fn=process_youtube_video,
    inputs=gr.Textbox(label="📺 YouTube Course URL"),
    outputs=[
        gr.Textbox(label="🗺️ Personalized Roadmap", lines=15),
        gr.Textbox(label="🧠 Flashcards", lines=10),
        gr.Textbox(label="❓ Quizzes", lines=10)
    ],
    title="SkillSmith - YouTube Course Analyzer",
    description="Paste a YouTube course URL to generate a roadmap, flashcards, and quizzes automatically!"
)

if __name__ == "__main__":
    demo.launch()
