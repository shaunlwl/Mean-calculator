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
            except ValueError:
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

class MeanCalculator:

    def __init__(self):
        self.dataset = []

    def calculateArithmeticMean(self):
        return calculate_arithmetic_means(self.dataset)
    
    def calculateGeometricMean(self):
        return calculate_geometric_means(self.dataset)

    def calculateHarmonicMean(self):
        return calculate_harmonic_means(self.dataset)

    def LoadDataset(self):
        self.dataset += get_numbers()
    
    def RemovefromDataset(self, list_of_numbers_remove):
        for numbers in list_of_numbers_remove:
            self.dataset.remove(numbers)
        
    def UpdateDataset(self, old_data , updated_data):
        self.RemovefromDataset(old_data)
        for i in updated_data:
            self.dataset.append(i)
            
        