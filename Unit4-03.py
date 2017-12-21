# Created by: Peter Zhu
# Created on November 2 2017
# Created for ICS3U

def postal_address(address, city, province, postal_code,apt_number = None):
	
    if(apt_number == None):
       print (address+' ' +city+' ' +postal_code+' ' +province)
    else:
       print (address+' ' +city+' ' +postal_code+' ' +province+' ' +apt_number)

user_address = raw_input("Enter your address here ",)
user_city = raw_input("Enter your city name here ",)
user_postal_code = raw_input("Enter your postal code here ",)
user_province = raw_input("Enter your province here ",)
user_apt_number = raw_input("Enter your appartment number here ",) 
postal_address(user_address, user_city, user_postal_code, user_province, user_apt_number ) 
