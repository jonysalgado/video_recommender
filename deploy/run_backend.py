from ml_utils import *
import youtube_dl as ytdl
import time

queries = ["machine+learning", "data+science", "learn+italian", "valorant"]

def update_db():
    ydl = ytdl.YoutubeDL({"ignoreerrors": True})
    with open("new_videos.json", "w+") as output:
        for query in queries:
            r = ydl.extract_info("ytsearch5:{}".format(query), download=False) # Change to 50 after
            for entry in r['entries']:
                if entry is not None:
                    p = compute_prediction(entry)
                    data_front = {
                        'title': entry['title'].replace("'", ""),
                        'thumbnail': entry["thumbnails"][-1]['url'],
                        'score': float(p),
                        'video_id': entry['webpage_url'],
                        'upload_date': time.time_ns()
                    }

                    # print(data_front['video_id'], json.dumps(data_front))
                    output.write("{}\n".format(json.dumps(data_front)))

    return True