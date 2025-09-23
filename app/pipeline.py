import os, json, boto3, requests, random
from datetime import datetime

# Environment variables for secrets and bucket names
RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
METADATA_BUCKET = os.environ.get("METADATA_BUCKET")
VIDEOS_BUCKET = os.environ.get("VIDEOS_BUCKET")
PROCESSED_BUCKET = os.environ.get("PROCESSED_BUCKET")
LOGS_BUCKET = os.environ.get("LOGS_BUCKET")

# Initialize S3 client
s3 = boto3.client('s3')

def log(message):
    dt = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    print(f"{dt} - {message}")

def fetch_highlights(league="NCAA", date="2025-09-23"):
    url = "https://highlightly-api.p.rapidapi.com/highlights"
    headers = {
    "X-RapidAPI-Key": "a14ada9ebcmsh88d4fefad739924p10c00cjsn4837c2a23855",
    "X-RapidAPI-Host": "highlightly-api.p.rapidapi.com"  # check actual host from docs
}

    }
    params = {"league": league, "date": date}  # API query parameters
    r = requests.get(url, headers=headers, params=params)
    data = r.json()
    
    # Save metadata to S3
    s3.put_object(
        Bucket=METADATA_BUCKET,
        Key=f"highlights/{league}/{date}/highlights.json",
        Body=json.dumps(data)
    )
    log("Metadata saved to S3")
    
    # Pick a random video
    if data:
        # Make sure 'videoUrl' exists in API response
        video_url = data[random.randint(0, len(data)-1)].get("videoUrl")
        if video_url:
            download_video(video_url, date, league)

def download_video(url, date, league):
    r = requests.get(url)
    filename = url.split("/")[-1]
    s3.put_object(
        Bucket=VIDEOS_BUCKET,
        Key=f"incoming/{filename}",
        Body=r.content
    )
    log(f"Video {filename} saved to S3")
    # Trigger MediaConvert (code skipped)

if __name__ == "__main__":
    fetch_highlights()
