from pathlib import Path

def findTopSegment(signal1, signal7):
    for c in signal7:
        if signal1.find(c) == -1:
            return c
    return ''

def findSegmentsCandF(signals, signal1):
    for signal in signals:
        if len(signal) == 6:
            if signal.find(signal1[0]) == -1:
                return signal1[0], signal1[1], signal
            elif signal.find(signal1[1]) == -1:
                return signal1[1], signal1[0], signal
    return ''

def allCharsExist(search, chars):
    for c in chars:
        if search.find(c) == -1:
            return False
    return True

def Diff(l1, l2):
    return list(set(l1) - set(l2))

def SignalsAreSame(s1, s2):
    return len(Diff(s1, s2)) == 0 and len(Diff(s2, s1)) == 0

def find9(signals, signal4, signal8):
    for signal in signals:
        if len(signal) == 6 and allCharsExist(signal, signal4):
            return Diff(signal8, signal)[0], signal

def find0(signals):
    for signal in signals:
        if len(signal) == 6 and signal != signal9 and signal != signal6:
            return Diff(signal8, signal)[0], signal

def findSegmentB(signals):
    return Diff(signal4, [segD, segC, segF])[0]

def findSignal(signals, segmentsForSignal):
    for signal in signals:
        if SignalsAreSame(signal, segmentsForSignal):
            return signal
    return ''

path = Path(__file__).parent / "aoc-day8-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

sum = 0

for line in input_array:
    signal_patterns, output_digits = line.split('|', 1)
    signals = signal_patterns.strip().split(" ")

    for signal in signals:
        l = len(signal)
        if l == 2:
            signal1 = signal
        elif l == 3:
            signal7 = signal
        elif l == 4:
            signal4 = signal
        elif l == 7:
            signal8 = signal

    # Find 7 and 1 to determine top segment (a)
    segA = findTopSegment(signal1, signal7)

    # Find 6 (6 segments that has only c or f from above), this will determine segments c & f's mapping
    segC, segF, signal6 = findSegmentsCandF(signals, signal1)

    # Find the 9 (6 segments illuminated that shares all 4 segments from the '4').  This shows us e's mapping
    segE, signal9 = find9(signals, signal4, signal8)

    # Find the 0 (6 segments illuminated that we haven't identified yet).  This shows us d's mapping
    segD, signal0 = find0(signals)

    # Now we can determine b's mapping
    segB = findSegmentB(signals)

    # g is the only one left
    segG = Diff(signal8, [segA, segB, segC, segD, segE, segF])[0]

    signal2 = findSignal(signals, [segA, segC, segD, segE, segG])
    signal3 = findSignal(signals, [segA, segC, segD, segF, segG])
    signal5 = findSignal(signals, [segA, segB, segD, segF, segG])

    #print ("segA is " + segA)
    #print ("segB is " + segB)
    #print ("segC is " + segC)
    #print ("segD is " + segD)
    #print ("segE is " + segE)
    #print ("segF is " + segF)
    #print ("segG is " + segG)
    #print ("0 is " + signal0)
    #print ("1 is " + signal1)
    #print ("2 is " + signal2)
    #print ("3 is " + signal3)
    #print ("4 is " + signal4)
    #print ("5 is " + signal5)
    #print ("6 is " + signal6)
    #print ("7 is " + signal7)
    #print ("8 is " + signal8)
    #print ("9 is " + signal9)

    output = output_digits.strip().split(' ')
    number = ""
    for digit in output:
        if SignalsAreSame(digit, signal0):
            number += "0"
        elif SignalsAreSame(digit, signal1):
            number += "1"
        elif SignalsAreSame(digit, signal2):
            number += "2"
        elif SignalsAreSame(digit, signal3):
            number += "3"
        elif SignalsAreSame(digit, signal4):
            number += "4"
        elif SignalsAreSame(digit, signal5):
            number += "5"
        elif SignalsAreSame(digit, signal6):
            number += "6"
        elif SignalsAreSame(digit, signal7):
            number += "7"
        elif SignalsAreSame(digit, signal8):
            number += "8"
        elif SignalsAreSame(digit, signal9):
            number += "9"
        else:
            print ("What is " + digit)
            exit()
    sum += int(number)
print (sum)