from transformers import pipeline
import os

def read_transcript(path="course_transcripts/transcript.txt"):
    if not os.path.exists(path):
        raise FileNotFoundError("Transcript not found. Please run transcript_extractor first.")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_generator(model_name="google/flan-t5-base"):
    print("Loading model... This may take a while.")
    generator = pipeline("text-generation", model=model_name, max_new_tokens=512)
    return generator

def generate_roadmap(transcript_text, generator):
    prompt = f"""
    You are an expert learning designer. Read the following transcript and divide it into a learning roadmap.
    Output a list of modules with a title, short description, and difficulty level.
    
    Transcript:
    {transcript_text[:1000]}
    
    Format:
    1. Module Name - Description (Beginner/Intermediate/Advanced)
    """
    result = generator(prompt, do_sample=True, temperature=0.7)
    return result[0]["generated_text"]

if __name__ == "__main__":
    transcript = read_transcript()
    gen = load_generator()
    roadmap = generate_roadmap(transcript, gen)

    with open("course_transcripts/roadmap.txt", "w", encoding="utf-8") as f:
        f.write(roadmap)

    print("✅ Roadmap saved to course_transcripts/roadmap.txt")
