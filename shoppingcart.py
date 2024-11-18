def addgrocery(cart,item):
    cart.append(item)
    print ("{} in cart for purchase ".format(item))

def removegrocery(cart,item):
    cart.remove(item)
    print ("{} removed from cart for purchase ".format(item))

def showcart(cart):
    print("cart items include ")
    if len(cart)>):
        for item in cart:
            print ("{} ".format(item))
    else:
        print("nothing in cart ")


def cleargrocery(cart):
    cart.clear()
    print ("cart is now empty ")

def main():
    finished=False
    cart=[]
    while finished ==   False:
        ans=input("Would you like to keep shopping? Yes/No ")
        if ans == 'Yes' or ans =='yes':
            print("Thank you for shopping")
            showcart(cart)
            print("Goodbye")
            finished = True
        else:
            ans=input("Would you like to [A] add groceries, [B] remove groceries, [C] show grocery cart, [D] clear grocery cart")
            if ans == 'a' or ans == 'A':
                newgrocery = input("What would you like to add to cart")
                addgrocery(cart, newgrocery)
            elif ans == 'b' or ans == 'B':
                newgrocery = input("What would you like to remove from cart")
                removegrocery(cart, newgrocery)
            elif ans == 'c' or ans == 'C':
                showcart(cart)
            elif ans == 'd' or ans == 'D':
                cleargrocery(cart)
            else:
                print("please try again ")

main()

                

            

