import math

def iszapreadable(page_number_list):
    # Directly return false if number of pages is odd
    if len(page_number_list) % 2 != 0:
        return False

    # If power of two, check second construction method
    if math.log2(len(page_number_list)).is_integer():
        # Set the start index
        idx = 0

        # Initialize the next wanted page number
        next_page_number = 1

        # Set a break variable to get out of while loop when not zap readable using the second construction method
        stop = False

        while next_page_number <= len(page_number_list) and not stop:
            # To be zap readable, subsequent page reads should have their page numbers in oder
            if (page_number_list[idx] == next_page_number):
                idx += next_page_number 
                idx = idx % len(page_number_list)
                next_page_number += 1
            else:
                stop = True

        if not stop:
            return True

    # If number of pages is even, check first construction method
    if len(page_number_list) % 2 == 0:
        # Set a new break variable
        stop = False

        # Initialize the index
        idx = 0

        while idx != len(page_number_list) and not stop:
            # If the index is in the first half of the list, the page number should be length - (idx*2+1)
            if idx < len(page_number_list)/2:
                stop = False if (page_number_list[idx] == len(page_number_list) - (idx*2 + 1)) else True 
                idx += 1

            # If the index is in the second half of the list, the page number should be length - (idx-(length/2))*2
            elif idx >= len(page_number_list)/2:
                stop = False if (page_number_list[idx] == len(page_number_list) - (idx - (len(page_number_list)/2))*2) else True
                idx += 1

        if not stop:
            return True

    return False

def zapbook(number_of_pages):
    # If the number of pages is odd, return empty book
    if number_of_pages != 1 and number_of_pages % 2 != 0:
        return []

    # If number of pages is one, just return book with one page
    if number_of_pages == 1:
        return [1]

    # Otherwise, start with an empty list
    book = [None] * number_of_pages

    # If power of two, use second construction method
    if math.log2(number_of_pages).is_integer():
        # Initialize start index
        idx = 0

        # Set the next page number
        next_page_number = 1

        while next_page_number <= number_of_pages:
            # To be zap readable, subsequent page reads should have their page numbers in oder
            book[idx] = next_page_number

            # Set the next index that needs to be visited
            idx += next_page_number 
            idx = idx % number_of_pages

            # Set the next page number that needs to be set
            next_page_number += 1

        return book

    # if even, use first construction method
    if number_of_pages % 2 == 0:
        for idx in range(0, number_of_pages):
            # If the index is in the first half of the list, the page number should be length - (idx*2+1)
            if idx < number_of_pages/2:
                book[idx] = int(number_of_pages - (idx*2 + 1))

            # If the index is in the second half of the list, the page number should be length - (idx-(length/2))*2
            elif idx >= number_of_pages/2:
                book[idx] = int(number_of_pages - (idx - (number_of_pages/2))*2)

        return book


if __name__ == "__main__":
    print(iszapreadable([7,5,3,1,8,6,4,2]))
    print(iszapreadable([1,2,4,7,3,8,6,5]))
    print(iszapreadable([1,2,5,3,8,7,4,6]))
    print(iszapreadable([1,1,1,1,1,1,1,1]))

    print(zapbook(6))
    print(zapbook(7))
    print(zapbook(8))
