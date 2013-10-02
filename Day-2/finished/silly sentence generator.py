import random

verb_list = ["ran","jumped","climbed","licked","programmed"] #create a list of all your verbs
noun_list = ["pet duck","tree","toaster","computer"]
adjective_list = ["tasty","large","smelly","green"]

#this function is given a list of words and selects one at random
def random_word(list_of_words):
    number_of_words = len(list_of_words) #get the length of the words list
    random_word_number = random.randint(0,number_of_words - 1) #pick a random number up to the end of the list
    selected_word = list_of_words[random_word_number] #select the word at the number spot
    return selected_word #hand it back

def random_word2(list_of_words):
    return random.choice(list_of_words)

#a simple sentence structure:
#The <adjective> <noun> <verb> the <adjective> <noun>.

for i in range(10):
    adjective1 = random_word2(adjective_list)
    adjective2 = random_word2(adjective_list)
    noun1 = random_word2(noun_list)
    noun2 = random_word2(noun_list)
    verb = random_word2(verb_list) #call the function and remember the result
    print "The",adjective1,noun1,verb,"the",adjective2,noun2
