import os
import asyncio
import streamlit as st
import subprocess

# --- Playwright Browser Download ---
@st.cache_resource
def install_playwright_browser():
    # Sirf browser download karna hai, library install nahi
    subprocess.run(["playwright", "install", "chromium"])

# Install browser
install_playwright_browser()

# Ab imports karein (requirements.txt se install hone ke baad)
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Browser Agent", page_icon="🌐")
st.title("🌐 AI Browser Agent")

# Sidebar
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password")
    model_name = st.selectbox("Model", ["gpt-4o", "gpt-4o-mini"])

user_task = st.text_area("Aap kya karwana chahte hain?", placeholder="e.g. Search for latest news on Google")

async def run_agent(task, key, model):
    llm = ChatOpenAI(model=model, api_key=key)
    browser = Browser(config=BrowserConfig(headless=True))
    agent = Agent(task=task, llm=llm, browser=browser)
    result = await agent.run()
    return result

if st.button("Run Agent 🚀"):
    if not api_key:
        st.error("API Key dalein!")
    elif not user_task:
        st.warning("Task likhein!")
    else:
        try:
            with st.status("Agent Working...", expanded=True):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                final_result = loop.run_until_complete(run_agent(user_task, api_key, model_name))
                st.success("Task Complete!")
                st.write(final_result)
        except Exception as e:
            st.error(f"Error: {str(e)}")
