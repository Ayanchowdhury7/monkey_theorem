def checker():
    import random #import random for randomly choose the string
    import string #it helps to call string.ascii_letters

    size = 0 #length of input string
    counts = -1 #no of time ice bear try to write whole string
    turns = 0 # counts divided by 100

    characters = string.ascii_letters + string.whitespace + string.punctuation + string.digits  #refernce to the ascii letters.
    desired_list = [] #blank list to store input string as a list
    desired_string = input("Enter your text: ") #user input

    size = len(desired_string) #length of input string
    
    for ch in desired_string:
        desired_list.append(ch) #helps to unpack the string into list


    checked_list = [] #blank list to store ice bears predictions

    while checked_list != desired_list: #check the user string to ice bear's string
        counts = counts + 1 # ice bear is dumb, so counts = -1 , line 6
        checked_list = [random.choice(characters) for _ in range(size)] #ice bear try to write
    else:
        counts = counts + 1 #if lists are matched while statements skipped so we have to count for last time
        turns = round (counts / 100) #simply divide the counts by 100, and rounded it for better looking result
        print(''.join(checked_list)) #to see, ice bear doing good job
        print(f"Ice bear write exactly same in {turns} times.") #ice bear is tired, but he reaches to the north pole :)


checker() # calling the function

