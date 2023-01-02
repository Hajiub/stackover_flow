import requests
from flask import render_template, Flask

app = Flask(__name__)
res = requests.get("http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow")
data_list = []
srt_dt = res.json()["items"]
for item in sorted(srt_dt,key=lambda item : item["view_count"]):
    data_list.append(
        {"Tags": item['tags'], "Link": item["link"], "Views": item["view_count"], "Answers": item["answer_count"]})
@app.route("/")
def index():
    return render_template("index.html",items=data_list)
