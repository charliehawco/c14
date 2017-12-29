import itertools, random, datetime, time

#Ok, so basically this program should take the measurements of each character in the alphabet plus capitals, then create a list of
#all possible combinations of letters and check to see if they fit the width of a redacted area of text
#obviously, if an accepted combination (because it's the correct size) contains spaces, then obviously it's not going to come up
#with a word in the dictionary, so it then adds those strings to a separate list then splits them by spaces
#then runs it through the dictionary

#ps I'd prefer it if you kept this to yourself for now, wanting to write a paper on it
#:)







#00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#Open data files

TextFile_CharacterData_EntireFile = open("ConfigTest2.txt","r")
Lst_CharacterData = list(TextFile_CharacterData_EntireFile.readlines())

TextFile_Dictionary_EntireFile = open("github_english_words_master.txt","r")
Lst_DictionarySearch = list(TextFile_Dictionary_EntireFile.readlines())

#End
#00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

#00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#1) Calculate semi-colon positions for constants line (line 1)
#2) Declare constants

intTemp0 = Lst_CharacterData[1].find(";") #semi-colon 0, line 1
intTemp1 = Lst_CharacterData[1].find(";", intTemp0 + 1) #semi-colon 1, line 1
intTemp2 = Lst_CharacterData[1].find(";", intTemp1 + 1) #semi-colon 2, line 1
intTemp3 = Lst_CharacterData[1].find(";", intTemp2 + 1) #semi-colon 3, line 1
intTemp4 = Lst_CharacterData[1].find(";", intTemp3 + 1) #semi-colon 4, line 1

nCharacters = int(Lst_CharacterData[1][0:intTemp0])
min_nSamples_perCharacter = int(Lst_CharacterData[1][(intTemp0 + 1):(intTemp1)])
max_RSD_perCharacter = int(Lst_CharacterData[1][(intTemp1 + 1):(intTemp2)])
Width_RedactedText = int(Lst_CharacterData[1][(intTemp2 + 1):(intTemp3)])

temp_date_year = (str(datetime.datetime.today()))[0:4]
temp_date_month = (str(datetime.datetime.today()))[5:7]
temp_date_day = (str(datetime.datetime.today()))[8:10]
temp_time_hour = (str(datetime.datetime.today()))[11:13]
temp_time_minute = (str(datetime.datetime.today()))[14:16]
temp_time_second = (str(datetime.datetime.today()))[17:19]
temp_date_all = (temp_date_day + "-" + temp_date_month + "-" + temp_date_year)
temp_time_all = (temp_time_hour + ":" + temp_time_minute + ":" + temp_time_second)

Width_RedactedText = 139 #TEMP VALUE ONLY, THIS LINE NEEDS TO BE DELETED

#00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#Prepare lists and tuples for analysis

Lst_CharacterData_LengthOf = len(Lst_CharacterData)
Lst_DictionarySearch_LengthOf = len(Lst_DictionarySearch)

#strips all new line characters from Lst_CharacterData and Lst_DictionarySearch
for i in range(0, nCharacters, 1):
    Lst_CharacterData[i] = (str(Lst_CharacterData[i])).strip("\n")

for i in range(0, Lst_DictionarySearch_LengthOf, 1):
    Lst_DictionarySearch[i] = (str(Lst_DictionarySearch[i])).strip("\n")

tempList0 = []
tempList1 = []
tempList2 = []
tempList3 = []
tempList4 = []
Lst_PossibleAnswers = []
Lst_PossibleAnswers2 = []
Lst_Rejections = []

for i in range(0, nCharacters, 1):
    tempString = (str((Lst_CharacterData[i + 3]))).split(";") #splits each line (starting from 3) from Lst_CharacterData by semi-colon
    tempList0.append(tempString[0]) #adds the first element of the split line (line of code above this one) and adds to a temporary list
    tempList1.append(int(tempString[1]))
    tempList2.append(int(tempString[2]))
    tempList3.append(int(tempString[3]))
    tempList4.append(tempString[4])

