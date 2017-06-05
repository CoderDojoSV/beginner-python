## Silly Sentence Generator

Our next project is a silly sentence generator that will randomly pick words from lists to generate a funny sentence.

Open the starter file: [silly sentence generator.py](silly%20sentence%20generator.py). Copy all the code into a new Python window.

### Let's look at the code:

#### Lists

Up until now, we've stored things in one variable at a time.  A list is a way to collect multiple values in one variable.  Let's make a list:

```python
>>> grocery_list = ["apples","bananas","a pet chicken"]
```

We can look at specific items in the list with an *index*, and indexes start from zero.

```python
>>> print grocery_list[0]
apples
```

#### Random

We can use the random module to create random numbers:

```python
import random
random.randint(0,5)
```

A module is something extra in Python that lets you go beyond what Python lets you do by default.

#### The `random_word` Function
The `random_word` function picks a random index from 0 to the last item in the list.  Then, it finds the word with that index, and hands it back:

```python
#this function is given a list of words and selects one at random
def random_word(list_of_words):
    number_of_words = len(list_of_words) #get the length of the words list
    random_word_number = random.randint(0,number_of_words - 1) #pick a random number up to the end of the list
    selected_word = list_of_words[random_word_number] #select the word at the number spot
    return selected_word #hand it back
```

*Functions* in Python let you take a piece of code and use it over and over again.

##### Functions
We can use the `def` keyword to define a function.  Functions let you send something to the function, and the function sends you something back.  You can re-use functions by sending them different data, and they'll send you different data back.

In the statement `random_word(verb_list)`, `verb_list` is what we're sending to the function.  The function doesn't care that it's the verb list, so we can give it any list of words.

### Add our own code!

#### Create your own noun and adjective lists

Look at how the verb list was done.  We can make our own lists of adjectives and nouns, and maybe add some more verbs for variety.

#### Use the function to select random words from each list

You will need 5 variables: `adjective1`, `noun1`, `verb`, `adjective2`, and `noun2`.  Remember, we can re-use functions by passing them different information, and they'll send different information back.

#### Print the result in a sentence.

Be sure to insert the word "the" in the right places.  What sentences can you make?

#### `random.choice`
We just wrote a function to pick a random word from a list of words.  However, the `random` module already gives us a way to do this.  We can use `random.choice` to write a new version of `random_word`:

```python
def random_word2(list_of_words):
    return random.choice(list_of_words)
```

We've just shortened a 4-line function to a 1-line function.  When you have a 1-line function, you have to think, "Do I really need that function?"  In this case, it's kind of OK, because we arrived at that 1-line function by a process of iteration.

#### Making more silly sentences
Can you change the program to print 10 silly sentences instead of 1?  Look back at [the notes from last week](../day-1) if you need to remember how loops work.

#### Possible extensions

* Improve your word list.  If you like Minecraft, for example, add some Minecraft terms!
* Improve the sentences' grammar
* Make the sentences longer, with more word types
* Just see how creative you can get with your sentences!


