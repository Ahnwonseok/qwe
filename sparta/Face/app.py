from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.ozvefus.mongodb.net/Clurster0?retryWrites=true&w=majority')
db = client.dbsparta

from face_rec import main

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    file = open('/face_rec/imagxes/Hello.txt', 'w')
    file.write(bucket_receive)
    file.close()
    # comparison()

    return jsonify({'msg': '검색완료'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.add.update_one({'num': int(num_receive)}, {'$set': {'done': 1}}) #클라에서 넘어온 숫자는 모두 문자

    return jsonify({'msg': '버킷완료'})

@app.route("/bucket/del", methods=["POST"])
def bucket_del():
    num_receive = request.form['num_give']
    db.add.update_one({'num': int(num_receive)}, {'$set': {'del': 1}})  # 클라에서 넘어온 숫자는 모두 문자

    return jsonify({'msg': '삭제완료'})

@app.route("/bucket/can", methods=["POST"])
def bucket_can():
    num_receive = request.form['num_give']
    db.add.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})  # 클라에서 넘어온 숫자는 모두 문자

    return jsonify({'msg': '취소완료'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.add.find({}, {'_id': False}))
    return jsonify({'buckets': bucket_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)