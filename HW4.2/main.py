class TreeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} Value: {self.value}"


class TreeValueDoesNotExist(TreeError):
    def __init__(self, value):
        message = f"Value '{value}' does not exist in the tree."
        super().__init__(message, value)


class TreeIllegalValue(TreeError):
    def __init__(self, value):
        message = f"Value '{value}' is illegal value."
        super().__init__(message, value)


class Narry:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        children_info = ' ; '.join(str(child) for child in self.children)
        if children_info:
            return f"{self.value} [{children_info}]"
        else:
            return str(self.value)

    def __repr__(self):
        return f"NarryNode({repr(self.value)})"

    def insert(self, value):
        if self.value == value:
            print("Value already exists in the tree.")
            return
        if len(self.children) < 4:
            index = 0
            while index < len(self.children) and self.children[index].value < value:
                index += 1
            if index < len(self.children) and self.children[index].value == value:
                print("Value already exists in the tree.")
                return
            self.children.insert(index, Narry(value))
        else:
            for child in self.children:
                if child.value >= value:
                    child.insert(value)
                    return
            self.children[-1].insert(value)
    def delete(self, value):
        if self.value == value:
            return True
        found = False
        for child in self.children:
            if child.delete(value):
                found = True
                self.children.remove(child)
                break
        return found


if __name__ == '__main__':
    tree = None
    while True:
        try:
            print("Menu:")
            print("1. Create a tree")
            print("2. Add a value to the tree")
            print("3. Delete a value from the tree")
            print("4. Print the tree")
            print("5. Exit\n")

            choice = int(input("Enter your choice:\n"))

            if choice == 1:
                value = int(input("Enter a value to enter the tree:\n"))
                tree = Narry(value)
            elif choice == 2:
                if not tree:
                    raise UnboundLocalError
                value = int(input("Enter a value to enter the tree:\n"))
                tree.insert(value)
            elif choice == 3:
                if not tree:
                    raise UnboundLocalError
                try:
                    value = input("Enter a value you want to delete:\n")
                    if not value.isdigit():
                        raise TreeIllegalValue(value)
                    notFound = tree.delete(value)
                    if not notFound:
                        raise TreeValueDoesNotExist(value)
                except TreeValueDoesNotExist as e:
                    print(e)
                except TreeIllegalValue as e:
                    print(e)
            elif choice == 4:
                print(tree)
            elif choice == 5:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except UnboundLocalError:
            print("Option not available. Please create a tree first.")
        except TreeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
