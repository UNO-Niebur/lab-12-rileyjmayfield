# SearchSortLab.py
# Name: Riley Mayfield
# Date: 4/22
# Assignment: Lab 13 – Searching and Sorting
# Purpose: Develop understanding of sorting lists


def linearSearch(data, target):
    """Return the index of target if found, otherwise return -1."""
    
    # TODO: implement linear search
    for i in range(len(data)):
        if data[i] == target:
            return i


    return -1


def bubbleSort(data):
    """Sort the list using bubble sort and return the sorted list."""
    
    # TODO: implement bubble sort

    for j in range(len(data)):
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
    
    return data


def main():
    # Test lists
    sortedList = [1, 2, 3, 4, 5]
    reversedList = [5, 4, 3, 2, 1]
    randomList = [3, 1, 4, 2, 5]

    # Test linear search
    print("Search for 4 in randomList:", linearSearch(randomList, 4))
    print("Search for 10 in randomList:", linearSearch(randomList, 10))

    # Test sorting
    print("Sorted list:", bubbleSort(sortedList.copy()))
    print("Reversed list sorted:", bubbleSort(reversedList.copy()))
    print("Random list sorted:", bubbleSort(randomList.copy()))


if __name__ == "__main__":
    main()
