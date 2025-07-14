from agent.customer_agent import create_agent


def main():
    agent = create_agent()
    print("Agent is ready. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = agent.run(user_input)
        print("Agent:", response)
        

if __name__ == "__main__":
    main()