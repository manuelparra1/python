import json
from openai import OpenAI
from env import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)

model = "gpt-3.5-turbo-1106"
temperature = 1
max_tokens = 4096
top_p = 1
frequency_penalty = 0
presence_penalty = 0

# Empty conversation history to start
conversation_history = []

while True:
    # Get user input for the next part of the conversation
    user_input = input("Enter your message (type 'exit' to finish): ")

    # If it's the first input, set it as the initial prompt
    if not conversation_history:
        conversation_history.append({"role": "user", "content": user_input})
    else:
        # Append the user's input to the conversation history dictionary
        conversation_history.append({"role": "user", "content": user_input})

    # Generate response using the entire conversation history dictionary
    response = client.chat.completions.create(
        model=model,
        messages=conversation_history,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )

    # Print the model's response
    print(response.choices[0].message.content)

    # Append the model's response to the conversation history dictionary
    conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})

    # Check if the user wants to exit the loop
    if user_input.lower() == 'exit':
        # Save the conversation history to a JSON file
        with open('conversation_history.json', 'w') as json_file:
            json.dump(conversation_history, json_file, indent=2)
        break
