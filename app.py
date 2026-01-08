import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Quotes Intelligence Dashboard",
    page_icon="📜",
    layout="wide"
)

# ---------------- SIDEBAR CONTROLS ----------------
st.sidebar.title("⚙️ Settings")
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=True)

# ---------------- THEME COLORS ----------------
if dark_mode:
    bg = "#0e1117"
    card = "#161b22"
    text = "#ffffff"
    sub = "#d1d5db"
else:
    bg = "#f5f7fa"
    card = "#ffffff"
    text = "#111111"
    sub = "#444444"

# ---------------- CUSTOM CSS (HOVER + ANIMATION) ----------------
st.markdown(f"""
<style>
.main {{
    background-color: {bg};
}}

.card {{
    background-color: {card};
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    color: {text};
}}

.card:hover {{
    transform: translateY(-6px) scale(1.02);
    box-shadow: 0 18px 40px rgba(0,0,0,0.35);
}}

.fade {{
    animation: fadeIn 1s ease-in-out;
}}

@keyframes fadeIn {{
    from {{opacity: 0; transform: translateY(15px);}}
    to {{opacity: 1; transform: translateY(0);}}
}}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
quotes_df = pd.read_csv("quotes_data.csv")
authors_df = pd.read_csv("authors_data.csv")

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📜 Quotes Explorer", "🧠 Author Explorer", "📊 Analytics"]
)

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":
    st.markdown(f"<h1 class='fade' style='color:{text};'>📜 Quotes Intelligence Dashboard</h1>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='color:{sub};'>Web Scraping & Crawling with Interactive Analytics</p>",
        unsafe_allow_html=True
    )

    tags_series = quotes_df["Tags"].dropna().astype(str)
    total_tags = len(set(", ".join(tags_series).split(", ")))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card fade">
            <div>Total Quotes</div>
            <h2>{len(quotes_df)}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card fade">
            <div>Total Authors</div>
            <h2>{authors_df["Author"].nunique()}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card fade">
            <div>Total Tags</div>
            <h2>{total_tags}</h2>
        </div>
        """, unsafe_allow_html=True)

    # -------- DOWNLOAD BUTTONS --------
    st.markdown("### ⬇️ Download Data")

    csv_buffer = BytesIO()
    excel_buffer = BytesIO()

    quotes_df.to_csv(csv_buffer, index=False)
    quotes_df.to_excel(excel_buffer, index=False)

    d1, d2 = st.columns(2)
    with d1:
        st.download_button(
            "⬇️ Download CSV",
            csv_buffer.getvalue(),
            "quotes_data.csv",
            "text/csv"
        )
    with d2:
        st.download_button(
            "⬇️ Download Excel",
            excel_buffer.getvalue(),
            "quotes_data.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# ---------------- QUOTES EXPLORER ----------------
elif page == "📜 Quotes Explorer":
    st.title("📜 Quotes Explorer")

    search = st.text_input("🔍 Search quote or author")

    if search:
        filtered_df = quotes_df[
            quotes_df["Quote"].str.contains(search, case=False, na=False) |
            quotes_df["Author"].str.contains(search, case=False, na=False)
        ]
    else:
        filtered_df = quotes_df

    st.dataframe(filtered_df, use_container_width=True)

# ---------------- AUTHOR EXPLORER ----------------
elif page == "🧠 Author Explorer":
    st.title("🧠 Author Explorer")

    author_list = authors_df["Author"].unique()
    selected_author = st.selectbox("Select an Author", author_list)

    author_info = authors_df[authors_df["Author"] == selected_author].iloc[0]

    st.markdown(f"<div class='card fade'>", unsafe_allow_html=True)
    st.subheader(selected_author)
    st.write(f"**Born:** {author_info['Born Date']} {author_info['Born Place']}")
    st.write(author_info["Description"])
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ANALYTICS (DYNAMIC USER INPUT) ----------------
elif page == "📊 Analytics":
    st.title("📊 Smart Analytics")

    query = st.text_input(
        "Type your analysis request 👇",
        placeholder="top 5 authors | most popular author | top tags | top 10 quotes"
    ).lower()

    if query:
        st.markdown("<div class='fade'>", unsafe_allow_html=True)

        # Top Authors
        if "top" in query and "author" in query:
            n = int("".join(filter(str.isdigit, query)) or 5)
            data = quotes_df["Author"].value_counts().head(n)

            fig, ax = plt.subplots()
            data.plot(kind="bar", ax=ax)
            st.pyplot(fig)

        # Most Popular Author
        elif "most popular author" in query:
            author = quotes_df["Author"].value_counts().idxmax()
            count = quotes_df["Author"].value_counts().max()
            st.success(f"🏆 Most Popular Author: **{author}** ({count} quotes)")

        # Top Quotes
        elif "quote" in query:
            n = int("".join(filter(str.isdigit, query)) or 5)
            st.dataframe(quotes_df.head(n))

        # Top Tags
        elif "tag" in query:
            all_tags = quotes_df["Tags"].dropna().astype(str).str.split(", ").explode()
            top_tags = all_tags.value_counts().head(5)

            fig, ax = plt.subplots()
            top_tags.plot(kind="bar", ax=ax)
            st.pyplot(fig)

        else:
            st.warning("Try: top 5 authors | most popular author | top tags")

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
# ---------------- FOOTER ----------------
st.markdown("""
<style>
.footer {
    margin-top: 40px;
    padding: 22px;
    border-radius: 16px;
    text-align: center;
    background: linear-gradient(135deg, #4e54c8, #8f94fb);
    color: white;
    font-size: 15px;
    font-weight: 500;
    box-shadow: 0 8px 25px rgba(0,0,0,0.35);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.footer:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 18px 40px rgba(0,0,0,0.55);
}

.footer span {
    font-weight: 700;
    font-size: 17px;
}

.footer .tagline {
    font-size: 14px;
    opacity: 0.9;
    margin-top: 6px;
}
</style>

<div class="footer">
    🚀 Built with <span>Python & Streamlit</span><br>
    👩‍💻 Developed by <span>Snehal Salve</span><br>
    <div class="tagline">
        AI Foundations • Data Science • Analytics • Web Scraping
    </div>
</div>
""", unsafe_allow_html=True)

