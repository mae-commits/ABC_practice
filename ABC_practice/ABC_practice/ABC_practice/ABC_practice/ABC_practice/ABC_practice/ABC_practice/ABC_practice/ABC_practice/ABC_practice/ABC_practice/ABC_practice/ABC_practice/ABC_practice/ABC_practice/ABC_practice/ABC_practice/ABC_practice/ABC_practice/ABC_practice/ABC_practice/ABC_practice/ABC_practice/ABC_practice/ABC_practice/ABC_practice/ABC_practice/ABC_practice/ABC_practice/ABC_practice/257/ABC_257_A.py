def main():
    N,X = map(int,input().split())
    count = X//N # X th alphabet is linked to the X//N  
    if count == X/N:
        print(chr(count + 64)) # change  the ascii codes to alphabet assigned to the number 
    else:
        print(chr(count + 65))

if __name__ == "__main__":
    main()