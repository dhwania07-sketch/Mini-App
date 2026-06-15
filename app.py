import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------------------------
# Product Database
# ---------------------------------------------------
products = [
    {
        "name": "Wireless Bluetooth Headphones",
        "price": 79.99,
        "description": "Premium over-ear headphones with noise cancellation and 30-hour battery life.",
        "category": "Electronics"
    },
    {
        "name": "Smart Fitness Watch",
        "price": 129.99,
        "description": "Track your health, workouts, sleep, and notifications.",
        "category": "Wearables"
    },
    {
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "description": "RGB mechanical keyboard for productivity and gaming.",
        "category": "Electronics"
    },
    {
        "name": "Minimalist Backpack",
        "price": 54.99,
        "description": "Stylish backpack for work and travel.",
        "category": "Fashion"
    },
    {
        "name": "Portable Coffee Maker",
        "price": 39.99,
        "description": "Brew coffee anywhere.",
        "category": "Home & Kitchen"
    },
    {
        "name": "LED Desk Lamp",
        "price": 29.99,
        "description": "Adjustable LED desk lamp.",
        "category": "Home & Kitchen"
    }
]

# ---------------------------------------------------
# CSS
# ---------------------------------------------------
st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

.hero {
    background: linear-gradient(135deg,#4F46E5,#7C3AED);
    color:white;
    padding:40px;
    border-radius:20px;
    text-align:center;
    margin-bottom:30px;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
    min-height:250px;
}

.price{
    color:green;
    font-weight:bold;
    font-size:20px;
}

.category{
    color:#4F46E5;
    font-size:13px;
    font-weight:bold;
}

/* Floating support button */
.support-btn{
    position:fixed;
    bottom:20px;
    right:20px;
    background:#4F46E5;
    color:white;
    padding:15px 25px;
    border-radius:50px;
    text-decoration:none;
    font-weight:bold;
    z-index:9999;
    box-shadow:0px 4px 12px rgba(0,0,0,0.2);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(
    list(set([p["category"] for p in products]))
)

selected_category = st.sidebar.selectbox(
    "Categories",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Shopping Cart")
st.sidebar.write("Items: 3")
st.sidebar.write("Subtotal: $249.97")
st.sidebar.success("Total: $249.97")

# ---------------------------------------------------
# Homepage
# ---------------------------------------------------
st.markdown("""
<div class="hero">
<h1>🛍️ MiniStore</h1>
<p>Your one-stop destination for quality products.</p>
</div>
""", unsafe_allow_html=True)

st.header("Welcome to MiniStore")

st.write(
    "Explore our featured collection of products."
)

# Filter products
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

st.subheader("Featured Products")

cols = st.columns(3)

for i, product in enumerate(filtered_products):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="product-card">
                <div class="category">{product['category']}</div>
                <h4>{product['name']}</h4>
                <div class="price">${product['price']}</div>
                <p>{product['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.button(
            "Add to Cart",
            key=f"cart_{i}"
        )

# ---------------------------------------------------
# Floating Support Button
# ---------------------------------------------------
st.markdown(
    """
    <a href="/Support_Chatbot" target="_self"
       class="support-btn">
       💬 Support
    </a>
    """,
    unsafe_allow_html=True
)