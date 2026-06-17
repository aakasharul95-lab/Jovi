import streamlit as st
from datetime import datetime
import random

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Jovitha's Colorful Learning & Writing Wonderland 🌈",
    page_icon="🦋",
    layout="centered"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(120deg, #f9d423 0%, #ff4e50 100%);
        color: #fff;
    }
    .big-title {
        font-size: 3em;
        font-weight: bold;
        color: #fff176;
        text-shadow: 2px 2px #ff4081;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .award {
        font-size: 1.5em;
        color: #ff80ab;
        text-align: center;
        margin-bottom: 1em;
    }
    .doctor-dream {
        font-size: 1.2em;
        color: #00bcd4;
        text-align: center;
        margin-bottom: 1em;
    }
    .fact-box {
        background: #fffde4;
        border-radius: 10px;
        padding: 1em;
        color: #333;
        font-size: 1.1em;
        margin-bottom: 1em;
        border: 2px solid #ff80ab;
    }
    .edu-plan {
        background: linear-gradient(90deg, #a1c4fd 0%, #c2e9fb 100%);
        border-radius: 10px;
        padding: 1em;
        color: #333;
        font-size: 1.1em;
        border: 2px solid #00bcd4;
        margin-bottom: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="big-title">🌟 Jovitha\'s Colorful Learning & Writing Wonderland! 🌟</div>', unsafe_allow_html=True)
st.markdown('<div class="award">🏆 Congratulations, Jovitha, on your amazing writing award! 🏆</div>', unsafe_allow_html=True)
st.markdown('<div class="doctor-dream">👩‍⚕️ Dream Big: Future Doctor in the Making! 👩‍⚕️</div>', unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=800&q=80", 
    caption="Let your imagination and knowledge fly!", 
    use_column_width=True
)

# --- SIDEBAR ---
st.sidebar.title("🌈 Jovitha's Toolbox")
color = st.sidebar.color_picker("🎨 Pick your favorite background color!", "#ff80ab")
st.sidebar.markdown("**Writing Tips:**")
st.sidebar.info("1. Let your imagination run wild!\n2. Don't worry about mistakes—just write!\n3. Use lots of details and fun words.\n4. Have fun and be yourself!")
st.sidebar.markdown("**Doctor's Corner:**")
st.sidebar.success("Did you know? The human body has 206 bones! 🦴")

# --- DYNAMIC BACKGROUND COLOR ---
st.markdown(
    f"""
    <style>
    .main {{
        background: linear-gradient(135deg, {color} 0%, #fffde4 100%);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- EDUCATIONAL FACT ---
facts = [
    "🧬 **Did you know?** The human brain is sometimes more active when you're asleep than when you're awake!",
    "🩺 **Doctors help people** by diagnosing illnesses and giving treatments to make them feel better.",
    "🦠 **Bacteria** are so tiny you need a microscope to see them, but some are helpful for your body!",
    "💉 **Vaccines** help protect you from diseases by teaching your body how to fight them.",
    "🫀 **Your heart** beats about 100,000 times every day!",
    "🧪 **Science is fun!** Mixing baking soda and vinegar creates a fizzy reaction called a chemical reaction."
]
st.markdown(f'<div class="fact-box">{random.choice(facts)}</div>', unsafe_allow_html=True)

# --- EDUCATION PLAN ---
st.header("👩‍⚕️ How to Become a Doctor in Sweden")
st.markdown("""
<div class="edu-plan">
<b>Jovitha's Dream: Doctor in Sweden 🇸🇪</b><br><br>
Here's a fun and simple plan for you!<br><br>
<ol>
  <li><b>Finish Grundskola (Elementary & Middle School)</b><br>
      - Focus on science, math, and languages.<br>
      - Stay curious and ask questions!</li><br>
  <li><b>Go to Gymnasium (High School, ages 16-19)</b><br>
      - Choose the <b>Natural Science Programme (Naturvetenskapsprogrammet)</b>.<br>
      - Study biology, chemistry, physics, and math.</li><br>
  <li><b>Apply to Medical University (Läkarprogrammet)</b><br>
      - After gymnasium, apply to a university with a medical program.<br>
      - In Sweden, medical school is usually <b>5.5 to 6 years</b> long.</li><br>
  <li><b>Become a Doctor!</b><br>
      - After university, you do a special training called <b>AT-tjänstgöring</b> (internship) for about 1.5 years.<br>
      - Then you get your license and can work as a doctor!</li>
</ol>
<b>Tip:</b> Keep reading, learning, and believing in yourself! You can do it, Jovitha! 🌟
</div>
""", unsafe_allow_html=True)

# --- WRITING PROMPT ---
st.header("🦄 Today's Magical Writing Prompt")
prompt = st.selectbox(
    "Choose a prompt to get started:",
    [
        "Write a story about a unicorn who learns to paint.",
        "Imagine you found a secret door in your school. What happens next?",
        "Describe your dream adventure with your best friend.",
        "Invent a new holiday and explain how people celebrate it.",
        "Write about a day in the life of a doctor who can talk to animals."
    ]
)
st.write(f"**Your prompt:** {prompt}")

# --- STORY WRITING & TXT DOWNLOAD ---
st.header("✍️ Start Writing Here!")
author = st.text_input("Author Name", value="Jovitha")
story_title = st.text_input("Story Title", value="My Amazing Story")
story = st.text_area("Let your creativity shine, Jovitha!", height=200)

now = datetime.now().strftime("%B %d, %Y at %H:%M")

book_content = f"""
========================================
        {story_title.upper()}
========================================

Author: {author}
Date: {now}

----------------------------------------
Prompt:
{prompt}
----------------------------------------

Story:
{story}

========================================
        THE END
========================================
"""

st.download_button(
    label="📥 Download My Story as a TXT File",
    data=book_content,
    file_name=f"{story_title.replace(' ', '_')}.txt",
    mime="text/plain"
)

# --- GENERAL KNOWLEDGE QUIZ ---
st.header("🧠 General Knowledge Quiz Time!")

questions = [
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Heart", "Skin", "Liver", "Brain"],
        "answer": "Skin"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What do doctors use to listen to your heartbeat?",
        "options": ["Thermometer", "Stethoscope", "Microscope", "Telescope"],
        "answer": "Stethoscope"
    },
    {
        "question": "How many bones are there in the human body?",
        "options": ["106", "206", "306", "406"],
        "answer": "206"
    },
    {
        "question": "What is the process by which plants make their food?",
        "options": ["Respiration", "Photosynthesis", "Digestion", "Evaporation"],
        "answer": "Photosynthesis"
    }
]

q = random.choice(questions)
user_answer = st.radio(q["question"], q["options"], key=q["question"])

if st.button("Check Answer"):
    if user_answer == q["answer"]:
        st.balloons()
        st.success("Correct! 🎉 You're a genius, Jovitha!")
    else:
        st.error(f"Oops! The correct answer is **{q['answer']}**. Keep learning!")

# --- FOOTER ---
st.markdown("---")
st.markdown("<center>Made with ❤️ for Jovitha, the amazing writer and future doctor! 🦋</center>", unsafe_allow_html=True)
