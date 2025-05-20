""" linked_list.py

Student: Alva Christensson
Mail: Alvachristensson03@gmail.com
Reviewed by: Yashaswi Sood
Date reviewed: 2025-05-19
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False
    
    def __getitem__(self, index):
        i = 0
        for x in self:
            if i == index:
                return x
            i += 1
        raise IndexError(f'LinkedList index {index} out of range')

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):  
        len = 0  
        f = self.first

        while f:
            len += 1
            f = f.succ
        return len


    def mean(self):               
        pass

    def remove_last(self): 
        f = self.first

        if self.first is None:
            raise ValueError ("Empty Linked list")
        
        elif f.succ is None:
            removedData = f.data
            self.first = None
            return removedData
        
        else:
            while f.succ.succ is not None:
                f = f.succ
            removedData = f.succ.data
            f.succ = None
            return removedData
        
    #Gör om linked list till en vanlig lista      
    def to_list(self):
        l = []
        #help-function
        def _to_list(node):
            if node is None:  # base case, when we reach the end of the linkedlist
                return None  # Nothing needs to be done
            
            else:
                l.append(node.data) #Adding the nodes data to the ordinary list
                _to_list(node.succ)  # recursive

        _to_list(self.first)
        return l
        
    def remove(self, x):  
        f = self.first  

        if f is None:
            return False
        
        if f.data == x:
            self.first = f.succ
            return True
            

        while f.succ is not None:
            if f.succ.data == x:
                f.succ = f.succ.succ 
                return True
            f = f.succ

        return False


    def remove_all(self, x):  
        def _remove_all(node):
            if node is None:  # Base case
                return None, 0  # Return nothin and a Node is not removed
            if node.data == x:  # if we find what is supposed to be removed
                new_node, count = _remove_all(node.succ)  # Skip the node and go to the next
                return new_node, count + 1  #
            else:
                new_node, count = _remove_all(node.succ)  # Behåll noden och fortsätt rekursionen
                node.succ = new_node  # Uppdatera pekaren till nästa nod
                return node, count  # Återvänd till föregående anrop
        
        self.first, removed_count = _remove_all(self.first)  # Starta rekursionen från första noden
        return removed_count  # Returnera hur många som tagits bort

    def __str__(self):  
        lst = '('

        for x in self:
            lst += str(x) + ', '

        if len(lst) > 2:
            lst = lst[0:-2]
        
        lst = lst + ')'
        return lst

    def copy(self):               #
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 
        O(n^2), 
        O(n) for forloppen in copy x O(n) for the worst case in insert (if the node needs the be addes in the last place)
    '''

    def copy(self):   
        result = LinkedList()

        if self.first is None:
            return result
        
        else:
            result.first = result.Node(self.first.data, None) # Sets first new node
            Old_node = self.first.succ #starting point for iteration
            New_node = result.first # startin point for iteration

            #goes through the old list and adds a new node to the new list

            while Old_node != None:
                    New_node.succ = result.Node(Old_node.data,None)

                    #Next node
                    Old_node = Old_node.succ
                    New_node = New_node.succ

            return result
    ''' Complexity for this implementation:
        O(n), goes through all the elements one time. We dont really need insert because we already know
        that the linkedlist is sorted from when it was created.
    '''

def main():

    #creating and printing Linkedlists thats going to be tested
    FullLst = LinkedList()

    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        FullLst.insert(x)
    FullLst.print()

    EmptyLst = LinkedList()
    EmptyLst.print()

    OneLst = LinkedList()
    OneLst.insert(7)
    OneLst.print()

    # Test code:
    # print(f'copy method test: {FullLst.copy()}')
    # print(f"Test lenght, should be 10: {FullLst.length()}")
    # print(f"Test remove last, should be 9: {FullLst.remove_last()}")
    # print(f"Test remove last, should raise evualationError: {EmptyLst.remove_last()}")
    # print(f"Test remove last, should be 7: {OneLst.remove_last()}")
    # print(f"Test Remove 7,should return True: {FullLst.remove(7)}")
    # print(f"Test Remove 8 ,should return False: {FullLst.remove(8)}")
    # print(f"Test Remove 1,should return True: {FullLst.remove(1)}")

if __name__ == '__main__':
    main()
