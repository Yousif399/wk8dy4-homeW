import re 

pattern = re.compile('abcd')
# re.match()
match = pattern.match('abcdefg12345')
# print(match)
# print(match.span())
# re.search
search = pattern.search('1234abcdefg12345')
print(search)
print(search.span())

# findal

finder = pattern.findall('abcd 123456abcd')
print(finder)

# set
pat_int = re.compile('[7-9][0-5][0-5][0-5]')
num = pat_int.search('7988979751509780989789515')
print(num)
num2 = pat_int.findall('79889797515097809897895152113215151')
print(num2)

# character  ranges
character = re.compile('[A-Z][a-z]')
finder = character.findall('Hello Mr jo Joseph How Are you')
print(finder)


# character count 
character_count = re.compile('[A-Z][a-z][0-9]{4,6}')
finder2 = character_count.findall('He333llo Wo6666rld EAr8123th ')

print(finder2)

char = re.compile('Mrs?')
finder3 = char.findall('Mrrrr.joseph got married to Mrs.joseph mMs.alex')
print(finder3)

char1 = re.compile('Ms*')
finder4 = char.findall('Mrrrr.joseph got married to Mrs.joseph mMs.alex Mr. Mrs. Ms Mx.')
print(finder4)

char2 = re.compile('Ms+ ')
finder5 = char.findall('Mrrrr.joseph got married to Mrs.joseph mMs.alex Mr. Mrs. Ms Mx.')
print(finder5)

my_string = "This string has 10909090 numbers, but it is only 1 string. I hope you solve this 2day!"

numbers = re.compile('[0-9]+')
find_numbers = numbers.findall(my_string)
print(find_numbers)


# Escaping charcter
my_string1 = "Thi's string it's has 10909090 numbers, but it is only 1 string. I hope you solve this 2day!"

p1 = re.compile('[\w]+')
p2 = re.compile('[\W]+')
f1 = p1.findall(my_string1) 
f2 = p2.findall(my_string1) 
print(f1)
print(f2)

my_string3 = "This string has 10909090 numbers, but it is only 1 string. I hope you solve this 2day!"

numbers1 = re.compile('[\d]+')
numbers2 = re.compile('[\D]+')
find_numbers1 = numbers1.findall(my_string3)
find_numbers2 = numbers2.findall(my_string3)
print(find_numbers1)
print(find_numbers2)

print('\n')
p3 = re.compile('[\s]+')
p4 = re.compile('[\S]+')
f3 = p3.findall(my_string1) 
f4 = p4.findall(my_string1) 
print(f3)
print(f4)

pattern_b= re.compile(r'\bCoding Temple\b')
p_np_b = re.compile(r'\BCoding Temple\B')
b = pattern_b.findall(' Coding Temple')
no_b = p_np_b.findall('CodingTemple')
print(b)
print(no_b)



# ______________

my_string_again = "Max Smith, aaron rodgers, Sam Darnold,LeBron James, Micheal Jordan, Kevin Durant, Patrick McCormick"

pat_name = re.compile('([A-Z][a-zA-Z[a-z]+) ([A-Z][a-zA-Za-z]+)')
find_names = pat_name.findall(my_string_again)
print(find_names)

for name in my_string_again.split(','):
    match = pat_name.search(name)
    print(match)
    if match:
        print(f' hereeee {match.group()}')
        print(f' 1 {match.group(1)}')
        print(f' 2   {match.group(2)}')
    else:
        print('none')



# pat_name = re.compile('(?P<f>[A-Z][a-zA-Z[a-z]+) (?P<l>[A-Z][a-zA-Za-z]+)')
# find_names = pat_name.findall(my_string_again)

# for name in my_string_again.split(','):
#     match = pat_name.search(name)
#     print(match)
#     if match:
#         print(f'hereeee {match.group("f")} {match.group("l")}')
#     else:
#         print('none') 


my_emails = ["shohat@codingcodingsummit.orgcom", "pocohontas1776@gmail.com", "helloworld@aol..com","yourfavoriteband@g6.org", "@codingsummit.com"]

# email_pat = re.compile('([a-Za-z0-9]+)@([A-Za-z0-9]+).(com|org)$')

f = open("names.txt")
print(f)
data = f.read()
print(data)
f.close()


# /with open
with open('names.txt') as f:
    data = f.read()
    print(data)

# read lines
with open('names.txt') as f:
    # data2 = f.readline(1-100)
    data2 = f.readlines()
    print(data2)


# re.math()
# pattern4 = re.compile('[a-z0-9]{2}')
# pattern4 = re.match('[a-z0-9]{2}', 'string' ) bad for time complex


# search()
# print(re.search(r'[a-z0-9]{2}', 'Hawkins'))

