import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to OUFC Maps! 👋")

    st.sidebar.success("Select a map layer above.")

    st.markdown(
        """
        OUFC Maps is a free service provided by the Ontario Urban Forest Council....omg
        
        Here, we provide maps and layers to identify communities that have urban forest policies and plans. 
        **👈 Select a layer from the sidebar** 
        ### Want to learn more?
        - Jump into our home page [OUFC](https://oufc.org)
        
    """
    )


if __name__ == "__main__":
    run()
