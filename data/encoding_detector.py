import chardet

with open('cancer_reg.csv', 'rb') as f :
    result = chardet.detect(f.read())
    print(result)