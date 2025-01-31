import streamlit as st

st.title("📂 Projects")
st.write("### Weather App")

st.write("Simple weather app that uses OpenWeatherMap API to get the weather of a city and Tkinter for GUI. It displays the temperature and weather description of the city.") 

leftimg, middleimg, rightimg = st.columns(3) # Create 3 columns

leftimg.image(   
    "https://raw.githubusercontent.com/xTakeshido/portfolio_app/main/assets/img/est1.png",
    use_container_width=True,
)
middleimg.image(
    "https://raw.githubusercontent.com/xTakeshido/portfolio_app/main/assets/img/est2.png",
    use_container_width=True,
)
rightimg.image(   
    "https://raw.githubusercontent.com/xTakeshido/portfolio_app/main/assets/img/est3.png",
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

st.markdown('<div style="margin-top: 15px;"> </div>',unsafe_allow_html=True)
st.write("### Flight Price Checker")

st.markdown('<div style="margin-top: 10px;">The Flight Price Checker is a Streamlit-based web application that allows users to check flight prices for a given route and date using the Booking.com API.</div>', unsafe_allow_html=True) 

st.image(
    "https://raw.githubusercontent.com/xTakeshido/portfolio_app/main/assets/img/flightchecker.png",
    use_container_width=True,
)

st.markdown(
    """
    <a style="text-decoration: none;" href="https://github.com/xTakeshido/flight_prices" target="_blank">
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