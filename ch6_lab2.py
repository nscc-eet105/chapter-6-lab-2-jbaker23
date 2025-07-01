import matplotlib.pyplot as plt



def main():
    print("This program will graph a line when given the slope and the intercept.")
    print("Please enter the values for m and b given the form y = m * x + b") 
    try:
        m = float(input("Enter the slope (m): "))
        b = float(input("Enter the y-intercept (b): "))
    except ValueError:
        print("Please enter valid numbers for m and b.")
        return
    
    x_values = [x for x in range (-20, 20)]

    y_values = [m * x + b for x in x_values]
    
     
    plt.grid(True)
    plt.axhline(y=0, color='r')
    plt.axvline(x=0, color='r')

    plt.plot(x_values, y_values)

    plt.show()
            




main()
