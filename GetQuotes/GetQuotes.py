import random

with open('all.txt', 'r') as all_quotes:
    quotesatfirst = []
    for x in all_quotes:
        quote = x.strip('\n')
        quotesatfirst.append(quote)

everything = [] + quotesatfirst

num = random.randint(0, len(everything)-1)
chosen_quote = everything[num] + '\n'

print(f'The number of lines is {len(everything) - 1}.')
print(f'That is approximately {(len(everything) - 1) / 20:.2f} months w/ 1 quote a day.')
print(f'That is approximately {(len(everything) - 1) / 40:.2f} months w/ 2 quotes a day.')
print(f'That is approximately {(len(everything) - 1) / 28:.2f} months w/ 2 quotes every tues/thurs.')
print(f'That is approximately {(len(everything) - 1) / 32:.2f} months w/ 2 quotes every mon/wed/fri.')



with open('used.txt', 'a+') as used:
    for i in range(0):
        used.seek(0)
        if chosen_quote not in used:
            print(chosen_quote + '\n')
            used.write(chosen_quote)
            num = random.randint(0, len(everything)-1)
            chosen_quote = everything[num] + '\n'
        elif chosen_quote in used:
            del everything[num]
            num = random.randint(0, len(everything)-1)
            chosen_quote = everything[num] + '\n'


