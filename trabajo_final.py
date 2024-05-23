import os

dicc_register = {}
price_total = 0 
counter = 0
list_sales = []

def fnt_clean():
    os.system('cls')
    print(f'📕📗📘📕📗📚SEXISS PAPELERY📚📘📙📗📕📙\n\nby: Jose Daniel Nuñez Arenas\n📙📗📕📘📙following the next instructions carefully📙📘📕📗📙{dicc_register}\n\n')

def fnt_register(code, tepe, name, amount, price):
    global dicc_register
    while True:
        fnt_clean()
        type_R = input('📚REGISTER PRODUCTS📚\n\n[1]register\n[2]back to the interface\n ➡️ ')
        if type_R == '1':
            if code in dicc_register:
                input('This product has already been registered 📙📙ENTER📙📙 ')
            else:
                dicc_register[code] = {'type': tepe, 'name': name, 'amount': amount, 'price': price}
                input('Product registered successfully 📙📙📙')
        elif type_R == '2':
            break

def fnt_make_sale():
    global price_total, counter
    while True:
        fnt_clean()
        type_S = input('📚MAKING SALES📚\n\n[1]sales \n[2]back to the interface\n ➡️ ')
        if type_S == '1':
            codex = input('Write the code for the sale\n ➡️')
            if codex in dicc_register:
                amount_sale = int(input('How much do you want to buy?\n ➡️'))
                if dicc_register[codex]['amount'] - amount_sale < 0:
                    input('You cannot buy this quantity because we do not have this quantity')
                else:
                    dicc_register[codex]['amount'] -= amount_sale
                    input('Product sold successfully 📙📙📙')
                    total_price = dicc_register[codex]['price'] * amount_sale
                    price_total += total_price
                    counter += 1
                    list_sales.append({'code': codex, 'amount_sold': amount_sale, 'total_price': total_price})
                    input('Total price: $' + str(total_price))
        elif type_S == '2':
            break

def fnt_show_register():
    while True:
        fnt_clean()
        type_SR = input('📚SHOWING REGISTERED PRODUCTS📚\n\n[1]show\n[2]back to the interface\n ➡️ ')
        if type_SR == '1':
            print(dicc_register)
            input('Shown successfully📙📙📙press enter to go back📙📙📙')
        elif type_SR == '2':
            break

def fnt_show_sold():
    global counter, list_sales
    while True:
        fnt_clean()
        type_SS = input('📚SHOWING SOLD PRODUCTS📚\n\n[1]show\n[2]back to the interface\n ➡️ ')
        if type_SS == '1':
            for sale in list_sales:
                print(f'Code: {sale["code"]}, Amount Sold: {sale["amount_sold"]}, Total Price: ${sale["total_price"]:.2f}')
            print(f'Total sales amount: {counter}')
            print(f'Total sales price: ${price_total:.2f}')
            input('Shown successfully📙📙📙press enter to go back📙📙📙')
        elif type_SS == '2':
            break

def fnt_selector(x):
    global sw
    if x == '1':
        code = input('Write the product code➡️ ')
        tipe = input('Write the product type➡️ ')
        name = input('Write the product name➡️ ')
        amount = input('Write the product amount➡️ ')
        price = input('Write the product price➡️ ')
        fnt_register(code, tipe, name, amount, price)
    elif x == '2':
        fnt_make_sale()
    elif x == '3':
        fnt_show_register()
    elif x == '4':
        fnt_show_sold()
    elif x == '5':
        sw = False

sw = True
while sw:
    fnt_clean()
    op = input('😈😈😈Welcome to SEXISS PAPELERY Interface😈😈😈\nWhat would you like:\n[1] Register Products\n[2] Making Sales\n[3] Showing the Registered Products\n[4] Showing Sold Products\n[5] 📚EXIT📚 \n➡️ ')
    fnt_selector(op)