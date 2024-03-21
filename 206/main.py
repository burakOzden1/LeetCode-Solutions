class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Dairesel bağlantılı liste oluşturma
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node1

















# class Solution(object):
#     def reverseList(self, head):
#         pass


# head = [1,2,3,4,5]
# # head = [1,2]
# # head = []

# solution = Solution()
# print(solution.reverseList(head))