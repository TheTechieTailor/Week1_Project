# The Innovative Indian Fusion Chef
from openai import OpenAI

client = OpenAI()

model = "gpt-3.5-turbo"

def handle_option(option, data):
    messages = [
        {
            "role": "system",
            "content": "You are a visionary chef who blends traditional Indian flavors with global culinary techniques, creating modern fusion dishes that dazzle the palate."
        },
        {
            "role": "user",
            "content": ""
        }
    ]
    if option == 1:
        messages[1]["content"] = f"Using your innovative fusion approach, suggest a dish name that creatively combines these ingredients: {data}?"
    elif option == 2:
        messages[1]["content"] = f"Can you provide a detailed recipe for an Indian fusion dish such as {data}, incorporating both traditional and modern culinary techniques?"
    elif option == 3:
        messages[1]["content"] = f"As an expert in Indian fusion cuisine, how would you critique this recipe and suggest improvements for a more innovative fusion approach: {data}?"
    
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
    print("Welcome to the AI Indian Chef Assistant!")

    while True:
        option, data = prompt_user()
        response = handle_option(option, data)

        continue_choice = input("\nDo you want to continue? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Thank you for embarking on a culinary fusion journey with our AI Indian Fusion Chef Assistant. Alvida!")
            break

if __name__ == "__main__":
    main()