import textwrap

#Define a dummy text
texts = """This method wraps the input paragraph such that each line is at most width characters long in the paragraph. If the input has some content, it returns a list of lines as output."""



def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    word_list = wrapper.wrap(text = string)
   
    return "\n".join(word_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)