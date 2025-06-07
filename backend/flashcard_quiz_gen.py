from transformers import pipeline
import os

def read_input(path="course_transcripts/roadmap.txt"):
    if not os.path.exists(path):
        raise FileNotFoundError("Roadmap not found. Please run roadmap_gen first.")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_model(model_name="google/flan-t5-large"):
    print("Loading model...")
    return pipeline("text2text-generation", model=model_name)

def generate_flashcards(text, generator):
    prompt = f"""You are a helpful assistant. Generate 5 flashcards from the following learning content:
{text[:1000]}

Format:
Q1: ...
A1: ...
Q2: ...
A2: ...
"""
    result = generator(prompt, max_new_tokens=300)[0]['generated_text']
    return result

def generate_quiz(text, generator):
    prompt = f"""Generate 5 multiple-choice questions based on the following content. Include 4 options and mark the correct answer with (Correct):

{text[:1000]}

Format:
1. Question?
   A. ...
   B. ...
   C. ...
   D. ... (Correct)
"""
    result = generator(prompt, max_new_tokens=400)[0]['generated_text']
    return result

if __name__ == "__main__":
    content = read_input()
    gen = load_model()

    flashcards = generate_flashcards(content, gen)
    quiz = generate_quiz(content, gen)

    os.makedirs("course_transcripts", exist_ok=True)
    with open("course_transcripts/flashcards.txt", "w", encoding="utf-8") as f:
        f.write(flashcards)
    with open("course_transcripts/quizzes.txt", "w", encoding="utf-8") as f:
        f.write(quiz)

    print("✅ Flashcards and quizzes saved!")
