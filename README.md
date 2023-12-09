# CEN5035 Software Engineering - Final Project
**Group 5:** Aishwarya Jawne, Alexandra Rozin, Dan Zimmerman

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
