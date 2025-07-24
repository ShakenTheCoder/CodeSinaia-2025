import ollama

model = "gemma3:1b"
chat_context = []
#append the context_prompt.txt file to the chat context
with open("CodeSinaia-2025\IntroToLLM\context_prompt.txt", "r") as file:
    context = file.read()
chat_context.append({"role": "system", "content": context})
#rint("the loaded context is:")
#rint(chat_context[0]["content"])
print("Welcome to the AI WiFi Helper!")
print("Context loaded. You can start asking questions.")
print("Type '/exit' to end the chat.")
while True:
    prompt = input("Ask a question: ")
    if prompt == "/exit":
        print(chat_context)
        chat_context = [" "]
        break
    if prompt != "":
        print("Processing your question...")
        chat_context.append({"role": "user", "content": prompt})
        response = ollama.chat(model = model, messages = chat_context)
        print(response["message"]["content"])
        chat_context.append({"role": "system", "content": response["message"]["content"]})