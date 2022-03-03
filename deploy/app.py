

import os.path
from flask import Flask, render_template, request, redirect
import os
import json
import run_backend
import time

app = Flask(__name__)

class Video:
    def __init__(self, video_id, title, thumbnail,score):
        self.video_id = video_id
        self.title = title
        self.thumbnail = thumbnail
        self.score = score

def get_predictions():
    
    videos = []
    
    new_videos_json = "new_videos.json"
    if not os.path.exists(new_videos_json):
        run_backend.update_db()
        
    last_update = os.path.getmtime(new_videos_json) * 1e9
    
    if time.time_ns() - last_update > (24*3600*1e9): # approximately 1 day
        run_backend.update_db()
        
    with open("new_videos.json", "r") as data_file:
        for line in data_file:
            line_json = json.loads(line)
            videos.append(line_json)
            
    predictions = []
    for video in videos:
        predictions.append(Video(video["video_id"], 
                    video["title"], 
                    video["thumbnail"], 
                    round(video["score"], 2)))
        
    predictions = sorted(predictions, key = lambda x: x.score, reverse=True)[:30]
    return predictions, int((time.time_ns() - last_update)/(1e9 * 60 * 60))


preds, last_update = get_predictions()

@app.route('/')
def main_page():
    return render_template("basic_table.html", title="Video Recommender", videos=preds, last_update=last_update)

@app.route('/background_process_button')
def background_process_botton():
    print(request.args.get('x'))
    print("ok")
    return ("nothing")

@app.route('/json')
def jsons():
    return render_template('test.html')

@app.route('/background_process_test')
def background_process_test():
    print(request.args.get('x'))
    print(request.args.get('y'))
    return ("nothing")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    