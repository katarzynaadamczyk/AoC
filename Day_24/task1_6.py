# Katarzyna Adamczyk
# Solution to day 24 task 1 of Advent of Code 2021


surelywrongsn = {} # level: z
digitsmaxtolow = [9, 8, 7, 6, 5, 4, 3, 2, 1]
digitslowtomax = [1, 2, 3, 4, 5, 6, 7, 8, 9]

divz = [1,      1,      1,      26,     1,      26,     1,      26,     26,     26,     1,      1,      26,     26]
addx = [12,     11,     12,     -3,     10,     -9,     10,     -7,     -11,    -4,     14,     11,     -8,     -10]
addy = [7,      15,     2,      15,     14,     2,      15,     1,      15,     15,     12,     2,      13,     13]


def findserialnumber(level, modelnumber, z, digits):
    if (level in surelywrongsn and surelywrongsn[level] == z) or level == 14:
        return None
    
    modelnumber *= 10
    originalz = z
    
    for digit in range(len(digits)):
        z = originalz
        x = z % 26 + addx[level]
        z //= divz[level]
        x = 1 if x == digits[digit] else 0
        x = 1 if x == 0 else 0
        y = 25 * x + 1
        z *= y
        y = digits[digit] + addy[level]
        y *= x
        z += y
    
        if z == 0 and level == 13:
            return modelnumber + digits[digit];
        newresult = findserialnumber(level + 1, modelnumber + digits[digit], z, digits);
        if newresult is not None:
            return newresult;
        
    surelywrongsn[level] = originalz
    return None
    

def solution1(filename):
    
    return findserialnumber(0, 0, 0, digitsmaxtolow)




def main():
    print(f'Result for data24 for task 1 is {solution1("Day_24/data24.txt")}')
    

if __name__ == '__main__':
    main()