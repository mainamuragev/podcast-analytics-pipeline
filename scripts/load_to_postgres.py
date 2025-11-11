import pandas as pd
from sqlalchemy import create_engine

# Path to your transformed CSV
CSV_PATH = "data/joe_rogan_videos.csv"

# Aiven PostgreSQL connection string
DB_URL = "postgresql://avnadmin:AVNS_KgyTPTbCPZDCKA56StT@pg-583808d-muragevincent39-e823.i.aivencloud.com:14040/defaultdb?sslmode=require"

# Load CSV
df = pd.read_csv(CSV_PATH)

# Connect and push to PostgreSQL
engine = create_engine(DB_URL)
df.to_sql("joe_rogan_videos", engine, if_exists="append", index=False)

print(f"Loaded {len(df)} records into PostgreSQL.")
