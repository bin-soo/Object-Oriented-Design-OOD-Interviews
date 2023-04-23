'''
requirements:
1. take waitlist order if restaurant is unavailable
2. cancel waitlist order of the customer
3. call in waiting customer when available

core methods:
Waitlist:
1. take order: given size, output ticket
2. cancel order: given ticket, output none
3. call in: output none
Ticket:
'''
from collections import deque

# class GroupList:
#     def __init__(self,identifier):
#         self.groupList = deque()
#         self.groupId = 0
#         self.identifier = identifier
#
#     def getIdentifier(self):
#         return self.identifier
#
#     def getId(self):
#         return self.groupId
#
#     def getList(self):
#         return self.groupList
#
#     def addOrder(self,order):
#         self.groupList.append(order)
#         self.groupId += 1
#
#     def checkOrder(self,id):
#         for item in self.groupList:
#             if item.getId() == id:
#                 return item
#
#     def cancelOrder(self,id):
#         for item in self.groupList:
#             if item.getId() == id:
#                 self.groupList.remove(item)
#                 return
#
# class WaitList:
#     def __init__(self):
#         self.GroupLists = [GroupList('S'),GroupList('L')]
#
#     def takeOrder(self, size):
#         order = Ticket(size)
#         group = 0 if size <= 4 else 1
#         order.setId(self.GroupLists[group].getIdentifier() + str(self.GroupLists[group].getId()))
#         self.GroupLists[group].addOrder(order)
#         print('new order: {}'.format(order.getId()))
#         return order
#
#     def cancelOrder(self,id):
#         for g in range(len(self.GroupLists)):
#             if self.GroupLists[g].getIdentifier() == id[0]:
#                 self.GroupLists[g].cancelOrder(id)
#                 return
#
#
#     def call(self, type):
#         order = None
#         if type == 'small':
#             order = self.GroupLists[0].getList().popleft()
#         elif type == 'large':
#             order = self.GroupLists[1].getList().popleft()
#         order.display()
#         return order

class WaitList:
    def __init__(self):
        self.smallGroupList = deque()
        self.largeGroupList = deque()
        self.smallId = 0
        self.largeId = 0

    def takeOrder(self, size):
        order = Ticket(size)
        if size <= 4:
            order.setId('S'+str(self.smallId))
            self.smallGroupList.append(order)
            self.smallId += 1
        else:
            order.setId('L' + str(self.largeId))
            self.largeGroupList.append(order)
            self.largeId += 1
        print('new order: {}'.format(order.id))
        return order

    def cancelOrder(self,id):
        if id[0] == 'S':
            for item in self.smallGroupList:
                if item.getId() == id:
                    self.smallGroupList.remove(item)
                    break
        elif id[0] == 'L':
            for item in self.largeGroupList:
                if item.getId() == id:
                    self.largeGroupList.remove(item)
                    break

    def call(self, type):
        order = None
        if type == 'small':
            order = self.smallGroupList.popleft()
        elif type == 'large':
            order = self.largeGroupList.popleft()
        order.display()
        return order



class Ticket:
    def __init__(self,size):
        self.size = size
        self.id = None

    def setId(self,id):
        self.id = id

    def getSize(self):
        return self.size

    def getId(self):
        return self.id

    def display(self):
        print('current order is {} with size {}'.format(self.id,self.size))

waitlist = WaitList()
waitlist.takeOrder(1)
waitlist.takeOrder(4)
waitlist.takeOrder(3)
waitlist.takeOrder(5)
waitlist.takeOrder(6)
waitlist.takeOrder(2)
waitlist.call('small')
waitlist.call('large')
waitlist.cancelOrder('S1')
waitlist.cancelOrder('S2')
waitlist.call('small')
waitlist.call('large')

