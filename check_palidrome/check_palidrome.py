def is_palidrome(string):
    ptr_start = 0
    ptr_end = len(string) - 1
    while ptr_start < ptr_end:
        while ptr_start < ptr_end and not string[ptr_start].isalpha():
            ptr_start += 1
        while ptr_end > ptr_start and not string[ptr_end].isalpha():
            ptr_end -= 1
        if string[ptr_start].lower() != string[ptr_end].lower():
            return False 
        else:
            ptr_start += 1
            ptr_end -= 1
    return True

if __name__ == "__main__":
    while True:
        print(is_palidrome(input()))
        print(" ")
