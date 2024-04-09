class NarryNode:
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
            self.children.insert(index, NarryNode(value))
        else:
            for child in self.children:
                if child.value >= value:
                    child.insert(value)
                    return
            self.children[-1].insert(value)

    def delete(self, value):
        if self.value == value:
            if self.children:
                self.value = self.children[0].value
                self.children.pop(0)
            else:
                return True
        found = False
        for child in self.children:
            if child.delete(value):
                found = True
                if len(child.children) < 2:
                    self.children.remove(child)
                break
        return found

    def delete_and_print_not_found(self, value):
        if not self.delete(value):
            print("Not found")

if __name__ == '__main__':
    # Example usage
    root = NarryNode(10)
    root.insert(5)
    root.insert(15)
    root.insert(8)
    root.insert(12)
    root.insert(20)
    root.insert(17)
    root.insert(3)
    root.insert(4)
    root.insert(1)
    root.insert(9)
    root.insert(4.5)
    root.insert(8.5)
    root.insert(7)
    root.insert(4.6)
    root.delete_and_print_not_found(5558)
    print(root)
