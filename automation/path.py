import os
import io
# p1 = os.path.join('usr', 'bin', 'spam')



path1 = os.path.join('var', 'www', 'html', 'node', 'crawler')
print(path1)

if os.path.isdir('/var/www/html/node/crawler/automation'):
    print('Folder exists, checking file')
    if os.path.exists('/var/www/html/node/crawler/automation/phonenumber.py'):
        print('File exists, good to go!')
    else:
        print('File does not exists, creating file')

file1 = open('/var/www/html/node/crawler/automation/phonenumber.py', 'a')
# second argument 'a' stands for append

read1 = file1.read()
