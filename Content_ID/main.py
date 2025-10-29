import os
import pandas as pd
from tqdm import tqdm
from videohash import VideoHash

VIDEO_DIR = "C:\\Glistas\\New folder (2)\\Telegram\\Manzhanshaoji"        # folder to scan
OUTPUT_CSV = "video_hashes.csv"
HASH_BITS = 256             # default 256 bits

def compute_video_hash(video_path):
    try:
        vh = VideoHash(path=video_path)   # ✅ updated parameter name
        return vh.hash_hex
    except Exception as e:
        print(f"[ERROR] {video_path}: {e}")
        return None

def main():
    paths = []
    for root, _, files in os.walk(VIDEO_DIR):
        for f in files:
            if f.lower().endswith(('.mp4','.mkv','.mov','.avi','.flv','.wmv')):
                paths.append(os.path.join(root, f))
    print(f"Found {len(paths)} videos")

    data = []
    for path in tqdm(paths):
        h = compute_video_hash(path)
        if h:
            data.append({"path": path, "hash": h})

    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Saved hashes to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()