import os

i = 0

print(' ')
print('=======================================')
print('=======================================')
print('=======================================')

for foldername, subfolders, filenames in os.walk('/var/www/html/node/crawler'):
    print('The current folder is ' + foldername)

    # for subfolder in subfolders:
        # print('SUBFOLDER of ' + foldername + ' is ' + subfolder)
        # print(i)

    for filename in filenames:
        print('FILE INSIDE ' + foldername + ': ' + filename)

    # print('%s %d' % (foldername, i))

print('')
