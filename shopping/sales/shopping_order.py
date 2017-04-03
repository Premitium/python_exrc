class Order:

    def __init__(self):
        self.quit = False
        self.add = False
        self.remove = False
        self.item = None

    def get_input(self):
        print("[command] [item] (cammand is a to add, d to delete, q to quit)")
        line = input()
        command = line[:1]
        self.item = line[2:]
        
        if command == "a":
            self.add = True
        if command == "d":
            self.delete = True
        if command == "q":
            self.quit = True
        
