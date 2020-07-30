#Import library to change number from integer to string
import inflect
p = inflect.engine()

#create arrays for matches
match_asc_order = []
match_desc_order = []

for i in range(100):
    #convert number to words
    word = p.number_to_words(i)
    
    #sort string alphabetically - ascending
    w = sorted(word)
    w_sorted_asc = ''.join(w)
    #check if number match original form
    asc_check_match = w_sorted_asc == word
    if asc_check_match:
        match_asc_order.append(word)
    
    #sort string alphabetically - descending
    reversed_w = word[::-1]
    w_sorted_desc = w_sorted_asc[::-1]
    #check if number match original form
    desc_check_match = w_sorted_desc == word
    if desc_check_match:
        match_desc_order.append(word)
    
#Print results
print("Numbers with letter sorted in ascending alphabetical order:")
print(match_asc_order)
print("Numbers with letter sorted in descending alphabetical order:")
print(match_desc_order)
