# Created by: Alireza Teimoori
# Created on: Dec 2017
# Unit_6-02
# uses function inside class
from enum import Enum
import sys


street = Enum('BLVD','CRES','DR','LANE','CRT')

class MailAddress():
    def __init__(self, house_number, street_name, street_type):
        
        self.house_number = house_number
        self.street_name = street_name
        self.street_type = street_type
        
    def fast_address(self):
        self.fast_address = self.house_number + " " + self.street_name + " " + self.street_type
        
        return self.fast_address

house_number = raw_input('enter your house number: \n')
street_name = raw_input('enter your street name: \n')
street_type_user= raw_input('enter your street type: \n')

if street_type_user in street:
    street_type = street_type_user
else:
    print("don't start this again :/ ...")
    print("I can stand this no more...")
    print("Goodbye and do not come back!")
    
    sys.exit()
    

a_mailing_address = MailAddress(house_number,street_name,street_type)


print(a_mailing_address.fast_address())
