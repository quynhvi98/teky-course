input('Moi cac ban nhap mot so nguyen bat ki:')
a=input
odd=1
while a>0:
     if a%2==0:
       print(odd)
       odd+=2
     elif a%2==1:
         print(odd)
         odd+=2
     if odd>a:
       break