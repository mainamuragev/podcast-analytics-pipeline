import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

CSV_PATH = "data/joe_rogan_videos.csv"
DB_URL = os.getenv("DB_URL")

df = pd.read_csv(CSV_PATH)
engine = create_engine(DB_URL)
df.to_sql("joe_rogan_videos", engine, if_exists="append", index=False)

print(f"Loaded {len(df)} records into PostgreSQL.")
