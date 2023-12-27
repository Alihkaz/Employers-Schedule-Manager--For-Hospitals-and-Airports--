#imports

import time
import requests
from datetime import datetime

# ____________________________________________________________________________________________________

# Constants and keys:

spreadsheet_endpoint="Your sheety end point" 
#the link to the forms that we want to fill the data with






today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%A").upper()



# ________________________________getting the name and the ID_________________________________________________



employer_name=input('Please Enter your name:\n') #getting the name of the user 
employer_ID=int(input('Please Enter your ID:\n'))+1 #getting the name of the user


# _____________________________________________________________________________________________________________



#Using Get request to search for the user according to his ID in the google forms , in addition
# to checking the status of his scudeuale to give him a new combination according to the allowed hours which is 40 hours ! 
# In addition to spliting the user sceduale data to see what is allowed
#for him and what not, and what is remaining for him and what not !


try:
   header={
      "Authorization": 'Bearer Your Bearer Token'
        }
   sheet_response = requests.get(url=f'{spreadsheet_endpoint}/{employer_ID}', headers=header)
   sc_data=sheet_response.json()
   print(sheet_response.json())
    
   nb_of_n_shifts= len(sc_data['N'])   #checking the nnumber of night shifts he added
   nb_of_s_shifts=len(sc_data['S'])    #checking the number of short day shifts 
   nb_of_l_shifts=len(sc_data['L'])    #checking the number of long day shifts 


   # These combinations will translate the allowed
   # Maximum and minimum hours of work,
   # Which is 40 hour distributed on different combinations !
   #and this will cover all the cases that are only a;;owes 
   #which represents the maximum number of worked hours whch is 40 , and maximum working days which is 6 days 
   #, less is allowed , but with completing the 40 hours, satisfying this collection ['NNNN','SSSSNN','LLLLL','LSLSN','NSNSN','NLNSL'] 
   #and to satisfy this rule 
   #, we will check the number of n s l characters in the combinations and make sure that there numbers doesn't
   #exceeds the corresponding ammount in the combination !


   if nb_of_n_shifts==4 or nb_of_l_shifts==5 : 
     print("sorry , you have reached the maximum range of working hours" )


   if nb_of_n_shifts==1 or nb_of_s_shifts==1 or nb_of_l_shifts==1:
    shift_type=input('please Choose your shift type:\n  1.S\n   2.L\n   3.N\n').upper()
   

   # For n
   if nb_of_n_shifts==3 : 
    shift_type=input('please Choose your shift type:\n  1.S\n ').upper()
    


   if nb_of_n_shifts==2:
    shift_type=input('please Choose your shift type:\n  1.S\n   2.L\n   3.N\n').upper()
   

    
   # For s 
   if nb_of_s_shifts==4:
    shift_type=input('please Choose your shift type:\n   N\n').upper()
    
   
   if nb_of_s_shifts==2:
    shift_type=input('please Choose your shift type:\n  1.S\n   2.L\n   3.N\n').upper()
   

   if nb_of_s_shifts==3:
    shift_type=input('please Choose your shift type:\n  1.S\n   2.N\n').upper()
   
   # For L
   if nb_of_l_shifts==4:
    shift_type=input('please Choose your shift type:\n  1.L\n').upper()
    

   if nb_of_l_shifts==2:
    shift_type=input('please Choose your shift type:\n  1.N\n  2.S\n  3.L\n ' ).upper()
    

   if nb_of_l_shifts==3:
    shift_type=input('please Choose your shift type:\n  1.L\n').upper()
   


#if the user id is not found , then we will create a new row for him/here
except:
   shift_type=input('please Choose your shift type:\n  1.S\n   2.L\n   3.N\n').upper()
   sheet_inputs = {
           "sheet": 
           {
            'Name' :employer_name,
            'ID': employer_ID ,
            f'{now_time}' : shift_type,
            
            }
            }
   header={
      "Authorization": 'Bearer Your Bearer Token'
        }

   sheet_response = requests.post(url=spreadsheet_endpoint, json=sheet_inputs, headers=header)
   print(sheet_response.text)
else:   #sending the data to sheety , that contains the filtered combination ! 
    header={
      "Authorization": 'Bearer Your Bearer Token'
        }

    sheet_inputs = {
           "sheet": 
           {
            'Name' :employer_name,
            'ID': employer_ID ,
            f'{now_time}' : shift_type,
            
            }
            }
    sheet_response = requests.post(url=spreadsheet_endpoint, json=sheet_inputs, headers=header)  
    print(sheet_response.text)





