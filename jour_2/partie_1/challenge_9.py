text_1 = "je M'appell alI 9 10 11"
text_2 = "jE m'appell kAmal 2 9 2 10 "

list_1 =  text_1.lower().split()
list_2 =  text_2.lower().split()

list_1_clean = [x for x in list_1 if len(x) <= 3]
list_2_clean = [x for x in list_2 if len(x) <= 3]

print(list(set(list_1_clean) & set(list_2_clean)))