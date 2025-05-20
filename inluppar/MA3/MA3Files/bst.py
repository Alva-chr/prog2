""" bst.py

Student: Alva Christensson
Mail: Alvachristensson03@gmail.com
Reviewed by: Yashaswi Sood
Date reviewed: 2025-05-19
"""


from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k): #
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    #Recursive method to find given number k
    def contains_recursive(self, k):

        def _contain_recursive(r, k):
            if r is None:
                return False #Base case
            
            #The 3 cases we can have
            if r.key == k:
                return True
            
            elif r.key < k:
                return _contain_recursive(r.left, k)

            elif r.key > k:
                return _contain_recursive(r.right, k)

        return _contain_recursive(self.root, k)

    def height(self):

        def _height(r):
            if r is None:
                return 0 #basecase
            
            #Recursive
            L_subTree = _height(r.left)
            R_subTree = _height(r.right)

            return 1 + max(L_subTree,R_subTree)
        
        return _height(self.root)

    def remove(self, key): #
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      #
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
        elif k > r.key:
            r.right = self._remove(r.right, k)
        
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                mini = self._min(r.right)
                r.key = mini.key
                r.right = self._remove(r.right, mini.key)
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above
    
    def _min(self, node):
        current = node
        while current.left is not None:
            current = current.left

        return current
    
    def __str__(self):   
        s = "<"          
        for x in self:
            s += str(x) + ", "

        if len(s) > 2:
            s = s[0:-2]
        return s + ">"

    def to_list(self): # Complexity: O(n)     
        return [x for x in self]

    def to_LinkedList(self):                 #     
        lst = LinkedList()

        for x in self:
            lst.insert(x)

        return lst


def random_tree(n):                               # Useful
    pass


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")

    print(t.height())
    print(t)
    print(t.to_list())


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? Yes
2. computing height? No
3. contains? Yes
4. insert? No
5. remove? Yes

"""

