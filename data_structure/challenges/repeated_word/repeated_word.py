import re
from collections import Counter , OrderedDict
# from data_structure.challenges.repeated_word.hashtable2  import Hashtable
from data_structure.data_structure.hashtable.hashtable  import Hashtable


  
def repeated_word(string): 
    reg = re.findall('[\w\']+',string.lower()) 
    ## or counts = dict()
    ## words = str.split()
    # findall:If one or more groups are present in the pattern, return a  list of tuples 

    ## using Counter

    # counted = Counter(reg) 
    # for key in reg:
    #   if counted[key]>1: 
    #     print (key) 
    #     return key
    words = []
    repeated = ""

    for i in reg: 
        if i in words: 
            print(i)

            repeated = i
            break
        words.append(i) 
    # print(words)
    # print(repeated)
    return repeated


string = "Once upon a time, there was a brave princess who..."
string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
# repeated_word(string3)

## with linked list 
# def repeated_words(string):
#     '''
#     using linked list this function will search for the first repeated word in your inputed string:
#         inp ---> only string
#         out >>> the repeated word from your input
#     '''
#     container = LinkedList()
#     word = ''
#     for i in range(len(string)):
#         if container.includes(word):
#             # print(container.toString())
#             print(word)
#             return word 
#         elif string[i] == ',' or string[i] == ' ' or string[i] == '-' or string[i] == '.' :
#             if word != '': 
#                 container.insert(word)
#                 word = ''
#             continue
#         else:
#             word += string[i].lower()
#     # print(container.toString())
#     return 'no repeated word in your input!'

# repeated_words(string3)

def repeat_word(paragraph: str) -> str:
    # create new hastable
    hashtable = Hashtable()

    # split paragraph into an array of words
    words_list = paragraph.split()

    # loop through words
    for i in range(len(words_list)):
        # check to see if it already exists in hashtable
        if hashtable.contains(i):
            # hash the key
            ht_index = hashtable._hash(i)
            # check to see if value is the same
            ht_node = hashtable._buckets[ht_index]

            if ht_node:
                # print(words_list[i])
                return words_list[i]
            # if value is the same return

        hashtable.set(i, words_list[i])
# repeat_word(string)


import re
class HashMap:
  def __init__(self, size=10000):
    self.size = size
    self.buckets = [None]*size
  def hash(self,key):
    '''
    this function takes a string value and return hashed key
    '''
    sum = 0
    for letter in key:
       sum= sum + ord(letter)* key.index(letter)
    return  sum
  def add(self,key):
    '''
    this function take a string key and a value then add them in the hashtable as a list
    '''
    index = self.hash(key)
    if self.buckets[index] is None:
      self.buckets[index] = key
      return None
    return key
  def collision(self , string):
    string = re.sub(r'[^\w\s]', '', string)
    strings = string.split(' ')
    for word in strings:
      if self.add(word):
        return word
hashm = HashMap()
print(hashm.hash('Ahmad'))
hashm.collision("hello world everyone, hello")
print(hashm.collision(string))