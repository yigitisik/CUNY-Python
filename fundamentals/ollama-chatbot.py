from ollama import Client
MODEL = "gemma3:4b"   # make sure this matches `ollama list`

client = Client()  # defaults to http://localhost:11434

def ask_ollama(message, history, stream_output):
    resp = client.chat(
        model=MODEL,
        messages=history + [{"role": "user", "content": message}],
        stream=stream_output,
    )

    if not stream_output:
        return resp["message"]["content"]

    # streaming mode
    full = ""
    for part in resp:
        if "message" in part:
            full += part["message"].get("content", "")
            print(part["message"].get("content", ""), end="", flush=True)
    print()
    return full


def main():
    print("🟢 Local Ollama Chatbot started")
    print("Type 'exit' to quit.\n")
    history = []

    while True:
        user_msg = input("You: ")
        if user_msg.lower() == "exit":
            break
        answer = ask_ollama(user_msg, history, False) #can toggle true or false for streaming resp
        print("\nOllama:", answer, "\n")

        history.append({"role": "user", "content": user_msg})
        history.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    main()
