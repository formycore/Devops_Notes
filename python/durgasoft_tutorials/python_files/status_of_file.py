def status_of_file(mode):
    f = open('abc.txt', mode)
    print('what is the file name: ', f.name)
    print('what is the file mode: ', f.mode)
    print('is the file readable: ', f.readable())
    print('is the file writable: ', f.writable())
    print('is the file closed: ', f.closed)
    f.close()
    print('is the file closed: ', f.closed)
    print('-------------------------')

#status_of_file('w')
file_modes = ['r', 'w', 'a', 'r+', 'w+', 'a+']
for mode in file_modes:
    status_of_file(mode)