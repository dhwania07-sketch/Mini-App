import streamlit as st
from openai import OpenAI

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬",
    layout="wide"
)

st.title("💬 MiniStore AI Support Assistant")

# --------------------------------------------------
# OpenAI Client
# --------------------------------------------------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# --------------------------------------------------
# Product Catalog
# --------------------------------------------------
PRODUCT_CATALOG = """
MiniStore Product Catalog:

1. Wireless Bluetooth Headphones
   Price: $79.99
   Category: Electronics
   Description:
   Premium over-ear headphones with noise cancellation
   and 30-hour battery life.

2. Smart Fitness Watch
   Price: $129.99
   Category: Wearables
   Description:
   Track workouts, heart rate, sleep, and notifications.

3. Mechanical Keyboard
   Price: $89.99
   Category: Electronics
   Description:
   RGB mechanical keyboard designed for productivity
   and gaming.

4. Minimalist Backpack
   Price: $54.99
   Category: Fashion
   Description:
   Stylish and durable backpack for work and travel.

5. Portable Coffee Maker
   Price: $39.99
   Category: Home & Kitchen
   Description:
   Compact coffee maker perfect for travel.

6. LED Desk Lamp
   Price: $29.99
   Category: Home & Kitchen
   Description:
   Adjustable LED desk lamp with modern design.
"""

# --------------------------------------------------
# System Prompt
# --------------------------------------------------
SYSTEM_PROMPT = f"""
You are MiniStore's professional customer support assistant.

Your responsibilities include helping customers with:

- Products
- Product recommendations
- Orders
- Order status
- Deliveries
- Shipping
- Refunds
- Returns
- Payments
- Store policies

Store Information:

{PRODUCT_CATALOG}

Rules:

1. Only answer questions related to MiniStore.
2. Use the product catalog when answering product questions.
3. If a customer asks about topics unrelated to MiniStore,
   politely redirect them back to store support topics.
4. Never claim access to real order systems.
5. If asked for order status, explain that this is a demo store.
6. Be professional, concise, friendly, and helpful.
7. Do not answer general knowledge questions.
8. Redirect unrelated conversations back to:
   products, orders, delivery, refunds, returns, or payments.

Example redirect:
"I'm here to help with MiniStore products, orders,
delivery, refunds, returns, and payment questions.
How can I assist you with your shopping experience today?"
"""

# --------------------------------------------------
# Chat History
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            "Hello! Welcome to MiniStore Support. How can I help you today?"
        }
    ]

# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# User Input
# --------------------------------------------------
user_input = st.chat_input(
    "Ask about products, delivery, refunds, orders..."
)

if user_input:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Build conversation
    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    conversation.extend(st.session_state.messages)

    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=conversation,
            temperature=0.3,
            max_tokens=300
        )

        assistant_reply = response.choices[0].message.content

    except Exception as e:
        assistant_reply = (
            f"Error connecting to AI service:\n\n{str(e)}"
        )

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    # Display response
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)