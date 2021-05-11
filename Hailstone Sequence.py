"""
Python program that reads in a number from the user and 
then displays the Hailstone sequence for that number.

Pick some positive integer and call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    n = int(input("Enter a number: ")) #user input
    counter = 0

    while(True):
        if n == 1:
            break
        else:                   #iterate until number becomes 1
            temp = n
            counter += 1
            if n % 2 != 0:     #if number is odd
                n = n * 3 + 1
                print(str(temp) + ' is odd, so I make 3n + 1: ' + str(n))
            else:                   #if number is even
                n //= 2
                print(str(temp) + ' is even, so I take half: ' + str(n))

    print('The process took ' + str(counter) + ' steps to reach 1')

if __name__ == "__main__":
    main()
