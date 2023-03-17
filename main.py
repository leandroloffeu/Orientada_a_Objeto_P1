
from conta import*
from cliente import*

if __name__ == '__main__': 
    cliente1 = Cliente('fabricio','Dias', 15625674890)   
    conta1 = Conta('123-5', cliente1, 120.00)
    conta2 = Conta('234-5', 'Gabriel Neves',200.00,500.00)
    conta3 = conta2

print(type(conta1.numero))
print(type(conta1.titular))
print(type(conta1.limite))
   
