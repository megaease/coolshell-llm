from llmtuner import ChatModel

try:
    import platform
    if platform.system() != "Windows":
        import readline
except ImportError:
    print("Install `readline` for a better experience.")


def main():
    chat_model = ChatModel()
    print("Welcome to MegaEase CoolShell LLM demo. Use `exit` to exit the application.")

    while True:
        try:
            query = input("\nUser: ")
        except UnicodeDecodeError:
            print("Detected decoding error at the inputs, please set the terminal encoding to utf-8.")
            continue
        except Exception:
            raise

        if query.strip() == "exit":
            break

        for new_text in chat_model.stream_chat(query, []):
            print(new_text, end="", flush=True)
        print()

if __name__ == "__main__":
    main()