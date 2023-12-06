from pathlib import Path
from bitstring import ConstBitStream, pack

def read_packet():
    global bs, version_sum
    version = bs.read('uint:3')
    type = bs.read('uint:3')
    version_sum += version
    #print ("Version: ", version)
    #print ("Type: ", type)

    if type == 4:
        return read_literal()
    else:
        packet_values = read_operator()
        if type == 0:
            return sum(packet_values)
        elif type == 1:
            product = 1
            for val in packet_values:
                product *= val
            return product
        elif type == 2:
            return min(packet_values)
        elif type == 3:
            return max(packet_values)
        elif type == 5:
            return 1 if packet_values[0] > packet_values[1] else 0
        elif type == 6:
            return 1 if packet_values[0] < packet_values[1] else 0
        elif type == 7:
            return 1 if packet_values[0] == packet_values[1] else 0
        

def read_literal():
    global bs
    keepReading = bs.read('bool')
    bits = bs.read('bin:4')
    while keepReading:
        keepReading = bs.read('bool')
        bits += bs.read('bin:4')
    return ConstBitStream('0b' + bits).read('uint:'+str(len(bits)))

def read_operator():
    global bs
    lengthTypeId = bs.read('bool')
    packet_values = []
    if lengthTypeId:
        subPacketCount = bs.read('uint:11')
        for packet in range(subPacketCount):
            packet_values.append(read_packet())
    else:
        packetLengthBits = bs.read('uint:15')
        startingPos = bs.pos
        while (bs.pos - startingPos) < packetLengthBits:
            packet_values.append(read_packet())
    return packet_values


path = Path(__file__).parent / "aoc-day16-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

version_sum = 0

bs = ConstBitStream('0x' + input_array[0].strip(" \r\n"))
#bs = ConstBitStream('0x9C0141080250320F1802104A08')

print(read_packet())
#print (version_sum)

