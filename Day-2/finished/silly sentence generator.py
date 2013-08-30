import random

verb_list = ["runs","jumps","climbs"] #create a list of all your verbs
noun_list = ["cat", "dog","sheep","lamp","mother","father"]
adjective_list = ["smart","shy","tall","short","happy"]

#this function is given a list of words and selects one at random
def random_word(list_of_words):
    number_of_words = len(list_of_words) #get the length of the words list
    random_word_number = random.randint(0,number_of_words - 1) #pick a random number up to the end of the list
    selected_word = list_of_words[random_word_number] #select the word at the number spot
    return selected_word #hand it back

#a simple sentence structure:
#The <adjective> <noun> <verb> the <adjective> <noun>.

adjective1 = random_word(adjective_list)
noun1 = random_word(noun_list)
verb = random_word(verb_list) #call the function and remember the result
adjective2 = random_word(adjective_list)
noun2 = random_word(noun_list)

print "The", adjective1, noun1, verb, "the", adjective2, noun2
