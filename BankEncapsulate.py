#Encapsulation:
class Bank:
    def __init__(self,acc,name,amount,pin):
        self.acc=acc
        self.name=name
        self.__amount=amount    #private data
        self._pin=pin

    def __str__(self):
        return f'{self.acc},{self.name},{self.__amount},{self._pin}'


    #public fun
    def checkBalance(self):
        return self.__amount


    #private method
    def __deposite(self,money):
        if money>0:
            self.__amount+=money
            print('Money deposited successfully! ',self.__amount)
        else:
            print('Deposite Failed')


    #protected method
    def _withdraw(self,money):
        if self.__amount>0 and money<=self.__amount:
            self.__amount-=money
            print('Withdraw Successfully! ',self.__amount)
        else:
            print('Withdraw Failed')
            

obj=Bank('10123456','Vyshu',1000,2003)


#private method can be access with one _ and Class Name
obj._Bank__deposite(5000)

obj._withdraw(3000)




  abdulumer1205@gmail.com

