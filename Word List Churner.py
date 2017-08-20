"Create Word List to be used with Aircrack-Ng for WEP Cracking."

base_string = str(raw_input('Enter Base String:'))

word_list = []

for number in range(0,1000):
    number_string = str(number)

    number_length = len(number_string)

    shortfall = 3- number_length

    word = base_string + '0'*shortfall + number_string

    word_list.append(word)


word_list_file = open(base_string+'.lst', 'w')

for word in word_list:
    word_list_file.write(word)
    word_list_file.write('\n')

word_list_file.close()
