import random

verb_list = ["run","jump","climb"] #create a list of all your verbs

#this function is given a list of words and selects one at random
def random_word(list_of_words):
    number_of_words = len(list_of_words) #get the length of the words list
    random_word_number = random.randint(0,number_of_words - 1) #pick a random number up to the end of the list
    selected_word = list_of_words[random_word_number] #select the word at the number spot
    return selected_word #hand it back

#a simple sentence structure:
#The <adjective> <noun> <verb> the <adjective> <noun>.

verb = random_word(verb_list) #call the function and remember the result
print verb
