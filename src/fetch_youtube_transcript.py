from typing import Optional
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound

def fetch_youtube_transcript(video_url: str) -> Optional[str]:
    try:
        video_id = video_url.split("v=")[1].split("&")[0]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = '\n'.join([item['text'] for item in transcript_list])
        return transcript
    except NoTranscriptFound:
        return None

# Example usage
video_url = "https://www.youtube.com/watch?v=y7wMTwJN7rAcl"
transcript = fetch_youtube_transcript(video_url)
print(transcript)