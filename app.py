
import streamlit as st

st.set_page_config(
    page_title="RADIA AI",
    page_icon="🩻",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #F5F7F5;
}
h1, h2, h3 {
    color: #173D36;
}
[data-testid="stSidebar"] {
    background-color: #E8EFEB;
}
.hero {
    background: #173D36;
    padding: 35px;
    border-radius: 15px;
    color: white;
}
.hero h1 {
    color: white;
    font-size: 42px;
}
.hero p {
    color: #D7E5DD;
    font-size: 17px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🩻 RADIA AI")
st.sidebar.caption("Medical Imaging Intelligence")
st.sidebar.divider()

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Home",
        "Image Workspace",
        "RADIA Academy",
        "About"
    ]
)

st.sidebar.divider()
st.sidebar.caption("RADIA AI | Version 0.1")

# HOME PAGE
if page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>RADIA AI</h1>
        <p>Intelligence in Medical Imaging.</p>
        <p>Explore medical imaging, artificial
        intelligence and radiological education.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.subheader("Explore RADIA AI")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🩻 **Image Workspace**")
        st.write("Upload and explore medical images.")

        st.info("🧠 **AI Laboratory**")
        st.write("Explore machine learning experiments.")

    with col2:
        st.info("📚 **RADIA Academy**")
        st.write("Learn radiology and medical imaging.")

        st.info("🗂️ **Image Library**")
        st.write("Organize educational imaging resources.")

    st.divider()
    st.caption("An educational medical imaging project.")

# IMAGE WORKSPACE
elif page == "Image Workspace":

    st.title("Medical Image Workspace")
    st.write("Upload an image to begin exploring it.")

    uploaded_file = st.file_uploader(
        "Choose a medical image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:
        st.success("Image uploaded successfully!")

        st.image(
            uploaded_file,
            caption="Uploaded Medical Image",
            use_container_width=True
        )

        st.write("File name:", uploaded_file.name)
        st.write("File size:", round(
            uploaded_file.size / 1024, 2
        ), "KB")

        st.info(
            "Image analysis tools will be added "
            "in upcoming development stages."
        )

# RADIA ACADEMY
elif page == "RADIA Academy":

    st.title("RADIA Academy")
    st.write("Your medical imaging learning centre.")

    st.subheader("Learning modules")

    st.markdown("""
    - Introduction to Radiology
    - X-ray Physics
    - Chest X-ray Anatomy
    - CT Imaging
    - MRI Fundamentals
    - Medical Image Processing
    """)

# ABOUT
elif page == "About":

    st.title("About RADIA AI")

    st.write("""
    RADIA AI is an educational and research-oriented
    project exploring artificial intelligence
    in medical imaging.

    Our long-term vision is to develop tools
    for multiple radiological imaging modalities.
    """)

    st.caption("RADIA AI — Built with Python and Streamlit.")
