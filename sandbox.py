import streamlit as st

def intro():
    import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to the Sandbox Page for Tecnológico de Monterrey data science HUB! 👋")

st.sidebar.success("Select a a empty sandbox to trial apps.")

st.markdown(
        """This Sandbox page contains differents deploying apps, to be use at our final showroom.

👈 Select a empty Sandbox Page to develope examples of what AI assistance can achieve!

        ### Want to learn more about streamlit?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### Want to learn more anout Assistant API use at this project?

        - Check out [AssistanAPI.openAI](https://platform.openai.com/docs/assistants/overview)

        ### See more complex demos
    """
    )

