# mortgage.py
#
# Exercise 1.7
mortgage_amount = 500000
current_month = 0
extra_start = 60
extra_end = 108
extra_payment = 1000
rate = 0.05
emi = 2684.11
principal_amount_paid = 0
total_paid = 0

while mortgage_amount > 0:
    current_month += 1
    if current_month > extra_start and current_month <= extra_end:
        emi_plus = emi + extra_payment
    else:
        emi_plus = emi
    
    interest_portion = mortgage_amount * rate * (1/12)
    principal = emi_plus - interest_portion
    
    if mortgage_amount < emi_plus:
        mortgage_amount = 0
        principal = mortgage_amount - interest_portion
        emi_plus = principal + interest_portion
    else:
        mortgage_amount -= principal

    # mortgage_amount -= principal
    principal_amount_paid += principal
    total_paid += emi_plus

    # print(i+1, ': Interest: ', interest_portion, '| Principal: ', principal)
    print(current_month, round(total_paid, 2), round(mortgage_amount, 2))

print('Principal amount paid: ', principal_amount_paid)
print('Total amount paid: ', total_paid, ' in', current_month, 'months')