tpl_iCharacter = tuple(tempList0) #creates a tuple from each element of the list 'tempList0'
tpl_iCharAvrgWidth = tuple(tempList1)
tpl_iCharacter_nSample = tuple(tempList2)
tpl_iCharacter_RSD = tuple(tempList3)
tpl_iCharacter_Samples = tuple(tempList4)

#End
#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#Check sample n values

ZeroValues_SampleNo_count = 0
LowValues_SampleNo_count = 0

#Checks to see how many characters have a) low sample numbers, and b) zero values
for i in range(0, nCharacters, 1):
    if tpl_iCharacter_nSample[i] < min_nSamples_perCharacter:
        LowValues_SampleNo_count = LowValues_SampleNo_count + 1
    elif tpl_iCharacter_nSample[i] == 0:
        ZeroValues_SampleNo_count = ZeroValues_SampleNo_count + 1

#End
#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#Check RSD values

HighValues_RSD_count = 0
ZeroValues_RSD_count = 0

#Checks to see how many characters have a) high RSD values, and b) zero values
for i in range(0, nCharacters, 1):
    if tpl_iCharacter_RSD[i] > max_RSD_perCharacter:
        HighValues_RSD_count = HighValues_RSD_count + 1
    elif tpl_iCharacter_RSD[i] == 0:
        ZeroValues_RSD_count = ZeroValues_RSD_count + 1

#End
#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#Find smallest character in array

#Set initial value to the value of the first item in the array
smallestWidth_inArray = tpl_iCharAvrgWidth[0]
largestWidth_inArray = tpl_iCharAvrgWidth[0]

for i in range(0, nCharacters, 1):
    #if Width of Character x is less than min_CharacterWidth_inArray
    if tpl_iCharAvrgWidth[i] < smallestWidth_inArray:
        #then set min_CharacterWidth_inArray = Width of Character x
        smallestWidth_inArray = tpl_iCharAvrgWidth[i]
    if tpl_iCharAvrgWidth[i] > largestWidth_inArray:
        largestWidth_inArray = tpl_iCharAvrgWidth[i]

max_CharactersPossible = 0
while (Width_RedactedText - (2 * tpl_iCharAvrgWidth[52])) > (smallestWidth_inArray * max_CharactersPossible):
    max_CharactersPossible = max_CharactersPossible + 1

min_CharactersPossible = 0
while (Width_RedactedText - (2 * tpl_iCharAvrgWidth[52])) > (largestWidth_inArray * min_CharactersPossible):
    min_CharactersPossible = min_CharactersPossible + 1

if max_CharactersPossible < 30:
    MaxValue_forAnalysis = max_CharactersPossible #because range() starts at 1 this time, we don't need to + 1 onto this value
else:
    MaxValue_forAnalysis = 30 #remember when using range() top value is excluded, so 30 not 29

if min_CharactersPossible > 0 and min_CharactersPossible < max_CharactersPossible:
    MinValue_forAnalysis = min_CharactersPossible
else:
    MinValue_forAnalysis = 1

#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#Program start

print("===============================================================================")
print("System Time: " + temp_time_all)
print("System Date: " + temp_date_all)

print("") #SPACER
print("") #SPACER

Smpl_ver_header = "    Sample data verification . . . . . . . . . . . : "
Smpl_check_header = "    Sample check . . . . . . . . . . . . . . . . . : "
RSD_ver_header = "    STDEV data verification. . . . . . . . . . . . : "
RSD_check_header = "    STDEV check. . . . . . . . . . . . . . . . . . : "
Char_ver_header = "    Character data verification. . . . . . . . . . : "
Trgt_ver_header = "    Redacted text width value. . . . . . . . . . . : "

print("Data Verification:")
if Lst_CharacterData_LengthOf == nCharacters + 3:
    print(Char_ver_header + "Number of lines in Lst_CharacterData list correspond with nCharacters value")
elif Lst_CharacterData_LengthOf != nCharacters + 3:
    print(Char_ver_header + "Number of lines in Lst_CharacterData list do not correspond with nCharacters value")
