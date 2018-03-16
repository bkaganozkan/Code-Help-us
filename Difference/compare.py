
text_dict = {}
text_2_dict = {}

def readFiles(f_file_path, s_file_path):
    with open(f_file_path, mode='r', encoding="utf-8") as read_file:
        f_text = read_file.readlines()
    with open(s_file_path, mode='r',encoding="utf-8") as read_file:
        s_text = read_file.readlines()
    return f_text,s_text

def clearText(f_text, s_text):
    # First Text
    for text in list(f_text):
        if text is '\n':
            f_text.pop(f_text.index(text))
        else:pass
    # Second Text
    for text in list(s_text):
        if text is '\n':
            s_text.pop(s_text.index(text))
        else:pass
    return f_text, s_text


def compareFiles(f_text, s_text):
    global text_dict, text_2_dict
    f,s = clearText(f_text, s_text)
    compare_results = []
    for index,text in enumerate(f):
        text_dict[index] = text

    for index,text in enumerate(s):
        text_2_dict[index] = text

    for ind in range(0,len(text_dict)):
        try:
            for index, latter in enumerate(text_dict[ind]):
                if text_dict[ind][index] is text_2_dict[ind][index]:
                    pass
                else:
                    compare_results.append([ind,index])
        except: print("{}.Row totally different. Difference starts {}. latter".format(ind,index-1))
    return compare_results

def showResults(compare_result):
    global text_dict,text_2_dict
    for ind in compare_result:
        print("{}{}".format(text_dict[ind[0]],text_2_dict[ind[0]]))
        try:
            print("{}. Row difference : {} ".format(ind[0],text_dict[ind[0]][ind[1]]), end="")
            print("---",text_2_dict[ind[0]][ind[1]])
        except:pass

f_text, s_text= readFiles("test1.txt", "test2.txt")
result = compareFiles(f_text,s_text)
showResults(result)

