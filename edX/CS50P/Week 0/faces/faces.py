def main():
    text = input()
    convert(text)

def convert(txt):
    txt = txt.replace(':)', '🙂')
    txt = txt.replace(':(', '🙁')
    print(txt)

main()