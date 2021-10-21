"""
Author : T. Dhar
Date : 21.10.2021
"""




def LinearSearch(array,key):
    flag = False
    for i in range(0,len(array)):
        if array[i]==key :
            flag = True
            print("The element is in the {} position".format(i+1))
    if not flag:
        print("Key not found.")


def main():
    array = eval(input("Enter the array : "))
    key = eval(input("Enter the key to be found : "))
    LinearSearch(array,key)



if __name__ == '__main__':
    main()
