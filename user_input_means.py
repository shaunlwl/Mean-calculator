import sys
import mean_calculator

while True:
    nums = mean_calculator.get_numbers()
    if nums ==[]:
        print("List of numbers provided is empty, pls input again")
        continue
    else:
        while True:
            user_choice = input("What is the mean required for calculation? Please choose one option: Arithmetic, Geometric or Harmonic ""\n""").lower()
            if user_choice == "arithmetic":
                print(mean_calculator.calculate_arithmetic_means(nums))
                while True:
                    user_choice_1 = input("Do you want to calculate another mean? Y/N/New dataset ""\n""")
                    if user_choice_1 in ["Y", "N", "New dataset"]:
                        break
                    else:
                        print("You have entered an invalid input, pls try again")     
            elif user_choice == "geometric":
                print(mean_calculator.calculate_geometric_means(nums))
                while True:    
                    user_choice_1 = input("Do you want to calculate another mean? Y/N/New dataset ""\n""")
                    if user_choice_1 in ["Y", "N" , "New dataset"]:
                        break
                    else:
                        print("You have entered an invalid input, pls try again") 
            elif user_choice == "harmonic":
                print(mean_calculator.calculate_harmonic_means(nums))
                while True:    
                    user_choice_1 = input("Do you want to calculate another mean? Y/N/New dataset ""\n""")
                    if user_choice_1 in ["Y", "N", "New dataset"]:
                        break
                    else:
                        print("You have entered an invalid input, pls try again") 
            else:
                print("You have entered an invalid mean, pls try again")
                continue
            if user_choice_1 == "Y":
                continue
            else:
                break        

    if user_choice_1 == "New dataset":
        continue
    else:
        user_choice_3 = input("Do you have more datasets to process? Y/N ""\n""")
        if user_choice_3 in ["Y", "N"]:
            if user_choice_3 == "Y":
                pass
            else:
                sys.exit()
        else:
            while True:
                print("You have entered an invalid input , pls try again")
                user_choice_3 = input("Do you have more datasets to process? Y/N ""\n""")
                if user_choice_3 in ["Y", "N"]:
                    if user_choice_3 == "Y":
                        break
                    elif user_choice_3 == "N":
                        sys.exit()
                else:
                    pass