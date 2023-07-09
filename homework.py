import re
# Exercise #1
# Print each persons name and twitter handle, using groups, should look like:
# txt = "Hawkins, Derek,Johnson, Joe, Zhai, Mo, Butz, Ryan"
pattern = re.compile('([A-Z][a-z]+), ([A-Z][a-z]+)')
pattern1 = re.compile('([A-Z][a-z]+), ([A-Z][a-z]+)-([A-Z][a-z]+)')
# find_txt = pattern.findall(txt)
# print(find_txt)
# pattern = re.compile('@([a-za-za-z]+)$')
with open('names.txt') as f:
    data = f.readlines()
    for d in data:
        # print(d)
        match = pattern.search(d)
        # print(match)
        match1 = pattern1.findall(d)
        # print(match1)
        if match:
            print(f'full names {match.group(2)} {match.group(1)}')
        
        else:
            print('not a full name')
        if match1:
            print(f'full names  {match1}')
        


print('________TWitter______@')
pattern1 = re.compile('@([a-za-za-z]+)$')
with open('names.txt') as f:
    data = f.readlines()
    for d in data:
    # print(d)
        match = pattern1.findall(d)
        if match:
            print(match)

# find_name = pattern.findall(f.readlines())
# print(find_name)

pattern3 = re.compile('([A-Z][a-z]+) ([A-Z][a-z]+)')
pattern4 = re.compile('([A-Z][a-z]+) ([A-Z]) ([A-Z][a-z]+)')
with open('regex_test.txt') as f:
    data = f.readlines()
    for d in data:
        match3 = pattern3.search(d)
        match4 = pattern4.search(d)
        # print(match3)
        if match3:
            print(f'full names: {match3.group()}')
        else:
            print('None')
        if match4:
            print(f'full names: {match4.group()}')