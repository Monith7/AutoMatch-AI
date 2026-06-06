import streamlit as st
from google import genai
from dotenv import load_dotenv
from database import get_all_vehicles
import os

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Page Config
st.set_page_config(
    page_title="AutoMatch AI",
    page_icon="🚗",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

div[data-testid="stChatMessage"] {
    border-radius: 15px;
    padding: 12px;
}

.vehicle-card {
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #444;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
# 🚗 AutoMatch AI

### Intelligent Vehicle Recommendation Agent

Find the perfect vehicle using AI-powered recommendations and database-driven insights.
""")

# Sidebar
st.sidebar.title("🚗 AutoMatch AI")

st.sidebar.markdown("""
### Features

✅ AI Vehicle Recommendations

✅ Vehicle Comparison

✅ Budget-Based Suggestions

✅ SQLite Vehicle Database

✅ Gemini AI Assistant
""")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### Sample Questions

• Best SUV under 20 lakhs

• Compare Creta and Seltos

• Best automatic car for city driving

• Recommend a 7-seater family vehicle
""")

# Welcome Box
st.info(
    "💡 Try asking: 'Best family SUV under 20 lakhs' or 'Compare Hyundai Creta and Kia Seltos'"
)

# Load Vehicles from SQLite
vehicles = get_all_vehicles()

vehicle_text = "\n".join([
    f"{v[0]} | ₹{v[1]} | {v[2]} | {v[3]} seats | {v[4]} | {v[5]} | {v[6]}"
    for v in vehicles
])

# Show Vehicle Database
with st.expander("📊 View Available Vehicles"):
    for vehicle in vehicles:
        st.markdown(f"""
        <div class="vehicle-card">
        <b>{vehicle[0]}</b><br>
        Price: ₹{vehicle[1]:,}<br>
        Fuel: {vehicle[2]}<br>
        Seats: {vehicle[3]}<br>
        Category: {vehicle[4]}<br>
        Mileage: {vehicle[5]}<br>
        Transmission: {vehicle[6]}
        </div>
        """, unsafe_allow_html=True)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat Input
prompt = st.chat_input(
    "Ask me about cars, SUVs, mileage, comparisons..."
)

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    system_prompt = f"""
You are AutoMatch AI, an expert Vehicle Recommendation Agent.

Use ONLY the vehicle database below.

VEHICLE DATABASE:
{vehicle_text}

Instructions:
- Recommend vehicles based on user requirements.
- Compare vehicles when requested.
- Explain recommendations clearly.
- Mention price, fuel type, mileage, seats, category and transmission.
- If an exact match doesn't exist, suggest the closest alternatives.
- Keep responses professional and concise.

User Query:
{prompt}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=system_prompt
    )

    reply = response.text

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)