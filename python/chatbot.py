import openai

# Set up your OpenAI API key
api_key = "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"
openai.api_key = api_key

def get_chatbot_response(user_input):
    # Prepare the chatbot prompt or messages
    chatbot_prompt = "User: " + user_input + "\nChatGPT:"

    # Call the API to get the chatbot's response
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the appropriate engine ID for ChatGPT
        prompt=chatbot_prompt,
        max_tokens=150,  # Control the length of the response
        stop=["\n"],  # Stop the response at the end of the current chat turn
    )

    # Extract and return the chatbot's reply from the API response
    chatbot_reply = response["choices"][0]["text"].strip()
    return chatbot_reply
