import importlib

def get_user_choice():
    chefs = {
        1: ("The Wise Italian Chef", "teacherjavier_ChefGPT"),
        2: ("The Vibrant Mexican Street Food Chef", "F0x_ChefGPT"),
        3: ("The French Pastry Maestro Chef", "NicolasV_ChefGPT"),
        4: ("The Japanese Kaiseki Virtuoso Chef", "Nada_J_ChefGPT"),
        5: ("The Traditional Chinese Dim Sum Chef", "FranSarr_ChefGPT"),
        6: ("The Innovative Indian Fusion Chef", "Arkano_eth_ChefGPT"),
        7: ("Exit", None)
    }
        
    print("\nWelcome to our culinary experience! Here are our finest chefs, each with their unique culinary expertise:")
    for key, (name, _) in chefs.items():
        print(f"{key}. {name}")

    
    while True:
        try:
            choice = int(input("\nWho will be guiding your culinary journey today? Enter their number (or choose '5' to exit): "))
            if choice in chefs:
                return chefs[choice]  
            else:
                print("Oops! It seems like an invalid number. Please choose a chef from the list above.")
        except ValueError:
            print("Hmm, that doesn't look like a number. Could you try entering it again?")

def main():
    while True:  
        chef_name, chef_module_name = get_user_choice()
        
        if chef_module_name is None:  
            print("Thank you for visiting our culinary experience. Bon appétit!")
            break

        
        chef_module = importlib.import_module(chef_module_name)
        chef_module.main()

        
        continue_choice = input("\nWould you like to consult another chef? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Thank you for joining our culinary journey. We hope to see you again soon!")
            break

if __name__ == "__main__":
    main()
