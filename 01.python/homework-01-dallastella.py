# Marco Dalla Stella
# 2023-06-06
# Homework 1

# Instructions
# Inspired by the BBC's "Your life on earth"Links to an external site.  (which I have watched hilariously decompose since it was created), we will be creating a program to analyze the year a user was born in.

# Please create a brand new file named homework-01-lastname.py

# The first line should be a comment with your full name
# The second line should be a comment with the date
# The third line should be a comment "Homework 1"
# When run from the command line, this file should prompt the user for their year of birth, and print out (approximately):

# How old the user is
# How many times the user's heart has beaten
# How many times a blue whale's heart has beaten in that time
# How many times a rabbit's heart has beaten in that time
# If the answer to rabbit heartbeats is more than a million, say "XXX million" instead of the very long raw number
# How old they are in Venus years
# How old they are in Neptune years
# Whether they are the same age as you, older or younger
#  If older or younger, how many years difference
#  If they were born in an even or odd year
# How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once)
# Which US President was in office when they were born (1960 onward)
# If someone says they were born in the future, try asking them again (assume they'll do it right the second time).




# As a first thing, I will set up the input and store it in the year variable.
# I will also make sure that if the person is born in the future, I'll ask them one more time.

year = int(input("What year were your born?"))
if year >= 2023:
    year = int(input("Hail, main of the future! No, really, what year were you born?"))

# Now I want to save some variables so that I won't have to digit all that horrible math again.

age = 2023-year
whale = (((33*60)*24)*365)*age
rabbit = ((8000*24)*365)*age

# Now I should be able to answer a few questions.
# To make big numbers more readable, I've found on the internet that I can use '"{:,}".format'.


print("You are",age,"years old.")
print("Your heart has beaten about","{:,}".format((100000*365)*age),"times so far.")
print("Over the same period of time, a whale's heart beats","{:,}".format(whale),"times.")
if rabbit >= 1000000:
    print("If a rabbit was your age, its heart would have beaten",int(str(rabbit)[0]),"million times.")
else:
    print("If a rabbit was your age, its heart would have beaten","{:,}".format(rabbit),"times.")
if age > 12:
    print("But that's unlikely, because rabbits can't live more than 12 years, while you are",age,"years old. That means that the rabbit that was born in your same year, is long dead!")
print("In Venus years, you would be",int(round((age/365)*225,0)),"years old.")
print("In Neptune years, you would be",int(round((age/365)*165,0)),"years old.")

if age > 35:
    print("You are",age-35,"older than me!")
elif age == 35:
    print("Cool, we are the same age!")
else:
    print("You are",35-age,"years younger than me.")

if year % 2 == 0 :
    print("I can see that you were born in an even year.")
else:
    print("I can see that you were born in an odd year.")

# For the presidents-related questions, I should use a list.
# This list should include the years where Democratic Presidents got elected since 1960.

dems = [1961,1963,1977,1992,2008,2020]
count = 0
for dem in dems:
    if year <= dem:
        count = count + 1
print("You have lived through",count,"Democratic Presidents")

# For the last one, I think I need a dictionary to match every year with the corresponding President.
# To do the dictionary, I first did it on Excel and then pasted it here.

presidents = {
    1960:	"Dwight D. Eisenhower",
1961:	"John F. Kennedy",
1962:	"John F. Kennedy",
1963:	"John F. Kennedy",
1964:	"Lyndon B. Johnson",
1965:	"Lyndon B. Johnson",
1966:	"Lyndon B. Johnson",
1967:	"Lyndon B. Johnson",
1968:	"Lyndon B. Johnson",
1969:	"Richard Nixon",
1970:	"Richard Nixon",
1971:	"Richard Nixon",
1972:	"Richard Nixon",
1973:	"Richard Nixon",
1974:	"Gerald Ford",
1975:	"Gerald Ford",
1976:	"Gerald Ford",
1977:	"Jimmy Carter",
1978:	"Jimmy Carter",
1979:	"Jimmy Carter",
1980:	"Jimmy Carter",
1981:	"Ronald Reagan",
1982:	"Ronald Reagan",
1983:	"Ronald Reagan",
1984:	"Ronald Reagan",
1985:	"Ronald Reagan",
1986:	"Ronald Reagan",
1987:	"Ronald Reagan",
1988:	"Ronald Reagan",
1989:	"George H. W. Bush",
1990:	"George H. W. Bush",
1991:	"George H. W. Bush",
1992:	"George H. W. Bush",
1993:	"Bill Clinton",
1994:	"Bill Clinton",
1995:	"Bill Clinton",
1996:	"Bill Clinton",
1997:	"Bill Clinton",
1998:	"Bill Clinton",
1999:	"Bill Clinton",
2000:	"Bill Clinton",
2001:	"George W. Bush",
2002:	"George W. Bush",
2003:	"George W. Bush",
2004:	"George W. Bush",
2005:	"George W. Bush",
2006:	"George W. Bush",
2007:	"George W. Bush",
2008:	"George W. Bush",
2009:	"Barack Obama",
2010:	"Barack Obama",
2011:	"Barack Obama",
2012:	"Barack Obama",
2013:	"Barack Obama",
2014:	"Barack Obama",
2015:	"Barack Obama",
2016:	"Barack Obama",
2017:	"Donald Trump",
2018:	"Donald Trump",
2019:	"Donald Trump",
2020:	"Donald Trump",
2021:	"Joe Biden",
2022:	"Joe Biden",
2023:	"Joe Biden"
}

if year in presidents:
    president = presidents[year]
    print ("The president in",year,"was",president,"!")
else:
    print("I cannot find who was the President in",year,"!")
