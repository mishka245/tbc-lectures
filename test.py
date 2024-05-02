def main():
    num = int( input('enter number between 100 and 1000): '))

    num_list = []
    if(100<= num < 1000):
        for i in range (1, num):
            if(i% 13 == 0):
                num_list.append(i)

        print('jeradebia', str(num_list) [1:-1])
        print('jeraebis radenobaa: ' , len(num_list))
    else:
        print('wrong number')

if __name__ == '__main__':
    main()