# Linked List
My implementation of linked list. I had also implemented indexing and slicing in it.

## Attributes: 
- `head` (Node or None): head of the LinkedList, default None.
    
## Functions: Look over to the respective functions for detailed information about them.
- `append`: It is used to append an element to the LinkedList.
- `display_element`: Displays the elements of the LinkedList.
- `remove`: Removes an existing element from the LinkedList.
- `to_pylist`: Converts the LinkedList to python's list object and return it.
- `get`: Returns the element whose index is provided, if index out of range returns None.
- `__getitem__`: Implements indexing and slicing to the LinkedList.
- `__setitem__`: Implements item assignment to LinkedList.
- `__len__`: Returns the length of LinkedList.

## Usage: Create an object of LinkedList class.
```
l1 = LinkedList()
```

## Example: 
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

## Note: 
- Errors might be raised when wrong input is provided. Handle them if necessary.
- data of Node class can be any object, even another LinkedList object.
- None is considered as end of LinkedList, so don't add None in it (this will cause loss of data).
