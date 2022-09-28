def get_number():
    '''This function returns a given number provided by a user'''
    while True:
        num = input("Pls input a number: ""\n""")
        if num == "":
            return None
        elif num.isdigit():
            num = int(num)
            return num   
        else:
            try:    
                num = float(num)
                return num
            except:
                print("You have provided an invalid input, pls try again")

def get_numbers():
    '''This function gets a list of numbers by calling the function get_number'''
    num_list = []
    while True:
        num = get_number()
        if num == None:
            return num_list
        else:
            num_list.append(num)

def calculate_arithmetic_means(nums):
    avg= 0
    if nums == []:
        return None
    else:
        for i in nums:
            avg+= i
        return avg/len(nums)

        
def calculate_geometric_means(nums):
    avg= 1
    if nums == []:
        return None
    else:
        for i in nums:
            avg*= i
        return avg**(1/len(nums))



def calculate_harmonic_means(nums):
    avg= 0
    if nums == []:
        return None
    else:
        for i in nums:
            avg+= 1/i
        return len(nums)/avg