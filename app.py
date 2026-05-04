import os
import asyncio
import subprocess
import streamlit as st
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv

# API Key load karein
load_dotenv()

# --- PLAYWRIGHT BROWSER INSTALLATION ---
# Libraries install nahi karni (wo requirements.txt karega)
# Sirf Chromium browser download karna hai
@st.cache_resource
def install_browser():
    subprocess.run(["playwright", "install", "chromium"])
    subprocess.run(["playwright", "install-deps"])

# App start hote hi browser download karein
install_browser()

# --- UI SETUP ---
st.set_page_config(page_title="AI Web Agent", page_icon="🌐")
st.title("🌐 Vision AI Browser Agent")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    model_name = st.selectbox("Model", ["gpt-4o", "gpt-4o-mini"])

user_task = st.text_area("Aap kya karwana chahte hain?", placeholder="e.g. Open YouTube and search for Coke Studio.")

# --- AGENT LOGIC ---
async def run_agent(task, key, model):
    llm = ChatOpenAI(model=model, api_key=key)
    browser = Browser(config=BrowserConfig(headless=True))
    agent = Agent(task=task, llm=llm, browser=browser)
    result = await agent.run()
    return result

# --- BUTTON ---
if st.button("Run Agent 🚀"):
    if not api_key:
        st.error("Pehle API Key sidebar mein dalein!")
    elif not user_task:
        st.warning("Task to likhein!")
    else:
        try:
            with st.status("Agent kaam kar raha hai...", expanded=True) as status:
                # Video folder check
                if not os.path.exists("./videos"):
                    os.makedirs("./videos")
                    
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                final_result = loop.run_until_complete(run_agent(user_task, api_key, model_name))
                
                status.update(label="✅ Task Complete!", state="complete")
                st.success("Success!")
                st.write(final_result)
                
                # Latest video dhoond kar dikhayein
                if os.path.exists("./videos"):
                    videos = [f for f in os.listdir("./videos") if f.endswith(".mp4")]
                    if videos:
                        latest_video = max([os.path.join("./videos", f) for f in videos], key=os.path.getctime)
                        st.video(latest_video)
        except Exception as e:
            st.error(f"Error: {str(e)}")
