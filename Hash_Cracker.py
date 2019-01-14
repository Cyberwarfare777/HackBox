import time
import hashlib
import os
import sys
import threading
from termcolor import colored


print(''' 

                *********** This Product is Made By Anonymous Hacker. Dec 2018 **************
                        From Contact : https://github.com/Cyberwarfare777/HackBox
                                Copyright From Anon Hacker 2018-2022

                                Warning : Do Not Use as illegal Purpose


''')

os.system('clear')
print(colored('\t\t\t\t\tAnonymous Hash Decrypter (Md5, SHA256, SHA251)\n', 'cyan'))
print('\t\t\t\t\t Starting At',time.asctime())
print('\n')

# Create a function Take User hash

def MD5_M(hash_num, wordlist_path):
    counter = 1
    try:
        wordlist_path = open(wordlist_path, 'r')
    except:
        print(colored('Sorry, File Does Not Exist', 'red'))
        sys.exit(1)
    
    for password in wordlist_path:
        hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
        # os.system('clear')
        start_time = time.time()
        print(colored('\nTrying Password {} '.format(counter), 'red'))
        # time.sleep(0.1) # it is optional
        counter += 1
        end_time = time.time()
        total_time = end_time - start_time

        if hash_obj == hash_num:
            sys.stdout.write(colored(f'\nCongradulations!!! The Password is {password}', 'green'))
            sys.stdout.write(colored(f'Total Time is {total_time}\n', 'white'))
            sys.exit(0)
        else:
            pass

# Pass value in function

hash_value = input('Enter Your Hash Value : ') # give md5 password
path = input('Please Give Path Of Wordlist : ') # enter path

# MD5_M(hash_value, path) # call function and pass arguments

process = threading.Thread(target=MD5_M, args=(hash_value, path, ))

process.daemon = True
process.start() # here is start threading now
process.join() # wait
