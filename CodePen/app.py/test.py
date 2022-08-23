def selection():
    select = input("Please select A: ")

    while select.upper() != "A":
        print("wrong input. Try Again")
    
        return selection()
    
    
    print("Hi")
    
    

selection()