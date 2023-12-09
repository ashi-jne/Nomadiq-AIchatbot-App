# Nomadiq AI Chatbot App - Final Project
**Creators:** Dan Zimmerman, Aishwarya Jawne, Alexandra Rozin

### Project Description
Natural language chatbot application with travel information curated for digital nomads and expatriates. The application is built using Python, Streamlit, and ElasticSearch.  The chatbot is built using OpenAI's GPT-3.5 API.

## Installation Instructions

**NOTE:** This will not work on Windows.  It will work on WSL or any flavor of Linux, and probably on MacOS.

1. Create and activate a new virtual environment.  
2. Clone or fork the repo into that venv.
3. Run `pip install -r requirements.txt` to install dependencies.
4. Make a new file called `.env` in the root directory.  In it store the following:
   - openai_api="<your OpenAI API key>"
   - cloud_id="<you Elastic Cloud ID>"
   - cloud_user="<Your Elastic username>"
   - cloud_pass="<your Elastic password>"
5. Run `streamlit run elasticdocs_gpt.py` to start the streamlit application.  When finished, the Streamlit app will be running locally at http://172.23.145.28:8501.  You do not need to open that URL.
6. Run `uvicorn main:app –reload` to start the main server.
7. Open http://localhost:8000 in a web browser to run the app.

**App Screens**
![image](https://github.com/ashi-jne/Nomadiq-AIchatbot-App/assets/96357892/38e3d00d-9c58-49d6-ab43-b7fbfdf92bce)
Landing Page

![image](https://github.com/ashi-jne/Nomadiq-AIchatbot-App/assets/96357892/c60e9e77-c5f8-42c0-a80a-373412d77191)
Login Page

![image](https://github.com/ashi-jne/Nomadiq-AIchatbot-App/assets/96357892/5c330e18-6599-4d05-9b82-1b4ccc655beb)
Explore/AI Chat Page

![image](https://github.com/ashi-jne/Nomadiq-AIchatbot-App/assets/96357892/217cded8-74e7-41d5-bb18-c588450604bb)
AI Chat in Action in Explore Page


User Flow:
![image](https://github.com/ashi-jne/Nomadiq-AIchatbot-App/assets/96357892/f2d923e3-71b4-4ec5-b1e9-23c02df92fc6)

UML:
![image](https://github.com/ashi-jne/Nomadiq-AIchatbot-App/assets/96357892/a05a0d19-fc0f-4d90-8529-ab3d7dda4ad7)











