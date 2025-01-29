import streamlit as st

st.markdown("""
            <center>
            <style>.header-about {font-size:99px; display: inline-block; font-weight: 650;} .excl {font-size:99px; display: inline-block; color: Indigo; font-weight: 650;}</style>
            <div class='header-about'>HELLO</div>
            <div class='excl'>!</div></center>
            """, 
            unsafe_allow_html=True
)

left, right = st.columns(2)

# Create buttons as hyperlinks with icons and matte black style
left.markdown(
    """
    <a style="text-decoration: none;" href="https://example.com/resume" target="_blank">
        <button style="
            width: 100%;
            padding: 0.75rem 1rem;
            border: none;
            outline: none;
            color: rgb(255, 255, 255);
            background: #333;
            position: relative;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        " role="button">
            <img src="https://img.icons8.com/material-outlined/24/ffffff/resume.png" alt="Resume Icon"/>
            Resume
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

right.markdown(
    """
    <a style="text-decoration: none;" href="https://github.com/xTakeshido" target="_blank">
        <button style="
            width: 100%;
            padding: 0.75rem 1rem;
            border: none;
            outline: none;
            color: rgb(255, 255, 255);
            background: #333;
            position: relative;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        " role="button">
            <img src="https://img.icons8.com/material-outlined/24/ffffff/github.png" alt="GitHub Icon"/>
            GitHub
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# Embed custom HTML and CSS to enable text wrapping
st.markdown(
f"""<p style='text-align: center; font-size: 20px; margin-top: 1rem; margin-bottom: 1rem;'>
        I’m currently diving into the world of Python, learning how to turn ideas into code and solve problems creatively.
          One of my biggest dreams is to visit Tokyo and South Korea, and it’s a goal I’m actively working toward.
            The thought of experiencing their vibrant cultures and stunning landscapes inspires me every day.</p>
 """,
    unsafe_allow_html=True,
)

leftimg, rightimg = st.columns(2)

leftimg.image(   # Display an image
    "assets\img\japaneseflag.png",
    use_container_width=True,
)
rightimg.image(   # Display an image
    "assets\img\southkoreanflag.png",
    use_container_width=True,
)

st.markdown(
f"""<p style='text-align: center; font-size: 20px;'>Right now i'm looking for opportunities to grow and learn, so if you have a project or idea you’d like to collaborate on, feel free to reach out to me!</p>""",
    unsafe_allow_html=True,
)

# Include Material Icons library
st.markdown(
    """
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    """,
    unsafe_allow_html=True,
)

# Email button with Material Icons
st.markdown(
    """
    <a style="text-decoration: none;" href="mailto:xtakeshido@gmail.com" target="_blank">
        <button style="
            width: 100%;
            padding: 0.75rem 1rem;
            border: none;
            outline: none;
            color: rgb(255, 255, 255);
            background: #333;
            position: relative;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        " role="button">
            <span class="material-icons" style="font-size: 24px;">email</span>
            Send me an email
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
