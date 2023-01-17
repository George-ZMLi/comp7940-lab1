
def main():
    print('Hello World')
    
def print_factor(x):
    for i in range(x+1):
        if i != 0 and x % i == 0:
            print(i, x/i)

if __name__ == '__main__':
    main()
    l = [52633,8137,1024,999]
    for j in l:
        print_factor(j)
