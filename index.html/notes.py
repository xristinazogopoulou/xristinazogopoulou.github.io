def delete_HTML(text):
    '''
    This function removes all HTML tags from the input text.

    >>> delete_HTML('This is <b>bold</b>!')
    'This is bold!'
    >>> delete_HTML('This is <i>italic</i>!')
    'This is italic!'
    >>> delete_HTML('This is <strong>italic</strong> and this is <ins>strikethrough</ins>!')
    'This is italic and this is strikethrough!'
    
'''
    '''
#this works for the test cases but its not very general
#not the best solution
    
    text = text.replace ('<b>', '')
    text=text.replace('</b', '')
    text=text.replace('<i>', '')
    text=text.replace('</i>', '')
    return text 
    '''

    accumulator=''
    for c in text:
        #if we are inside of an HTML tag:
        accumulator+=c
        #do something with c
    return accumulator 



