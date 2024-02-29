from dataclasses import dataclass
from typing import NoReturn


# structure of a Node of LinkedList
@dataclass
class Node[node]:
    data: any
    next: node | None = None


# main LinkedList class
class LinkedList:
    """
    My implementation of linked list. I had also implemented indexing and slicing in it.

    Attributes: 
        - `head` (Node or None): head of the LinkedList, default None.
        
    Functions: Look over to the respective functions for detailed information about them.
        - `append`: It is used to append an element to the LinkedList.
        - `display_element`: Displays the elements of the LinkedList.
        - `remove`: Removes an existing element from the LinkedList.
        - `to_pylist`: Converts the LinkedList to python's list object and return it.
        - `get`: Returns the element whose index is provided, if index out of range returns None.
        - `__getitem__`: Implements indexing and slicing to the LinkedList.
        - `__setitem__`: Implements item assignment to LinkedList.
        - `__len__`: Returns the length of LinkedList.

    Usage: Create an object of LinkedList class.
        ```
        l1 = LinkedList()
        ```

    Example: 
        ```
        l1 = LinkedList()
        l1.append(8, 7, 'hello')        # you can simply use other functions like this.
        print(l1.head, l1.head.next)    # head and its next element can be accessed like this.
        l1[::-1]                        # indexing can be performed this way.
        l1[0] = 9                       # item assignment.
        print(len(l1))                  # to print the length of l1.

        for i in l1:                    # we can also iterate through it.
            print(i.head)
        ```

    Note: 
        - Errors might be raised when wrong input is provided. Handle them if necessary.
        - data of Node class can be any object, even another LinkedList object.
        - None is considered as end of LinkedList, so don't add None in it (this will cause loss of data).
    """

    def __init__(self) -> None:
        self.head: Node | None = None

    def append(self, *values: any) -> None:
        """
        This method appends the provided arguments (*values) to the end of the LinkedList. 
        If there are no elements in the LinkedList, then the first elment of `values` will be set as the head of the LinkedList and rest of the arguments will be appended.

        Parameters: 
            - `*values` (any) : Any type and any number of arguments.

        Returns: 
            - None
        """

        for value in values:
            if not self.head:
                self.head = Node(value)

            else:
                temp: Node = self.head

                while temp.next:
                    temp = temp.next

                temp.next = Node(value)

    def display_elements(self) -> None | NoReturn:
        """
        This method prints the elements of the LinkedList in a user friendly way:
        `8 -> 7 -> hello -> None`

        If there are no values present in the LinkedList, a ValueError is raised.
        """

        if not self.head:
            raise ValueError("No values present in LinkedList.")

        temp: Node = self.head

        print("Elements of List:")
        while temp:
            print(f'{temp.data} -> ', end='')
            temp = temp.next

        print('None')

    def remove(self, value: any) -> None | NoReturn:
        """
        This method removes the provided value from the LinkedList.
        If value not present, a ValueError is raised.

        Parameters: 
            - `value` (any): Any value form the LinkedList.

        Returns: 
            - None
        """

        temp: Node = self.head
        previous = None
        present = False

        while temp:
            if temp.data == value:
                present = True
                if not previous:
                    self.head = temp.next

                else:
                    previous.next = temp.next

                del temp
                return None

            else:
                previous = temp
                temp = temp.next

        if not present:
            raise ValueError(f"'{value}' not present in LinkedList.")

    def to_pylist(self) -> list:
        """
        This method converts the LinkedList object to a python list object and returns it.
        If no values present in the LinkedList, a ValueError is raised.

        Parameters: 
            - None

        Returns: 
            - list: All the values of LinkedList in python list object.
        """

        if not self.head:
            raise ValueError("No values present in LinkedList.")

        temp: Node = self.head
        pylist = []

        while temp:
            pylist.append(temp.data)
            temp = temp.next

        return pylist

    def get(self, index: int) -> any:
        """
        This method returns the provided index element from LinkedList. If index not in range returns None.

        Parameters: 
            - `index` (int): Any integer value between 0 and len(LinkedList).

        Returns: 
            - any: Any object that is present at the index, if index out of range returns None.
        """

        temp: Node = self.head

        try:
            for _ in range(index):
                temp = temp.next

            return temp.data

        except:
            return None

    def __getitem__(self, index: int | slice) -> "LinkedList" | NoReturn:
        """
        This method returns a new LinkedList object according to the index or slice object provided.
        If index is not of type int or slice, TypeError is raised.
        If index not present, IndexError is raised.

        Parameters: 
            - `index` (int or slice): Indices to slice LinkedList.

        Returns: 
            - LinkedList: New LinkedList object according to the slice or index.
        """

        pylist = self.to_pylist()
        return_list = LinkedList()

        if isinstance(index, int):
            return_list.append(pylist[index])

        elif isinstance(index, slice):
            return_list.append(*pylist[index.start:index.stop:index.step])

        else:
            raise TypeError(f"Invalid index type `{index}`. It should be of type `int` or `slice`.")

        return return_list

    def __setitem__(self, index: int, value: any) -> None | NoReturn:
        """
        This method changes the node's `data` by `value` at the given index. 
        If index is not of type int, TypeError is raised.
        If index not present, IndexError is raised.

        Parameter: 
            - `index` (int): Any interger value between 0 and len(LinkedList).
            - `value` (any): Any value to set at that index.

        Returns: 
            - None
        """

        if isinstance(index, int):
            temp: Node = self.head

            for _ in range(index):
                temp = temp.next

            temp.data = value

        else:
            raise TypeError(f"Invalid index type `{index}`. It should be of type `int`.")

    def __len__(self) -> int:
        """
        This method returns the length or number of elements in the LinkedList.
        Note: None is not considered as a value of LinkedList so it won't contribute in length of LinkedList.
        """

        temp: Node = self.head
        length = 0

        while temp:
            length += 1
            temp = temp.next

        return length


if __name__ == '__main__':
    l1 = LinkedList()
    # l1.display_elements()
    print(len(l1))
    l1.append(7, 'Hello', [1, 2, 3])
    l1.append(8)
    l1.append([1, 2, 3])
    l1.display_elements()
    l1.remove(8)
    l1.remove('Hello')
    # l1.remove(7)
    l1.remove([1, 2, 3])
    l1.display_elements()
    print(len(l1))
    print(l1.head, l1.head.next)
    print(pylist := l1.to_pylist())
    l1.append(*pylist)
    l1.display_elements()
    print(l1.get(1))
    print(l1.get(8))
    l1[::-1].display_elements()
    # l1[8].display_elements()
    l1.display_elements()
    l1[0] = 'Hello'
    l1.display_elements()
    for i in l1:
        print(i.head)
    print(len(l1))
