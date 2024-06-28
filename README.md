**Wikipedia ChatBot**

The Wikipedia ChatBot is a simple web application built using Streamlit and the Wikipedia API. It allows users to fetch and display summaries of Wikipedia articles based on their queries.

**Features**
**Search**: Enter any topic or query in the input box to fetch a summary from Wikipedia.
**Display**: Displays the retrieved Wikipedia summary in a text area.
**Copy to Clipboard**: Option to copy the displayed summary to the clipboard for easy sharing or further use.


**Install Dependencies:**

Ensure **Python** and pip are installed.
Install required libraries using:
Copy code
pip install streamlit wikipedia-api pyperclip
Run the App:

Navigate to the directory containing app.py.

Run the app using Streamlit:

arduino
Copy code
streamlit run app.py
The app will open in your default web browser.
Interact with the App:

Enter a topic or query in the text input and click "Ask".
The Wikipedia summary for the entered query will be displayed.
Use the "Copy to Clipboard" button to copy the summary text for sharing or saving.
Deployment
Local Deployment:

Use Streamlit to run the app locally for testing and development.
Cloud Deployment:

Deploy the app to Streamlit Sharing or other cloud platforms for public access.
Dependencies
Python 3.x
Streamlit
Wikipedia API (wikipedia-api)
Pyperclip (for copying text to clipboard)
