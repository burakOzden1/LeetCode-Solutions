class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Tek Yönlü Bağlantılı Liste (Singly Linked List):
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(node1.data)
print(node1.next.data)
print(node1.next.next.data)
print(node1.next.next.next.data)


print(node1.next.data)
print(node2.next.data)
print(node3.next.data)
print(node4.next.data)
print(node5.next.data)

# Çift Yönlü Bağlantılı Liste (Doubly Linked List):

node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node13 = Node(13)
node14 = Node(14)
node15 = Node(15)

node10.next = node11
node11.prev = node10

node11.next = node12
node12.prev = node11

node12.next = node13
node13.prev = node12

node13.next = node14
node14.prev = node13

node14.next = node15
node15.prev = node14


# Dairesel Bağlantılı Liste (Circular Linked List):

node20 = Node(20)
node21 = Node(21)
node22 = Node(22)
node23 = Node(23)
node24 = Node(24)

node20.next = node21
node21.next = node22
node22.next = node23
node23.next = node24
node24.next = node20

print(node20.next.data)


################################ Cozum ##############################

class Solution(object):
    def reverseList(self, head):
        def rec(prev, curr):
            if not curr:
                return prev
            tail = rec(curr, curr.next)
            curr.next = prev
            return tail
        return rec(None, head)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Bağlantılı listeyi tersine çevirme
solution = Solution()
new_head = solution.reverseList(node1)

# Tersine çevrilen bağlantılı listeyi yazdırma
current = new_head
while current:
    print(current.data, end=' ')
    current = current.next

    
################################ Cozum ##############################