#1. + concatenate
#2. , commas
#3. f formatted string
#4. % substitutions
#5. using the Template module

user = "Kevin"

print("1. Hello "+user)
print("2. Hello",user)
print(f"3. Hello {user}")
print("4. Hello %s" % user)
from string import Template
template = Template('5. Hello $name')
print(template.substitute(name = user))
