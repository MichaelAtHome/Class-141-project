from flask import Flask, jsonify, request
import csv

all_movies = []

with open('shared_articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []
did_not_view = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_movie():
    article = all_articles[0]
    all_articles  = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/not-liked-article", methods=["POST"])
def unliked_movie():
    artice = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(not_liked_articles)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-view", methods=["POST"])
def did_not_watch():
    article = all_articles[0]
    all_articles = all_articles[1:]
    did_not_view.append(article)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()