else:
    print(Char_ver_header + "ERROR - possible misssing data from original character data text file!")

if Width_RedactedText > 0:
    print(Trgt_ver_header + "Value present (" + str(Width_RedactedText) + ")")
elif Width_RedactedText == 0:
    print(Trgt_ver_header + "Value missing")
else:
    print(Trgt_ver_header + "ERROR")

if ZeroValues_SampleNo_count == 0:
    print(Smpl_ver_header + "All characters have at least one sample present")
elif ZeroValues_SampleNo_count != 0:
    print(Smpl_ver_header + "ERROR - At least one character has no samples")
else:
    print(Smpl_ver_header + "ERROR")

if ZeroValues_RSD_count == 0:
    print(RSD_ver_header + "All characters have a value (other than 0) present in the RSD column (no indication of acceptable-ness)")
elif ZeroValues_RSD_count != 0:
    print(RSD_ver_header + "At least one character has an RSD value of zero, or is missing a value altogether")

print("") #SPACER

print("Data Quality Checks:")

if LowValues_SampleNo_count > 0:
    print(Smpl_check_header + "At least one character has less samples than specified (" + str(min_nSamples_perCharacter) + ")")
elif LowValues_SampleNo_count == 0:
    print(Smpl_check_header + "All characters have acceptable sample numbers")
else:
    print(Smpl_check_header + "ERROR")

if HighValues_RSD_count > 0:
    print(RSD_check_header + "At least one character has an RSD value greater than the one specified (" + str(max_RSD_perCharacter) + ")")
elif HighValues_RSD_count == 0:
    print(RSD_check_header + "All characters have acceptable RSD values")
else:
    print(RSD_check_header + "ERROR")

print("") #SPACER

print("Smallest character in array. . . . . . . . . . : " + str(smallestWidth_inArray))
print("Largest character in array . . . . . . . . . . : " + str(largestWidth_inArray))
print("Min. number of characters in redacted text . . : " + str(min_CharactersPossible))
print("Max. number of characters in redacted text . . : " + str(max_CharactersPossible))

print("") #SPACER

print("Character Table")
print("===============================================================================")
print("Character" + "   " + "Avrg. Width" + "   " + "Samples (n)" + "   " + "RSD (%)" + "   " + "Sample list")

for i in range(0, nCharacters, 1):
    TempStringQ = str(tpl_iCharacter[i]).ljust(9)
    TempStringR = str(tpl_iCharAvrgWidth[i]).ljust(11)
    TempStringS = str(tpl_iCharacter_nSample[i]).ljust(11)
    TempStringT = str(tpl_iCharacter_RSD[i]).ljust(7)
    TempStringU = str(tpl_iCharacter_Samples[i])
    print(TempStringQ + "   " + TempStringR + "   " + TempStringS + "   " + TempStringT + "   " + TempStringU)

print("===============================================================================")

print("") #SPACER
print("") #SPACER

print("Analysis start")
print("===============================================================================")

#time.sleep(5)

Lst_iCharacter_Results = []

for iCombinationLength in range(MinValue_forAnalysis, MaxValue_forAnalysis):
  for aCombination in itertools.product(tpl_iCharacter, repeat=iCombinationLength):
    str_Combination = ''.join(aCombination)

    tmp_sum = 0
    for k in range(0, len(aCombination), 1):
        for i in range(0, nCharacters, 1):
            if aCombination[k] == tpl_iCharacter[i]:
                tmp_sum = tmp_sum + tpl_iCharAvrgWidth[i]

    if tmp_sum == (Width_RedactedText - (2 * tpl_iCharAvrgWidth[52])) and str_Combination.count("_") == 0:
        Lst_PossibleAnswers.append(str_Combination)
        print("> Adding " + str_Combination + " to Lst_PossibleAnswers with a value of " + str(tmp_sum) + ")")
    elif tmp_sum == (Width_RedactedText - (2 * tpl_iCharAvrgWidth[52])) and str_Combination.count("_") > 0:
        Lst_Rejections.append(str_Combination)
        print("> Adding " + str_Combination + " to Lst_Rejections with " + str(str_Combination.count("_")) + " spaces")
    elif tmp_sum != (Width_RedactedText - (2 * tpl_iCharAvrgWidth[52])):
        print("> Rejecting " + str_Combination + " with a non-matching value of " + str(tmp_sum))
    else:
        print("> Error for string " + str_Combination + "with a non-matching value of" + str(tmp_sum))

