# ========= SECURITY NOTES =========
# This file contains sensitive information such as API keys and database credentials.
# Ensure this file is not exposed in public repositories or shared with unauthorized individuals.
# Use environment variables or secure vaults to manage sensitive data in production environments.
# ========= SECURITY NOTES =========

# === Local LLM (Ollama) ===
OLLAMA_MODEL = "llama3.1"
OLLAMA_URL = "http://localhost:11434/api/generate"

# === Whisper.cpp (offline STT) ===
WHISPER_BINARY = r"/absolute/path/to/whisper.cpp/main" 
WHISPER_MODEL =  r"/absolute/path/to/whisper.cpp/models/ggml-base.en.bin"

# === Piper TTS voices (offline) ===
PIPER_VOICE_EN = r"/absolute/path/to/piper/voices/en_us/voice.pth"
PIPER_VOICE_JA = r"/absolute/path/to/piper/voices/ja_jp/voice.pth"
PIPER_VOICE_ZH = r"/absolute/path/to/piper/voices/zh_cn/voice.pth"

# === Spotify (free dev account) ===
SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

# === Discord Bot ===
DISCORD_TOKEN = "your_discord_bot_token"
DISCORD_CHANNEL_ID = "your_discord_channel_id"

# === AUDIO / UI ===
SAMPLE_RATE = 16000
CHANNELS = 1
UI_WIDTH = 900
UI_HEIGHT = 650
