infile = open('phonebook.in')
outfile = open('phonebook.out', 'w')
emailaddress = {}
for email in infile:
    emailaddress[email.strip()] = infile.readline().strip()

#0. means to go back to menu 
#1. Look up email address
#2. Add new name and email address
#3. Change existing email address
#4. Delete name and email address
#5. Save and exit
choice = input('Enter\n1) look up an email address\n2) add a new name and email address\n3) change an email address\n4) delete a name and email address\n5) save address book and exit:\n')
while choice <= '6':
    if choice == '0':
        choice = input('Enter\n1) look up an email address\n2) add a new name and email address\n3) change an email address\n4) delete a name and email address\n5) save address book and exit\n')
        
    elif choice == '1':
        try:
            lookup = input('Enter name: ')
            print(emailaddress[lookup])
            choice = input('press 0 to go back to main menu, if you are done')
            if (input == '0'):
                #choice = '0'
                continue
            
        except:
            print ('Sorry, no contact exists under that name')
            choice = input('Enter\n1) look up an email address\n2) add a new name and email address\n3) change an email address\n4) delete a name and email address\n5) save address book and exit\n')
               
    elif choice == '2':
        newname = input('Enter new name: ')
        newemail = input('Enter new email address: ')
        emailaddress[newname] = newemail
        print(emailaddress)
        choice = input ('press 0 to go back to main menu, if you are done')
        if (newname == '0'):
            #choice = '0'
            continue 
        
    elif choice == '3':
        lookname = input('Whose email would you like to change?\n')
        upemail = input("Enter email\n'")
        emailchange = {lookname : upemail}
        emailaddress.update(emailchange)
        print(emailaddress)                        
        choice = input ('press 0 to go back to main menu, if you are done')
        if (lookname == '0'):
            #choice = '0'
            continue  

    elif choice == '4':
        lookname = input('Enter name of entry that you would like to delete: ')
        try:
            print(emailaddress[lookname])
            print('Are you sure you want to delete this entry? (yes/no)')
            doublecheck = input('')
            if (doublecheck == 'yes'):  
                del emailaddress[lookname]
                if (doublecheck == '0'):
                    #choice = '0'
                    continue
            else:
                doublecheck == 'no' 
                choice = input ('press 0 to go back to main menu, if you are done')
                if (doublecheck == '0'):
                    #choice = '0'
                    continue                
        except:
            print('That name is not valid')
            if (doublecheck == '0'):
                    #choice = '0'
                    continue
            continue

    elif choice == '5':
        break
    
    choice = input('Enter\n1) look up an email address\n2) add a new name and email address\n3) change an email address\n4) delete a name and email address\n5) save address book and exit:')
    #outfile.close(phonebook.out)
        
    for key, val in emailaddress.items():
        outfile.write('{0}, {1}\n'.format(key, val)) 
        #outfile.write(emailaddress[val])
        #outfile.write(val+'\n')
                      
outfile.close()                      
infile.close()
