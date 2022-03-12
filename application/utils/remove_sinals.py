sinais = ['!', '?']

def remove_sinals(string: str):
    for i in string:
        if i in sinais:
            string = string.replace(i, '')
    
    return string