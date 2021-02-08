def rxlsx(path):
    with open(path, mode='r+b') as file:
        body = file.read()
        return body
