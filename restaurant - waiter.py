'''
requirements:
1. when a customer group arrives, assign a waiter for service
2. customer group orders meals, then waiter take the order to kitchen
3. when the meals are ready, kitchen call the corresponding waiter
4. waiter take the meals to the customer group
5. how the kitchen deal with orders (in turn)
6. check out the order whe customer group finish it

core objects:
Customer
- waiter: Waiter
- order: Order
Restaurant
- waiters: list<Waiter>
- menu: dict<str,int>
Waiter
- id: int
- customers: dict<Customer>
Kitchen
- orders: deque<Order>
Order
- meals: list<int>
- waiter: Waiter
- price: int
'''

from collections import deque
class Customer:
    def __init__(self):
        self.waiter = None
        self.order = None

    def assignWaiter(self,waiter):
        self.waiter = waiter

    def getWaiter(self):
        return self.waiter

class Restaurant:
    def __init__(self):
        self.waiterNum = 3
        self.waiters = [Waiter(i) for i in range(self.waiterNum)]
        self.menu = {'a':5,'b':8,'c':10,'d':6,'e':4}
        self.currentWaiter = 0
        self.kitchen = Kitchen()
        self.order = {}

    def assignWaiter(self, customer):
        waiter = self.waiters[self.currentWaiter%self.waiterNum]
        customer.assignWaiter(waiter)
        waiter.serveCustomer(customer)
        self.currentWaiter += 1

    def takeOrder(self, customer, meals):
        order = Order(customer, customer.getWaiter(), meals)
        self.kitchen.takeOrder(order)
        customer.order = order
        self.order[order] = 1
        return order

    def takeCall(self):
        order = self.kitchen.call()
        waiter = order.waiter
        waiter.takeCall(order)
        print('waiter {} take order call {} to customer'.format(waiter.getId(),order.id))

    def checkOut(self,order):
        self.order[order] = 0
        price = 0
        for i in range(len(order.meals)):
            price += self.menu[order.meals[i]]
        print('order {} has checked out with {} dollars'.format(order.id,price))
        return price


class Waiter:
    def __init__(self,id):
        self.id = id
        self.customers = {}

    def serveCustomer(self,customer):
        self.customers[customer] = 0
        print('waiter {} serves customer now.'.format(self.id))

    def getId(self):
        return self.id

    def takeCall(self,order):
        self.customers[order.customer] = 1


class Kitchen:
    def __init__(self):
        self.orders = deque()

    def takeOrder(self, order):
        self.orders.append(order)

    def call(self):
        order = self.orders.popleft()
        return order


class Order:
    id = 0
    def __init__(self,customer,waiter,meals):
        self.id = Order.id
        self.customer = customer
        self.meals = meals
        self.waiter = waiter
        Order.id += 1
        print('create order with waiter {} and meals {}'.format(self.waiter.id,self.meals))

    def getWaiterId(self):
        return self.waiter.getId()



ming = Customer()
hong = Customer()
restaurant = Restaurant()
restaurant.assignWaiter(ming)
restaurant.assignWaiter(hong)
order1 = restaurant.takeOrder(ming,['a','c'])
order2 = restaurant.takeOrder(hong,['b','d','e'])
restaurant.takeCall()
restaurant.checkOut(order1)
restaurant.takeCall()
restaurant.checkOut(order2)

