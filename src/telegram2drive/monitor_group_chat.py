# standard
import os

# local
from environment_variables import API_HASH, API_ID, GROUP_CHAT_ID

# third party
from pyrogram import Client, filters, idle
from upload_to_drive import upload_to_drive

app = Client("audio_uploader_bot", api_id=API_ID, api_hash=API_HASH)


@app.on_message(filters.chat(GROUP_CHAT_ID) & filters.audio & ~filters.voice)
def handle_audio(client: Client, message):
    audio = message.audio
    file_name = f"{audio.file_unique_id}_{audio.file_name or 'audio.mp3'}"
    print("Got an audio file")
    message.download(file_name)

    print(f"Downloaded: {file_name}")
    upload_to_drive(f"downloads/{file_name}")
    os.remove(f"downloads/{file_name}")


def main():
    app.start()
    print("Listening...")
    idle()
    app.stop()


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    try:
        main()
    except Exception as e:
        print(f"Fatal error: {e}")
