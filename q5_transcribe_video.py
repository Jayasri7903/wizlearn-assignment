import whisper

# Load whisper model
model = whisper.load_model("tiny")# You can use "tiny", "small" for faster speed

# Path to your video file (ensure this matches the downloaded filename)
video_path = "wizlearn_video.mp4"  # Rename the video file to this or update the path

# Transcribe
print("🎤 Transcribing...")
result = model.transcribe(video_path)

# Save the transcript
with open("q5_transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("✅ Transcript saved as q5_transcript.txt")
