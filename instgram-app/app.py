from flask import Flask, jsonify, request

app = Flask(__name__)

posts = [
    {"id": 1, "user": "nishant", "caption": "Hello from Instagram!", "likes": 5},
]

@app.route('/')
def home():
    return "📸 Mini Instagram API is running!"

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post_id = len(posts) + 1
    post = {
        "id": post_id,
        "user": data.get("user"),
        "caption": data.get("caption"),
        "likes": 0
    }
    posts.append(post)
    return jsonify(post), 201

@app.route('/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    for post in posts:
        if post["id"] == post_id:
            post["likes"] += 1
            return jsonify(post)
    return jsonify({"error": "Post not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
