import csv
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




def star_cashier():
    products = []
    total = 0


    while True:

        name = str(input("enter product name "))
        
        if name == "FIN":
            break
        
        price = float(input("enter the price of the product in euros  ")) 
        quantity = int(input("enter the quantity of the product "))
        discount = float(input("enter the product discount or 0 if you do not have "))
        
    
    
        subtotal = round(price*quantity*(1- discount),2)
        products.append(subtotal)
        
       
      
   
    for i, product in enumerate(products):
        print("the product", i + 1, "it has a price of:", product)
        total += product

        #print("El producto", i+1, "tiene un precio de:", product)
        
    #total = sum(products)
    print("the total is", total)


    
    file_name = 'cashier2.csv'

    
    with open(file_name, 'a', newline='') as file_csv:
        escritor_csv = csv.writer(file_csv)
        #escritor_csv.writerow(["subtotal"])
        for product in products:
            escritor_csv.writerow([product])

    print("Archivo CSV guardado correctamente.")

    
    


if __name__ == "__main__":
    clear_screen()
    star_cashier()