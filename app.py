import streamlit as st
import wikipediaapi
import pyperclip

# Function to fetch Wikipedia summary for a given query
def get_wiki_summary(query):
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent='my-wikipedia-bot/1.0'  # Replace with your own user agent
    )
    page_obj = wiki_wiki.page(query)
    if page_obj.exists():
        return page_obj.summary
    else:
        return "Sorry, I couldn't find any relevant information on that topic."

# Main function to run the Streamlit app
def main():
    st.title("Wikipedia ChatBot")
    st.markdown("Ask me about anything, and I will try to provide a summary.")

    user_input = st.text_input("You:")
    if st.button("Ask"):
        if user_input.strip():
            # Fetch summary from Wikipedia
            response = get_wiki_summary(user_input.strip().lower())
            st.text_area("Wikipedia:", value=response, height=300)
            
            # Add a button to copy text to clipboard
            if st.button("Copy to Clipboard"):
                pyperclip.copy(response)
                st.success("Text copied to clipboard!")
            
        else:
            st.warning("Please enter a topic to search.")

# Run the app
if __name__ == "__main__":
    main()
