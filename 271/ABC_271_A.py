n = int(input())

hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

if n <= 15:
    print('0' + hex[n])
else:
    print(hex[n//16] + hex[n%16])