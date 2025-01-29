import streamlit as st

st.title("📂 Projects")
st.write("### Weather App")

st.write("Simple weather app that uses OpenWeatherMap API to get the weather of a city. It displays the temperature and weather description of the city.") 

leftimg, middleimg ,rightimg = st.columns(3)

leftimg.image(   # Display an image
    "assets\img\weatherapp1.png",
    use_container_width=True,
)
middleimg.image(
    "assets\img\weatherapp2.png",
    use_container_width=True,
)
rightimg.image(   # Display an image
    "assets\img\weatherapp3.png",
    use_container_width=True,
)

st.markdown(
    """
    <a style="text-decoration: none;" href="https://github.com/xTakeshido/weather_app" target="_blank">
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
