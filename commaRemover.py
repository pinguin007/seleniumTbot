def comma_remover(text):
    list_version= list(text)
    for i in  list_version:
        if i==',':
            list_version.remove(i)
    finalnum= ''.join(list_version)

    return int(finalnum)