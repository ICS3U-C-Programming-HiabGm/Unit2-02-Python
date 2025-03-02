# Created by: Hiab G
# Date: Wed, Feb. 28th
# This program asks the user for the radius and then calculates the circumference of a circle using tau.
import constants


def main():
    # Get the radius from the user
    radius = float(input("Enter the radius of the circle (mm): "))

    # Calculate the circumference
    circumference = constants.TAU * radius

    # Display the circumference
    print("Circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()
