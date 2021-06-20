import re
from collections import Counter , OrderedDict

  
def repeated_word(string): 
    reg = re.findall('[\w\']+',string.lower()) # findall:If one or more groups are present in the pattern, return a  list of tuples 
    counted = Counter(reg) 
    # for i in reg:
    #     counted = OrderedDict.popitem(i)
    #     print(counted)
    # repeated = {}
    # for i in reg:
    #     if counted[i]>1:
    #         repeated[counted[i]].keys = counted[i]
    # print(repeated)

    for key in reg:
      if counted[key]>1: 
        print (key) 
        return key
        

string = "Once upon a time, there was a brave princess who..."
string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
repeated_word(string2)