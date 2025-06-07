from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import os

def extract_video_id(url):
    parsed_url = urlparse(url)
    if "youtube.com" in parsed_url.netloc:
        return parse_qs(parsed_url.query).get("v", [None])[0]
    elif "youtu.be" in parsed_url.netloc:
        return parsed_url.path[1:]
    return None

def get_transcript(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        return "Invalid YouTube URL"
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = "\n".join([t["text"] for t in transcript])
    return full_text

def save_transcript(video_url, save_path="course_transcripts/transcript.txt"):
    text = get_transcript(video_url)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Transcript saved to {save_path}")
    return save_path

if __name__ == "__main__":
    url = input("Paste a YouTube video URL: ")
    save_transcript(url)
