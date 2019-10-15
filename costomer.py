class Customer:
    def __init__(self,name,total=0.0):
        self._name = name
        self._total = total
    def pay(self,price):
        self._total += price
        return self._total
    def total(self):
        return self._total
class VIP(Customer):
    _discount = 0.98
    def pay(self,price):
        paid = round(price*VIP._discount,2)
        self._total += paid
        return self._total
class CustomerManager:
    __name_to_customer = {}
    __VIP_price = 1000.0
    @classmethod
    def VIP(cls,name):
        if (name in cls.__name_to_customer and isinstance(cls.__name_to_customer[name],VIP)):
            return True
        else:
            False
    @classmethod
    def pay_price(cls,name,price):
        if name not in cls.__name_to_customer:
            cls.__name_to_customer[name] = Customer(name)
        customer = cls.__name_to_customer[name]
        paid = customer.pay(price)
        total = customer.total()
        if(not isinstance(customer,VIP) and total>=cls.__VIP_price):
            cls.__name_to_customer[name] = VIP(name,total)
        return paid,total

print('张三，第一次',(CustomerManager.pay_price('张三',100)))
print('张三，第二次',(CustomerManager.pay_price('张三',100)))
print('张三，第三次',(CustomerManager.pay_price('张三',900)))
print('张三，第四次',(CustomerManager.pay_price('张三',900)))
