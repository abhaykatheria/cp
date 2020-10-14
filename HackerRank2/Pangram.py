def pangram(string1):
    import string
    small=set(string.ascii_lowercase)
    big=set(string.ascii_uppercase)
    if small<=set(string1.lower()) or big <=set(string1.upper()):
        print("pangram")
    else:
        print("not pangram")

string1=str(input())
pangram(string1)