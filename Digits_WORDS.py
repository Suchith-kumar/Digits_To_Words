# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:23:07 2015

Program to print Digits in to equivalent words representation

@author: Suchith kumar
"""

# Number_TO_Words() function :
#                           
#                           Consists of Word_Set a dictionary that has set of
#                           <digit,word> key-value pairs for mapping digits 
#                           with equivalent words
#
#       1. Invokes DigitPlace() for extracting individual digits
#       2. Invokes Word_Conversion() to convert digits to words
#       Finally prints the output as a string

def Number_To_Words(num):
    Word_Set = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0:'' }
    if num == 0:
        print("zero")
        return
    digitval_list = DigitPlace(num)
    Number_in_words=Word_Conversion(digitval_list,Word_Set)
    print(Number_in_words)


# Word_Conversion() function :
#                             Converts the digits into words. Basically map
#                             the digit to words in the dictionary object
#                            <digilist> -> contains list of digits(units,tens,
#                             upto 1 lakhs) 
#                            words -> represents the Word_Set{} dictionary

def Word_Conversion(digilist,words):
    wstr=''                     #wstr->word string that holds the digit's word
    count=0                     #count->to keep track of the digit place value
    
    for item in digilist:
       #Check for Unit place 
        if count==0 :
            if item==0 :
                if digilist[count+1]!=0 :
                    count +=1
                    temp=10+item  #temp->to represent 10,11,....19 
                    continue
            if len(digilist)>1 and digilist[count+1]==1 :
                count+=1
                temp=10+item
                continue
            else:
                wstr=words[item]
                
        #Check for the tenth's place        
        if count==1 :
            if item==1 :
                wstr=words[temp]+" "+wstr
            else :
                w=10*item        #w->to represent 20,30,40,....90
                wstr=words[w]+" "+wstr.lower()
        
        #Check for the hundredth place
        if count==2 :
            if item==0 :
                if digilist[count+1]!=0 :
                    count +=1
                    continue
            elif len(digilist)>3 and digilist[count+1]!=0 :
                wstr=words[item]+" "+"hundred and"+" "+wstr.lower()
                count+=1
                continue
            else:
                wstr=words[item]+" "+"hundred and"+" "+wstr.lower()
        #Check for the thousand place 
        if count==3 :
            if item==0 :
                if digilist[count+1]!=0 :
                    count +=1
                    temp=10+item
                    continue
            if len(digilist)>4 and digilist[count+1]!=0 :
                wstr=words[item]+" "+"thousand"+" "+wstr.lower()
                count+=1
                continue
            else:
                wstr=words[item]+" "+"thousand"+" "+wstr.lower()
        
        #Check for the Ten thousands place        
        if count==4 :
            if item==1 :
                wstr=words[temp]+" "+"thousand"+" "+wstr.lower()
            else:
                w=10*item
                wstr=words[w]+" "+wstr.lower()
                
        #Check for the one lakh place
        if count==5 :
            if item==0 :
               if digilist[count+1]!=0 :
                    count +=1
                    temp=10+item
                    continue
            else:
                wstr=words[item]+" "+"lakh"+" "+wstr.lower()
                
        #Check for the ten lakh place
        if count==6 :
            if item==1 :
                wstr=words[temp]+" " +"lakh"+" "+wstr.lower()
        count+=1

    return wstr


# DigitPlace() function :
#                        Produces the unit,tenth,hundred upto 1lakh places
#                        digits
#       1. Find the remainder and store it in list object
#       2. Return the list object finally

def DigitPlace(number):
    dlist=[]
    while(number>0):
        rem=number%10
        dlist.append(rem)
        number//=10
    return dlist


#Accept the User input
#  try and except block to catch the errors    
try:
    inp = int(input("Enter the number : "))
    
    if inp<1000000 :
        Number_To_Words(inp)
    elif inp<0 :
        raise ValueError('Negative numbers **** NOT ALLOWED ****')
    else :
        raise ValueError('Number exceeds **** 1,000,000 *****')
       
except ValueError as err:
    print(err.args)

