# Lesson 5

# input 
start_money = float(input())
cookies_sold = input()

#processing
#big_cookies = 0 
#cookies_sold = 0
big_cookies = cookies_sold.count('b')
cookies = cookies_sold.count('c')

#for current_coookie in cookies_sold:
#    if current_cookie == "c":
#        cookies +=1
#    elif current_cookie == "b":
#        big_cookies += 1
#    else:
#        print(f"{current_cookie} is not a valid sale item.")
# end of for

total_cookies = big_cookies + cookies
profit = (big_cookies * 1.25) + (cookies * 0.75)
end_day = start_money + profit

#output

print(f"We sold {total_cookies} cookies, we made ${profit}. We now have ${end_day}.")

