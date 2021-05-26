# def test(input):
#     ch_list = [] 
#     for i in input:
#         if i == "[" or  i == "]" or i == "{" or i == "}" or i == "(" or i == ")" :
#           ch_list.append(i)
        
#     if (ch_list.count("[") + ch_list.count("]")) % 2 == 0 and (ch_list.count("{") + ch_list.count("}")) % 2 == 0 and  (ch_list.count("(") + ch_list.count(")")) % 2 == 0:
#         return True
#     else:
#         return False

# test(f)
def multi_bracket_validation(input):
    """
    function take a string as arg and return a boolean representing whether or not the brackets in the string are balanced
    """
    # if len(input) % 2 != 0:
    #     return False
    # else:
    #     return True
    parentheses, curly, square_brackets = [], [], [] 
    for i in input:
        if i == "[":
            square_brackets.append(i)
        if i == "]":
            square_brackets.append(i)
        if i == "{":
            curly.append(i)
        if i == "}":
            curly.append(i)
        if i == "(":
            parentheses.append(i)
        if i == ")":
            parentheses.append(i)
    if len(parentheses) % 2 == 0 and len(square_brackets) % 2 == 0 and len(curly) % 2 == 0:
        return True
    else:
        return False
a = "()[[Extra Characters]]"
b = "{}(){}"
s = "{}{Code}[Fellows](())"
t = "[({}]"
f = "(]("

print(multi_bracket_validation(f))
