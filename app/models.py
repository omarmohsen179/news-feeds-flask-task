from app.db import get_db_connection


def add_post(content, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO posts (content, user_id) VALUES (%s, %s)", (content, user_id)
    )
    conn.commit()
    cursor.close()
    conn.close()


def update_post(post_id, content):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE posts SET content = %s WHERE id = %s", (content, post_id))
    conn.commit()
    cursor.close()
    conn.close()


def delete_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM posts WHERE id = %s", (post_id,))
    conn.commit()
    cursor.close()
    conn.close()


def get_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM posts WHERE id = %s", (post_id,))
    post = cursor.fetchone()
    cursor.close()
    conn.close()
    return post


def get():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return posts
