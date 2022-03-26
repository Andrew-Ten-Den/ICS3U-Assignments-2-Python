#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: March 23 2022
# This program calculates the volume of a rectangular prism
# with length, width and height inputted from the user


def main():
    # This program calculates the volume of a rectangular prism

    # input
    length = int(input("Enter length of the rectangular prism (cm): "))
    width = int(input("Enter width of the rectangular prism (cm): "))
    height = int(input("Enter height of the rectangular prism (cm): "))

    # process
    area = length * width * height

    # output
    print("")
    print("Volume is {} cm³.".format(area))
    print("")
    print("Done")


if __name__ == "__main__":
    main()
