import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LoveLingual",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #1a1a1a;
        color: #e0e0e0;
    }
    .stButton > button {
        width: 100%;
        padding: 20px;
        margin: 10px 0;
        font-size: 14px;
        border-radius: 8px;
        border: none;
        font-weight: 500;
    }
    .blue-button > button {
        background-color: #1E3A8A;
        color: white;
    }
    .blue-button > button:hover {
        background-color: #2D5BB5;
    }
    .orange-button > button {
        background-color: #92400E;
        color: white;
    }
    .orange-button > button:hover {
        background-color: #B85C11;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.scores = {
        "Words of Affirmation": 0,
        "Acts of Service": 0,
        "Receiving Gifts": 0,
        "Quality Time": 0,
        "Physical Touch": 0
    }
    st.session_state.quiz_complete = False

# Love languages
love_languages = [
    "Words of Affirmation",
    "Acts of Service",
    "Receiving Gifts",
    "Quality Time",
    "Physical Touch"
]

# Questions
questions = [
    ("What would make your day?",
     "Your partner brings home your favorite snack without you asking", "Acts of Service",
     "Your partner hugs you from behind while you're cooking", "Physical Touch"),
    
    ("When you're having a tough day, what helps most?",
     "Your partner puts their hand on your shoulder and listens", "Physical Touch",
     "Your partner tells you exactly why they think you're amazing", "Words of Affirmation"),
    
    ("What's the perfect Sunday?",
     "A long hike or adventure together with no distractions", "Quality Time",
     "Your partner leaves little love notes around the house for you to find", "Words of Affirmation"),
    
    ("How does your partner show they care most?",
     "By remembering small details you mentioned weeks ago and surprising you with relevant gifts", "Receiving Gifts",
     "By taking care of the chores so you can relax", "Acts of Service"),
    
    ("What makes you feel truly connected?",
     "Holding hands, cuddling, or other physical affection", "Physical Touch",
     "Deep conversations where they really understand you", "Quality Time"),
    
    ("Your ideal evening together includes...",
     "Sitting close together watching your favorite show", "Physical Touch",
     "Them telling you how much you mean to them", "Words of Affirmation"),
    
    ("When you accomplish something, what matters?",
     "Your partner gives you flowers or a special gift to celebrate", "Receiving Gifts",
     "Your partner says they're proud of you and tells everyone", "Words of Affirmation"),
    
    ("What would make you feel most appreciated?",
     "Your partner preparing your favorite meal or fixing something you've been worried about", "Acts of Service",
     "A full day together with their complete attention", "Quality Time"),
    
    ("Which touches your heart more?",
     "Finding out they ran errands for you without being asked", "Acts of Service",
     "Them playing with your hair or giving you a massage", "Physical Touch"),
    
    ("What's most romantic to you?",
     "A thoughtfully wrapped present chosen just for you", "Receiving Gifts",
     "Uninterrupted time together talking about your dreams", "Quality Time"),
    
    ("After a long day at work, you want...",
     "Your partner to rub your shoulders and be physically close", "Physical Touch",
     "Your partner to tell you that you handled everything beautifully", "Words of Affirmation"),
    
    ("What makes you feel like they truly understand you?",
     "They remember the small things you mentioned in passing", "Words of Affirmation",
     "They make time to sit down and really listen to you", "Quality Time"),
    
    ("You'd rather they...",
     "Book a surprise getaway adventure for you two", "Quality Time",
     "Surprise you with a gift they know you've been wanting", "Receiving Gifts"),
    
    ("What's the sweetest gesture?",
     "Them noticing you're tired and taking over your responsibilities for the day", "Acts of Service",
     "A loving text in the middle of the day saying they're thinking of you", "Words of Affirmation"),
    
    ("In moments of intimacy, what matters most to you?",
     "Hugging, kissing, and feeling their physical presence", "Physical Touch",
     "Having their full attention and being the center of their world", "Quality Time"),
    
    ("When you're sick or struggling, your partner would best help by...",
     "Preparing your favorite comfort food and taking care of household tasks", "Acts of Service",
     "Bringing you a thoughtful care package with small gifts inside", "Receiving Gifts"),
    
    ("What's a dealbreaker for you?",
     "Them never taking the initiative to spend alone time with you", "Quality Time",
     "Them not acknowledging your efforts or saying 'thank you'", "Words of Affirmation"),
    
    ("When you need comfort, you prefer...",
     "Them holding you close without needing to say anything", "Physical Touch",
     "Them stepping in to handle problems so you don't have to worry", "Acts of Service"),
    
    ("Your partner would win you over by...",
     "Planning a special date night tailored perfectly to your interests", "Quality Time",
     "Presenting you with something they picked out especially for you", "Receiving Gifts"),
    
    ("Which moment feels most intimate?",
     "When they compliment you on who you are, not just what you do", "Words of Affirmation",
     "When they reach for your hand or pull you close without thinking", "Physical Touch"),
    
    ("How excited is Mackenzie for the Red Sox game with Andrew on Friday?",
     "Literally buzzing with energy about spending the evening together", "Quality Time",
     "About to melt from the overwhelming anticipation", "Physical Touch")
]

# Show quiz or results
if st.session_state.quiz_complete:
    # Display results
    st.markdown("<h1 style='text-align: center; color: #FF6B9D;'>Your Love Language Profile</h1>", unsafe_allow_html=True)
    
    # Calculate percentages and sort
    total_score = sum(st.session_state.scores.values())
    percentages = {lang: (st.session_state.scores[lang] / total_score * 100) for lang in love_languages}
    sorted_languages = sorted(percentages.items(), key=lambda x: x[1], reverse=True)
    
    # Color palette
    colors = ["#FF6B9D", "#FF8FAB", "#FF9DB8", "#2E5FD1", "#6B93D6"]
    
    # Display results
    st.markdown("<br>", unsafe_allow_html=True)
    for rank, (language, percentage) in enumerate(sorted_languages, 1):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write(f"**{rank}. {language}**")
            # Progress bar
            st.progress(percentage / 100)
        with col2:
            st.write(f"**{percentage:.1f}%**")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Take Quiz Again", use_container_width=True):
        st.session_state.current_question = 0
        st.session_state.scores = {lang: 0 for lang in love_languages}
        st.session_state.quiz_complete = False
        st.rerun()
else:
    # Display quiz
    st.markdown("<h1 style='text-align: center;'>Love Language Questionnaire</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #888888;'>Question {st.session_state.current_question + 1} of {len(questions)}</p>", unsafe_allow_html=True)
    
    question_data = questions[st.session_state.current_question]
    question_text = question_data[0]
    option1_text = question_data[1]
    option1_lang = question_data[2]
    option2_text = question_data[3]
    option2_lang = question_data[4]
    
    st.markdown(f"<h3 style='text-align: center;'>{question_text}</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(option1_text, use_container_width=True, key=f"option1_{st.session_state.current_question}"):
            st.session_state.scores[option1_lang] += 1
            st.session_state.current_question += 1
            if st.session_state.current_question >= len(questions):
                st.session_state.quiz_complete = True
            st.rerun()
    
    with col2:
        if st.button(option2_text, use_container_width=True, key=f"option2_{st.session_state.current_question}"):
            st.session_state.scores[option2_lang] += 1
            st.session_state.current_question += 1
            if st.session_state.current_question >= len(questions):
                st.session_state.quiz_complete = True
            st.rerun()
