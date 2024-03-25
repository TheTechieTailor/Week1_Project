# The Mexican Street Food Chef
from openai import OpenAI

client = OpenAI()

model = "gpt-3.5-turbo"

def handle_option(option, data):
    messages = [
        {
            "role": "system",
            "content": "You are a lively and passionate chef, known for your mastery of Mexican street food. Your dishes celebrate bold flavors and fresh ingredients."
        },
        {
            "role": "user",
            "content": ""
        }
    ]
    if option == 1:
        messages[1]["content"] = f"Using your expertise in Mexican street food, suggest a dish name using these ingredients: {data}?"
    elif option == 2:
        messages[1]["content"] = f"Can you provide a detailed recipe for a traditional Mexican dish such as {data}?"
    elif option == 3:
        messages[1]["content"] = f"How would you critique this Mexican street food recipe and suggest improvements: {data}?"
    
    try:
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)
        return "".join(collected_messages)
    except Exception as e:
        print(f"An error occurred while contacting the OpenAI service: {e}")
        return "I'm sorry, but I couldn't process your request right now."

def prompt_user():
    options = {
        1: "Find dishes you can make with your ingredients",
        2: "Get detailed recipes for specific dishes",
        3: "Receive critique and improvement suggestions for recipes"
    }
    
    print("\nSelect an option (1, 2 or 3):")
    for key, value in options.items():
        print(f"{key}. {value}")

    option = 0
    while True:
        try:
            option = int(input("Your choice: "))
            if option in [1, 2, 3]:
                break
            else:
                print("Please select a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    data = ""
    if option == 1:
        data = input("Enter ingredients (comma-separated): ").strip()
    elif option == 2:
        data = input("Type the name of the dish you want a recipe for: ").strip()
    elif option == 3:
        data = input("Enter the recipe to criticize: ").strip()
    
    return option, data

def main():
    print("Welcome to the AI Mexican Chef Assistant!")

    while True:
        option, data = prompt_user()
        response = handle_option(option, data)

        continue_choice = input("\nDo you want to continue? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Thank you for exploring the streets of Mexico with our AI Mexican Street Food Chef Assistant. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()

