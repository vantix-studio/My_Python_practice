price = 55000
if price > 50000:
    final_price = int(price - (price*0.2))
    print(f"you have to pay {final_price}")
elif  price >= 20000 and price <= 50000 :
    final_price =int (price - (price*0.1))
    print(f"you have to pay {final_price}")
else :
    print("no off")    