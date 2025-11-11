import yt_dlp
import json
from pathlib import Path

OUTPUT_FILE = Path("data/raw/joe_rogan_metadata.json")
UPLOADS_PLAYLIST = "https://www.youtube.com/playlist?list=UUzQUP1qoWDoEbmsQxvdjxgQ"

ydl_opts = {
    "quiet": False,
    "extract_flat": False,
    "dump_single_json": True,
    "playlistend": 20,  # Limit to 20 videos for testing
    "skip_download": True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(UPLOADS_PLAYLIST, download=False)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(info, f, indent=2)

print(f"Saved metadata to {OUTPUT_FILE}")
