#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:01:35 2018

@author: lrgtomaszewski
"""

def getMode():
    print('Do you wish to encrypt or decrypt a message?')
    mode = input()
#This allows for the user to input the choice of encrypting a message 
#or decrypting a message.
    if mode in  'e encrypt'.split():
        print(Encryption())
        return mode
#If the user inputs any of the strings listed in line 14 then, it will 
#print the encryption code. So it follows the encrytion process.
    elif mode in 'd decrypt'.split():
        print(Decryption())
        return mode
#If the user inputs any of the strings listed in line 19 then, it will 
#print the encryption code. So it follows the encrytion process.
    else:
        print('For Encryption, enter either "e", "encrypt".') 
        print('For Decryption, enter either "d", "decrypt".')
#If the user doesn't input any of the strings listed in line 14 & 19
#then, it will print the message listed in line line 25/26 so it 
#advises the user the direct input it requires to proceed.

def Encryption():
    ERead = open('plaintext.txt', 'r').read()
#This opens the plaintext.txt file and reads it, if the user did not
#want to source form a txt file then the code can be replaced in line
#32 by;
      #print('Enter message to be encrypted!')
      #ERead = input()
    print('Please enter unique key for Encryption!')
    Ekey = input()
#Line 38 & 39 allows the user to input a unique key that is the 
#important reference to which the code encrypts and decrypts, thus 
#typing the key in has to be correct.
    EMessage = len(ERead)
    EKey = Ekey * (1 + EMessage//len(Ekey))
#Both the message and key in lines 32 & 39 are now broken down for
#their lengths.
    EWrite = open('plaintext.txt.enc.txt', 'w')
#This is the location where the encrypted text with outputted too.
#This allows the code to write into a .txt file.
    for i in range(EMessage):
        EPi = ord(ERead[i])
        Eki = ord(EKey[i]) - 32
        ECi = EPi + Eki
#The above sequences allow for the mathematical formula for 
#encrypting a message. Lines 51 converts the individual letters 
#of the message into numbers that corresponds with ASCII 1967 
#defintions. Line 52 Does the following but with the key instead
#of the message, 32 is then subtracted but the numbers the individual
#letters so that the key is not greater than 126 which is the highest
#number in the ASCII 1967 defintions. It is the added together to 
#encrypt the letter via a number.
        if ECi > 126:
            ECi = ECi - 95
#If the final value of ECi is greater than 126 (The max limit of the
#ASCII 1967 defintions), similiar what happens to the key in line 52.
        E = chr(ECi)
#Line 53 adds the key and the letter togehter to get a single number
#the muber is thus changed back into a letter in relation to the 
#ASCII 1967 defintions. This allows the message in line 32 to be 
#"encrypted" but replaces the orginal message with the encrypted 
#message. Which is saved in a .txt file named in line 47.
        print(EPi, Eki, ECi, E)
        EWrite.write(E)
    EWrite.close()
    print('System Message: Encryption Complete')
#The lines 73 & 74 writes the encrypted text into a seperate file
#labelled in line 47, and closes it, stops the writing to the file.

def Decryption():
    DRead = open('plaintext.txt.enc.txt', 'r').read()
#This opens the plaintext.txt.enc.txt file and reads it, if the user
#did not want to source form a txt file then the code can be replaced 
#in line 80 by;
             #print('Enter message to be Decrypted!')
             #ERead = input()
    print('Please enter unique key for Decryption!')
    Dkey = input()
#Line 86 & 87 allows the user to input a unique key that is the 
#important reference to which the code decrypts, thus typing the 
#key in has to be correct and has to be the same as the key set 
#during the encryption phase.
    DMessage = len(DRead)
    DKey = Dkey * (1 + DMessage//len(Dkey))
#Both the message and key in lines 80 & 87 are now broken down for
#their lengths.
    DWrite = open('plaintext.txt.enc.dec.txt', 'w')
#This is the location where the Decrypted text with outputted too.
#This allows the code to write into a .txt file.
    for i in range(DMessage):
        DPi = ord(DRead[i])
        Dki = ord(DKey[i]) - 32
        DCi = DPi - Dki
#The above sequences allow for the mathematical formula for 
#decrypting a message, its is the reverse method to encrypting a 
#file. Line 100 converts the individual letters of the message into 
#numbers that corresponds with ASCII 1967 defintions. Lines 101 Does 
#the following but with the key instead of the message, 32 is then 
#subtracted but the numbers the individual letters so that the key 
#is not greater than 126 which is the highest number in the ASCII 
#1967 defintions. The value of the letters in the message then is 
#taken away from the value of letters in the key to encrypt the 
#letter via a number.
        if DCi < 32:
            DCi = DCi + 95
#If the final value of DCi is greater than 126 (The max limit of the
#ASCII 1967 defintions), similiar what happens to the key in line 101.
        D = chr(DCi)
#Line 102 minus the key and the letter togehter to get a single number
#the muber is thus changed back into a letter in relation to the 
#ASCII 1967 defintions. This allows the message in line 80 to be 
#"encrypted" but replaces the orginal message with the encrypted 
#message. Which is saved in a .txt file named in line 96.
        print(DPi, Dki, DCi, D)
        DWrite.write(D)
    DWrite.close()
    print('System Message: Decryption Complete')
#The lines 124 & 125 writes the decrypted text into a seperate file
#labelled in line 96, and closes it, stops the writing to the file.

Cipher = getMode()
print(Cipher)