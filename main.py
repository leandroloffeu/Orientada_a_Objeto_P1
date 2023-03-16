
from conta import*

if __name__ == '__main__':  
    conta1 = Conta('123-5', 'Nilton Junior', 120.00)
    conta2 = Conta('234-5', 'Gabriel Neves',200.00,500.00)
    conta3 = conta2

conta1.transfere(conta2, 121)
print(conta2.saldo)
print(conta1.saldo)

print(conta1.limite)



   
