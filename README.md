            ┌───────────────────────────────┐
            │         EventBridge            │
            │ (Scheduled Trigger e.g. Daily) │
            └───────────────┬───────────────┘
                            │
                            ▼
              ┌───────────────────────────┐
              │     EC2 Instance (App)     │
              │  - Runs Python pipeline.py │
              │  - Uses boto3 & requests   │
              └───────────────┬───────────┘
                              │
   ┌──────────────────────────┼─────────────────────────────┐
   │                          │                             │
   ▼                          ▼                             ▼
┌─────────────┐        ┌──────────────┐             ┌───────────────────┐
│   RapidAPI   │        │ Metadata S3  │             │   Videos S3       │
│ Sports API   │        │ (highlights) │             │ (Raw incoming)    │
│ (fetch JSON) │        │  highlights/ │             │  incoming/        │
└───────┬─────┘        └──────┬───────┘             └───────────┬───────┘
        │                      │                                 │
        │                      ▼                                 ▼
        │          ┌───────────────────────┐           ┌──────────────────────┐
        │          │ Logs S3 (processing)  │           │ Processed S3 Bucket   │
        │          │ logs/YYYY-MM-DD.log   │           │ transcoded/processed/ │
        │          └───────────────────────┘           └──────────────────────┘
        │
        ▼
 ┌───────────────┐
 │ AWS MediaConvert│
 │ (optional step) │
 │ - Transcoding   │
 │ - Format change │
 └────────────────┘






##Step-by-step Flow

1.EventBridge triggers the pipeline (cron-like schedule, e.g., once a day).

2.EC2 instance runs the Python script (pipeline.py).

3.Script fetches sports highlights JSON from RapidAPI.

4.Script saves JSON metadata → S3 metadata bucket.

5.Script picks a random video URL → downloads video → saves raw file → S3 videos bucket.

6.(Optional) Video is sent to AWS MediaConvert for processing/transcoding.

7.Processed/transcoded videos are stored → S3 processed bucket.

8.Logs of all activities are stored → S3 logs bucket.

9.Future: notifications (SNS, Lambda) can be plugged in for alerts.
