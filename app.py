from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.yxb3ggu.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('index.html')

# @app.route("/movie", methods=["POST"])
# def movie_post():

#     sample_url = request.form['sample_url']
#     sample_comment = request.form['sample_comment']
#     sample_star = request.form['sample_star']

#     URL = sample_url
#     headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get(URL,headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     ogtitle = soup.select_one('meta[property="og:title"]')['content']
#     ogimage = soup.select_one('meta[property="og:image"]')['content']
#     ogdesc = soup.select_one('meta[property="og:description"]')['content']

#     moive = {
#         'title' : ogtitle,
#         'image' : ogimage,
#         'description' : ogdesc,
#         'comment' : sample_comment,
#         'star' : sample_star
#     }
#     db.movies2.insert_one(moive)


#     return jsonify({'msg':'저장 완료!'})

# @app.route("/movie", methods=["GET"])
# def movie_get():
#     all_moives = list(db.movies2.find({},{'_id':False}))
#     return jsonify({'result': all_moives })

@app.route("/api/reviews", methods=["GET"])
def reviews_get():
    all_reviews = list(db.review.find({},{'_id':False}))
    print(all_reviews)
    return jsonify({'reviews': all_reviews })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)