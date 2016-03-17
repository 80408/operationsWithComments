#for preprocessing json file

import re
import json

def getCommentsPos(text_with_comments, comments, comments_in_quotes):
    comments_in_quotes_pos_iter = comments_in_quotes.finditer(text_with_comments)
    comments_pos_iter           = comments.finditer(text_with_comments)
    
    comments_in_quotes_pos_list = [comments_in_quotes_pos for comments_in_quotes_pos in comments_in_quotes_pos_iter] 
    comments_pos_list = [comments_pos for comments_pos in comments_pos_iter]
    
    correct_comments_pos_list = []
    
    i = 0
    j = 0
    
    len_cpl   = len(comments_pos_list)
    len_ciqpl = len(comments_in_quotes_pos_list)
    
    while j < len_ciqpl:
        if comments_pos_list[i].start() < comments_in_quotes_pos_list[j].start():
            correct_comments_pos_list.append(comments_pos_list[i])
            i = i + 1
        elif comments_pos_list[i].start() > comments_in_quotes_pos_list[j].start():
            i = i + 1
            j = j + 1
            
    for k in range(i, len_cpl):
        correct_comments_pos_list.append(comments_pos_list[k])
    
    return correct_comments_pos_list
    
def deleteComments(text_with_comment, comments_pos):
    text_without_comment = text_with_comment
    
    for cp in reversed(comments_pos):
        text_without_comment = text_without_comment[0:cp.start()] + text_without_comment[cp.end():len(text_with_comment)]
    
    return text_without_comment
    
def preprocessing(slashes, slashes_in_quotes, slashes_with_stars, slashes_with_stars_in_quotes, text_with_comment):
    
    sc_pos = getCommentsPos(text_with_comment, slashes, slashes_in_quotes)
    text_without_sc = deleteComments(text_with_comment, sc_pos)
    
    lc_pos = getCommentsPos(text_without_sc, slashes_with_stars, slashes_with_stars_in_quotes)
    text_without_c = deleteComments(text_without_sc, lc_pos)
    
    return text_without_c
    

def main():
    slashes           = re.compile(r'//.*\n')     # // * \n
    slashes_in_quotes = re.compile(r'".*\/\/.*"') # "*//*" 
    
    slashes_with_stars           = re.compile(r'\/\*\s*.*\s*.*\s*\*\/') # /* * */
    slashes_with_stars_in_quotes = re.compile(r'"[^"]*\/\*.*\*\/"\n')   # "*/* * */"\n
        
    file_path = input()
    
    f = open(file_path, "r")
    text_with_comments = f.read()
    f.close()
    
    text_without_comments = preprocessing(slashes, slashes_in_quotes, slashes_with_stars, slashes_with_stars_in_quotes, text_with_comments)
    
    print text_without_comments
    
main()    