print("===============================================================================")
print("")

#End
#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#Split Lst_Rejections items by space, then run against dictionary again

print("")
print("Splitting Lst_Rejection items")
print("===============================================================================")

Lst_tempstring = []
Lst_Rejections_LengthOf = int(len(Lst_Rejections))
count = 0

if Lst_Rejections_LengthOf > 0:
    for i in range(0, Lst_Rejections_LengthOf, 1): #for i from 0 to UpperBound(Lst_Rejections)
        if (str(Lst_Rejections[i])).count("_") > 0: #if Lst_Rejections[i] contains spaces
            Lst_tempstring = str(Lst_Rejections[i]).split("_") #split Lst_Rejections[i] by space and add to temp list
            Lst_tempstring_LengthOf = int(len(Lst_tempstring))
            for k in range(0, Lst_PossibleAnswers_LengthOf, 1): #for k from 0 to UpperBound(Lst_PossibleAnswers)
                count = 0
                for j in range(0, Lst_DictionarySearch_LengthOf, 1): #for j from 0 to UpperBound(Lst_DictionarySearch)
                    if str(Lst_PossibleAnswers[k]) == str(Lst_DictionarySearch[j]): #if Lst_PossibleAnswers[k] == Lst_DictionarySearch[j]
                        count = count + 1
                        exit
                if count > (Lst_tempstring_LengthOf - 1):
                    Lst_PossibleAnswers2.append(str(Lst_PossibleAnswers[k]))
                    print("> Adding " + str(Lst_PossibleAnswers[k]) + " to Lst_PossibleAnswers")
                elif count < Lst_tempstring_LengthOf:
                    print("> Rejecting " + str_Combination)
                else:
                    print("> String error. Function returned an error for string " + (str(Lst_PossibleAnswers[k])))
else:
    print("> No items!")

print("===============================================================================")
print("")

#End
#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#Check items from Lst_PossibleAnswers against dictionary

Lst_PossibleAnswers_LengthOf = int(len(Lst_PossibleAnswers))

if Lst_PossibleAnswers_LengthOf > 0:
    for i in range(0, Lst_PossibleAnswers_LengthOf, 1):
        count = 0
        for k in range(0, Lst_DictionarySearch_LengthOf, 1):
            if (str(Lst_PossibleAnswers[i])).lcase == (str(Lst_DictionarySearch[k])).lcase: #DO I NEED TO MAKE THE SEARCH STRING AND THE DICTIONARY TUPLE ALL LOWER CASE?
                count = count + 1
        if count > 0:
            Lst_PossibleAnswers2.append(str(Lst_PossibleAnswers[i]))
            print("> Adding " + str(Lst_PossibleAnswers[i]) + " to Lst_PossibleAnswers2")
        elif count == 0:
            print("> " + str(Lst_PossibleAnswers[i]) + " rejected.")
        else:
            print("> String error. Function returned an error for string " + (str(Lst_PossibleAnswers[i])))
elif Lst_PossibleAnswers_LengthOf == 0:
    print("> No items!")

#End
#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

print("")
print("===============================================================================")
print("Items in array Lst_PossibleAnswers2:")
print("")

Lst_PossibleAnswers2_LengthOf = int(len(Lst_PossibleAnswers2))
if Lst_PossibleAnswers2_LengthOf == 0:
    print("> No items!")
elif Lst_PossibleAnswers2_LengthOf != 0:
    for i in range(0, Lst_PossibleAnswers2_LengthOf, 1):
        print("> String " + str(i) + ": " + Lst_PossibleAnswers2[i])
