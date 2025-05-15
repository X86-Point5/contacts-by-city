#app.py
"""
Contact Book Application (ContactsByCity)

Uses a dictionary to store contacts from a csv "contacts.csv" and then allows
for manipulation and display of the contact book within the console menu.

Features:
-Contact Adding (With Checking for Email Repeats)
-Contact Removal
-Filtering By City
"""

__author__ = "Maximus Barraza (Github: X86-Point5)"
__version__ = "1.0.0"
__date__ = "2025-05-15"

#clearing the screen
import os

#early program exit
import sys

#reading and writing dictionaries from csv files
from FileOperator import get_csv_dictionary, dictionary_to_csv

#single character input handling
from InputHandler import input_char, input_string


#takes the dictionary from "contacts.csv"
contacts_dict = get_csv_dictionary("contacts.csv")

proper_headers = {'FirstName', 'LastName', 'City', 'Email'}

#incase the contacts could not be loaded correctly the program should not run
#checks if all of the headers exist and that all headers have the same length
if((not contacts_dict) or (proper_headers != set(contacts_dict.keys())) or 
   len(set(len(contacts_dict[k]) for k in contacts_dict)) != 1):

    #outputs an error message and ends the program
    print('\n\tERROR: The "contacts.csv" file has been tampered with, ending the program')
    sys.exit()

#initializes city_filter to None so that all cities are displayed
city_filter = "None"
while True:

    #clears the screen
    os.system("cls")

    #outputs the header
    print("\n\t----- Stored Contacts -----\n")

    #counts the amount of contacts printed
    contacts_printed = 0

    #loops through every contact
    for index in range(len(contacts_dict['FirstName'])):

        #if the city filter is disabled then the contact information for 
        #each contact is printed
        if city_filter == "None":
            print(f"\t{contacts_dict['FirstName'][index]} {contacts_dict['LastName'][index]}: ")
            print(f"\t{contacts_dict['City'][index]}, {contacts_dict['Email'][index]}\n")
            contacts_printed += 1

        #if the city filter is enabled then only contacts from the given
        #city will be printed
        elif city_filter == contacts_dict['City'][index]:
                print(f"\t{contacts_dict['FirstName'][index]} {contacts_dict['LastName'][index]}: ")
                print(f"\t{contacts_dict['City'][index]}, {contacts_dict['Email'][index]}\n")
                contacts_printed += 1

    #incase no contacts ever get printed then a text is outputted
    #to indicate this
    if contacts_printed == 0:
        print("\tNo Matching Contacts\n")

    #the menu for the contact screen
    print("\t-----------------------------")
    print('\tEnter "F" to filter for a')
    print('\tcity, "A" to add a contact,')
    print('\t"R" to remove a contact by')
    print('\temail or "X" to exit the ')
    print('\tprogram and save the information')
    print("\t-----------------------------")

    #controls the menu for the program
    control_char = input_char("\tEnter: ", "afxr")

    #if the user wants to add a contact
    if control_char == "A":
        #adds the first and last names to the contact book
        contacts_dict['FirstName'].append(input("\tEnter the first name of the contact   : "))
        contacts_dict['LastName'].append(input("\tEnter the last name of the contact    : "))

        #ensures that no repeat emails are added to the contact book
        contacts_dict['Email'].append(input_string("\tEnter the email of the contact        : ",
                                                   contacts_dict['Email'], "\tERROR - Email already exists"))

        #adds the city of the contact
        contacts_dict['City'].append(input("\tEnter the city of the contact         : "))

    #if the user wants to filter the contact
    elif control_char == "F":
        #gets the city to filter for
        city_filter = input('\tEnter the city filter or "None" for no filter: ')

    #if the user wants to remove a contact
    elif control_char == "R":

        #retreives an email to remove
        email_to_remove = input("\tEnter the email to be removed: ")

        #attempts to remove the email by getting an index and deleting it
        try:
            #gets the index of the email
            remove_index = contacts_dict['Email'].index(email_to_remove)

            #deletes all contact information from the dictionary
            contacts_dict['FirstName'].pop(remove_index)
            contacts_dict['LastName'].pop(remove_index)
            contacts_dict['Email'].pop(remove_index)
            contacts_dict['City'].pop(remove_index)

            #outputs removal success
            print("\n\tContact successfully removed", end="\n\n\t")
        except ValueError:

            #outputs removal failure
            print("\n\tERROR - Email does not exist", end="\n\n\t")

        #waits for the user before the code runs
        os.system("pause")

    #if the user exits the program
    elif control_char == "X":

        #saves the new contact information to the contacts file
        dictionary_to_csv(contacts_dict, "contacts.csv", list(contacts_dict.keys()))
        break
    
