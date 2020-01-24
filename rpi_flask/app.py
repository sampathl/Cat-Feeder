from flask import Flask

app=Flask(__name__)

@app.route("/_feed_data")
def _feed_data():
    print("this is ok")

