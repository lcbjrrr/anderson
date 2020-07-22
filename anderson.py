"Hello"
name = "Anderson"
print(type(name))
message = ' Anderson said to me "I will see you later "'

hello = "hello, world"
print(hello)

# Ask user for name
name = input("What's your name?:")
# Ask user for age
age = input("How old are you?:")

# Ask user for city
city = input("What city do you live in?:")
# Ask user what they enjoy
love = input("What do you love doing?:")
# Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love )
# Print output to screen
print(output)





def nome_completo(n,s):
    n_c = n + ' ' +s
    return(n_c)

nome = 'luiz'
sobrenome = 'barboza'

luiz= nome_completo(nome,sobrenome)
print(luiz)


#PythonEstruturadeDados

our_list = [98, 12, 20, 13, 5]
print(our_list)
type(our_list)

Anderson = [16,17,18,19, "A", "B", "C", "9", False, True ]
Anderson[2]
