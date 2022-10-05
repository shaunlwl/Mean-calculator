import mean_calculator

def main():
    
    dataset1 = mean_calculator.MeanCalculator()
    dataset2 = mean_calculator.MeanCalculator()
    dataset1.LoadDataset()
    print("New input")
    dataset2.LoadDataset()
    print("New input")
    dataset1.LoadDataset()
    dataset1.RemovefromDataset([2,3])
    dataset2.RemovefromDataset([3,5])
    dataset2.UpdateDataset([8,6],[8,8])

    print(dataset1.calculateArithmeticMean())
    print(dataset2.calculateGeometricMean())




if __name__ == "__main__":
    main()
