import re

eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

with open('/Users/matt/Projects/Advent of Code/2020/aoc-day4-input.txt') as my_file:
    batch_file = my_file.readlines()

entry = ""
valid = 0
for line in batch_file:
    if line.strip() == "":
        #print(entry)
        # Process entry
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        for field in entry.split():
            #print (field)
            fieldType, fieldValue = field.split(':')
            intValue = 0
            try:
                intValue = int(fieldValue)
            except ValueError:
                intValue = 0
            #print(fieldType)
            if fieldType == "byr" and intValue >= 1920 and intValue <= 2002:
                byr = True
            elif fieldType == "iyr" and intValue >= 2010 and intValue <= 2020:
                iyr = True
            elif fieldType == "eyr" and intValue >= 2020 and intValue <= 2030:
                eyr = True
            elif fieldType == "hgt":
                units = fieldValue[-2:]
                num = 0
                try:
                    num = int(fieldValue[0:len(fieldValue)-2])
                except ValueError:
                    num = 0
                if units == "cm" and num >= 150 and num <=193:
                    hgt = True
                elif units == "in" and num >= 59 and num <= 76:
                    hgt = True
            elif fieldType == "hcl":
                if re.fullmatch('#[0-9a-f]{6}', fieldValue) != None:
                    hcl = True
            elif fieldType == "ecl":
                for color in eyeColors:
                    if color == fieldValue:
                        ecl = True
            elif fieldType == "pid":
                if re.fullmatch('\d{9}', fieldValue) != None:
                    pid = True
        
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valid += 1
            #print ("Valid")

        entry = ""
        #print()
        #print()
        #exit(1)

    else:
        # Add to entry
        entry += line

print (valid)