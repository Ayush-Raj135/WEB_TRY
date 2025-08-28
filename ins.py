import streamlit as st
from PIL import Image
import os
import json
from datetime import datetime

# Create folders if they don't exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("data", exist_ok=True)

POSTS_FILE = "data/posts.json"

def load_posts():
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_post(image_path, caption):
    posts = load_posts()
    posts.insert(0, {"image": image_path, "caption": caption, "timestamp": datetime.now().isoformat()})
    with open(POSTS_FILE, "w") as f:
        json.dump(posts, f)

# App Title
st.title("📸 Streamlit Instagram Clone")

# Image Upload Section
st.subheader("Upload a new post")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
caption = st.text_input("Enter a caption")

if uploaded_file and caption:
    image_path = os.path.join("uploads", uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    save_post(image_path, caption)
    st.success("Post uploaded!")

# Feed Section
st.subheader("📷 Feed")
posts = load_posts()
if posts:
    for post in posts:
        st.image(post["image"], width=400)
        st.caption(post["caption"])
        st.write(f"🕒 {post['timestamp'].split('T')[0]}")
        st.markdown("---")
else:
    st.write("No posts yet.")
