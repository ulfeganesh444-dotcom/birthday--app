import streamlit as st
import datetime
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ganesh's Birthday special", page_icon="🎂", layout="centered")

# --- USER INFO ---
name = "Ganesh"
birthday = datetime.date(2025, 8, 1)
today = datetime.date.today()

# --- SAVAGE QUOTES ---
savage_quotes = [
    "I don’t compete. I dominate.",
    "Built in silence. Launched in power.",
    "Alone is my power zone.",
    "No tags. No attention. Just growth.",
    "Real ones move quiet. Results make noise."
]
quote = random.choice(savage_quotes)

# --- CHALLENGES ---
challenges = [
    "Write down 3 goals and execute 1 today.",
    "Push one silent project to GitHub.",
    "Avoid all distractions. Build like a savage.",
    "No social scroll. Just learn, lift, and code."
]
challenge = random.choice(challenges)

# --- PHOTOS ---
photo_files = st.file_uploader("Upload your birthday photos", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# --- HEADER ---
st.title(f"🔥 {name}'s Savage Birthday special Dashboard 🔥")
st.subheader(f"Date: {birthday.strftime('%d %B')} | Today: {today.strftime('%d %B %Y')}")
st.markdown("---")

# --- PHOTO DISPLAY ---
if photo_files:
    st.markdown("### 📸 Uploaded Photos")
    for photo in photo_files:
        st.image(photo, use_container_width=True)
else:
    st.info("Upload your favorite birthday photos to display here.")

# --- MINDSET & CHALLENGE ---
st.markdown("### 💭 Savage Mindset Quote")
st.success(f"\"{quote}\"")

st.markdown("### 🎯 Today's Savage Challenge")
st.warning(challenge)

# --- FRIENDS/FAMILY SHARING ---
st.markdown("---")
st.header("💬 Message Board")
st.markdown("Invite my friends or family to wish me below 👇")

with st.form("wish_form"):
    sender_name = st.text_input("Your Name")
    message = st.text_area("Your Wish or Message for Ganesh")
    submitted = st.form_submit_button("Send Wish")

    if submitted and sender_name and message:
        st.success(f"Thanks, {sender_name}! Your wish has been saved.")
        with open("wishes.txt", "a", encoding="utf-8") as f:
            f.write(f"From {sender_name}: {message}\n")
    elif submitted:
        st.error("Please fill in both fields to submit.")

# --- FOOTER ---
st.markdown("---")
st.markdown("🔒 This page is private. No tags. No noise. Just elevation. 💯")
st.markdown("Made by Ganesh with strong mindset 💀")
