import streamlit as st # Streamlit library

#Logo resize
st.html("""
  <style>
    [alt=Logo] {
      height: 20rem;
    }
  </style>
        """)

#Page Setup
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/photo_camera_front:",
    default=True,
)
projects_page = st.Page(
    page="views/projects.py",
    title="Projects",
    icon=":material/developer_board:",
)

# Navigation Setup
pg = st.navigation([st.Page("views/about_me.py"), st.Page("views/projects.py")])

# Display logo in the sidebar
st.sidebar.image("assets/img/logo.png", use_container_width=True)

# Run Navigation
pg.run()