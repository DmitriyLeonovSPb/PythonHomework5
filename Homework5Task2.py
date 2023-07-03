folder = r'C:\Home1\Docss\secret.txt'
def parcelink(linkk: str) -> tuple():
    a = folder.split("\\")
    b = a[-1].split(".")
    if a[-1] in folder:
       way = folder.replace(a[-1],'')
    file_name = b[0]
    extension = b[1]
    return way, file_name, extension
answer = parcelink(folder)
print(answer)



