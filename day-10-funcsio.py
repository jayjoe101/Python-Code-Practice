def format_name(f_name, l_name): 
    """ Takes two strings, first and last, then adds an uppercase letter
    to the beginning of the strings""" # adds a description to the function
    
    return f'{f_name.title()} {l_name.title()}' # title upercases first letter

format_name('john', 'tron')
