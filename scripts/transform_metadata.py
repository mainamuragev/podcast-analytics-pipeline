import json
import pandas as pd
from pathlib import Path

INPUT_FILE = Path("data/raw/joe_rogan_metadata.json")
OUTPUT_FILE = Path("data/joe_rogan_videos.csv")

with open(INPUT_FILE, "r") as f:
    data = json.load(f)

# Extract video entries
videos = data.get("entries", [])

# Build rows
rows = []
for video in videos:
    rows.append({
        "video_id": video.get("id"),
        "title": video.get("title"),
        "upload_date": video.get("upload_date"),
        "duration": video.get("duration"),
        "view_count": video.get("view_count"),
        "like_count": video.get("like_count"),
        "channel": video.get("channel"),
        "channel_id": video.get("channel_id"),
    })

df = pd.DataFrame(rows)
df.to_csv(OUTPUT_FILE, index=False)
print(f"Saved {len(df)} records to {OUTPUT_FILE}")
