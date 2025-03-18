from collections import defaultdict

class MultiValueDict:
    # This program must store all key value pairs as strings
    def __init__(self):
        self.store = defaultdict(set)

    def keys(self):
        if not self.store:
            print("(empty set)")
        else:
            # Enumerates over the store's keys, starting at 1
            for i, key in enumerate(self.store.keys(), 1):
                print(f"{i}) {key}")

    def members(self, key):
        if key not in self.store:
            print(") ERROR, key does not exist.")
        else:
            # Enumerates over the requested key, starting at 1
            for i, member in enumerate(self.store[key], 1):
                print(f"{i}) {member}")

    def add(self, key, member):
        # Adds a member to a collection for a given key. Displays an error if the member already exists for the key.
        # This means we can use a set as the value for each key added
        if member in self.store[key]:
            print(") ERROR, member already exists for key")
        else:
            self.store[key].add(member)
            print(") Added")
    # removes a member from the collection for a given key
    def remove(self, key, member):
        if key not in self.store:
            print(") ERROR, key does not exist")
        elif member not in self.store[key]:
            print(") ERROR, member does not exist")
        else:
            self.store[key].remove(member)
            print(") Removed")
            if not self.store[key]:
                del self.store[key]
    # removes all members for a given key and removes the key from the dictionary as well
    def remove_all(self, key):
        if key not in self.store:
            print(") ERROR, key does not exist")
        else:
            del self.store[key]
            print(") Removed")
    # removes all keys and members from the dictionary
    def clear(self):
        self.store.clear()
        print(") Cleared")
    # checks to see if key exists in the dictionary
    def key_exists(self, key):
        print(") true" if key in self.store else ") false")
    # checks to see if a member exists for a specific key
    def member_exists(self, key, member):
        if key in self.store and member in self.store[key]:
            print(") true")
        else:
            print(") false")
    # prints all members (not keys) in the dictionary
    def all_members(self):
        # The outer loop (for values in self.store.values()) iterates over each set of members
        # The inner loop (for m in values) iterates over each individual member inside a set
        # Members is a flatenned list of all the members in self.store
        members = [m for values in self.store.values() for m in values]
        if not members:
            print("(empty set)")
        else:
            for i, member in enumerate(members, 1):
                print(f"{i}) {member}")
    # prints all keys in the dictionary including all of the keys' members
    def items(self):
        if not self.store:
            print("(empty set)")
        else:
            # List comprehension
            # Returns all keys in the dictionary and all of their members. Returns nothing if there are none. Order is not guaranteed.
            print("\n".join(f"{key}: {value}" for key, values in self.store.items() for value in values))
    # Alternate implementation:
    # def items(self):
    #     if not self.store:
    #         print("(empty set)")
    #     else:
    #         for key, values in self.store.items():
    #             for value in values:
    #                 print(f"{key}: {value}")

def main():
    db = MultiValueDict()
    command_dispatch = {
        # Lambdas for conciseness of code
        "ADD": 
            lambda args: db.add(*args) if len(args) == 2 else print(") ERROR, incorrect number of arguments"),
        "REMOVE": 
            lambda args: db.remove(*args) if len(args) == 2 else print(") ERROR, incorrect number of arguments"),
        "REMOVEALL": 
            lambda args: db.remove_all(*args) if len(args) == 1 else print(") ERROR, incorrect number of arguments"),
        "KEYS": 
            lambda args: db.keys() if not args else print(") ERROR, incorrect number of arguments"),
        "MEMBERS": 
            lambda args: db.members(*args) if len(args) == 1 else print(") ERROR, incorrect number of arguments"),
        "CLEAR": 
            lambda args: db.clear() if not args else print(") ERROR, incorrect number of arguments"),
        "KEYEXISTS": 
            lambda args: db.key_exists(*args) if len(args) == 1 else print(") ERROR, incorrect number of arguments"),
        "MEMBEREXISTS": 
            lambda args: db.member_exists(*args) if len(args) == 2 else print(") ERROR, incorrect number of arguments"),
        "ALLMEMBERS": 
            lambda args: db.all_members() if not args else print(") ERROR, incorrect number of arguments"),
        "ITEMS": 
            lambda args: db.items() if not args else print(") ERROR, incorrect number of arguments"),
        "EXIT": 
            lambda args: exit(), # When called inside the main loop, exits immediately
    }

    while True:
        '''
        Command prompts the user to enter a command after "> ".
        strip() will remove leading/trailing whitespaces
        split() breaks the input into a list of strings
        '''
        command = input("> ").strip().split()
        # command will be empty list if "enter" is pressed without any args, and will simply restart loop
        if not command:
            continue
        
        # Unpacking of command list
        # action = "ADD"
        # args = ["key1", "value1"]
        # *args allows a function to accept any number of positional arguments. It collects them into a tuple
        action, *args = command
        # converts to upper case so "add" and "ADD" will be same command
        action = action.upper() 

        command_dispatch.get(action, lambda args: print(") ERROR, unknown command"))(args)

if __name__ == "__main__":
    main()
