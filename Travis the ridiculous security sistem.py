Known_users = ["Anderson", "Luiz", "Daniel", "Alice", "Artur", "Vinicius", "Vitoria"]
print(len(Known_users))
while True:
    print("Hi, my name is Travis")
    name=input("What is your name?: ").strip().capitalize()
    
    if name in Known_users:
        print("hello {}!".format(name)) 
        remove = input("Would you like to be removed from the system? (y/n?)").strip().lower()
        if remove == "y":
            Known_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
    else:
        print("Hmmm... i don't think i have met you yet{}".format(name))
        add_me = input("Would you like to be added to the system? (y/n?)").strip().lower()
        if add_me == "y":
            Known_users.append(name)
        elif add_me == "n":
            print("No worries, see you around.")

       

