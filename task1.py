name=input("What's your name? \n")
age=int(input("your age?\n"))
city=input("where do you live?\n")
uv=input("your college?\n")
dept=input("what's your department?\n")
fav=input("Favorite programming language?\n")
goal=input("your programming goal?\njoh")

result=f"""Student Introduction
my name is {name}.
I am {age} years old. 
I live in {city}. 
I study {dept} at {uv} University.
My favorite programming language is {fav}.
My programming goal:\n Become a {goal}."""
print(result)