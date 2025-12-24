from utils.ask_assistant import ask_assistant

print("Movie Recommendation Assistant")
print("=" * 50)

queries = [
    "I want to watch a good action movie tonight",
    "Recommend me something funny",
    "What's a good sci-fi movie?",
    "I'm in the mood for horror",
    "What's the weather like today?"
]

for q in queries:
    print(f"\nQuery: {q}")
    response = ask_assistant(q)

    if isinstance(response, dict):
        print("Response:")
        print(response)
    else:
        print("Response:", response)

    print("-" * 40)
