from flask import Blueprint, request, jsonify
from app.models import add_post, update_post, delete_post, get_post, get

main = Blueprint("main", __name__)


@main.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    add_post(data["content"], data["user_id"])
    return jsonify({"message": "Post created"}), 201


@main.route("/posts/<int:post_id>", methods=["PUT"])
def modify_post(post_id):
    data = request.json
    update_post(post_id, data["content"])
    return jsonify({"message": "Post updated"}), 200


@main.route("/posts/<int:post_id>", methods=["DELETE"])
def remove_post(post_id):
    delete_post(post_id)
    return jsonify({"message": "Post deleted"}), 200


@main.route("/posts", methods=["GET"])
def retrieve_posts():
    post = get()
    return jsonify(post), 200


@main.route("/post/<int:post_id>", methods=["GET"])
def retrieve_post(post_id):
    post = get_post(post_id)
    if post:
        return jsonify(post), 200
    else:
        return jsonify({"message": "Post not found"}), 404
