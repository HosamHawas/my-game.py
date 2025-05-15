import os
import time 


def clear_screen():
    os.system ("cls" if os.name == "nt" else "clear")
def currency_rates():
    print("""  welcome to  'currency converter':
            ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
          
_____________________________________________________________________________

          USD : 1.0
          EUR : 0.85
          EGP : 30.9
          RMB : 6.5 """)
    

def Currency_conversion():
   
    Currency_rate = {"usd":1.0, "eur":0.85, "egp":30.9, "rmb":6.5,}
    user_currency = input("choose a currency convert from: ").lower()
    amount_with_user = float(input("Enter the amount: "))

    while True:
        if input(f"you entred {amount_with_user} {user_currency}. confirm(y/n): ") == "n":
            amount_with_user = float(input("Enter the amount: "))
        else:
            clear_screen()
            currency_convert_to= input("choose a currency convert to: ").lower()
            exchange_rate =Currency_rate[currency_convert_to]/Currency_rate[user_currency] 
            total_fter_conversion =  amount_with_user / exchange_rate
            output_in_doller =  amount_with_user / Currency_rate[user_currency] 
            
            time.sleep(2)
            print("\nAnalyzing your request....please wait.")
            time.sleep(2)
            print(f"\nchecking best {currency_convert_to}s best rates avalible.....please wait.")
            time.sleep(2)
            print(f"\ngetting a discount price for {user_currency}.....please wait.")
            time.sleep(2)
            clear_screen()
            print(f"\nperpraing the deal from {user_currency} to {currency_convert_to}......please wait.")
            time.sleep(3)
            print(f"\nExchange rate 1 {user_currency} = {exchange_rate} {currency_convert_to}")
            print(f"\n{amount_with_user} {user_currency} is equal to {output_in_doller} {currency_convert_to}")
            
currency_rates()

Currency_conversion()

# while True:
#     clear_screen()
#     currency_rates()
    
    