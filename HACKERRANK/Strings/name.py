def print_full_name(first, last):
    if len(first_name)<=10 and len(last_name)<=10:
        name=print(f"Hello {first_name} {last_name}! You just delved into python.")
        return name
    else:
        return "First and Last Name should be less than or equal to 1o"
    
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)