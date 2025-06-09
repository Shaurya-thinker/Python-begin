import sys
# print("Name of the program is:", sys.argv[0])
# print("Argument List:", str(sys.argv))
# print(len(sys.argv))

""" x = int(sys.argv[1])
y = int(sys.argv[2])
sum = x+y
print("The sum is: ", sum)

z = int(sys.argv[3])
mul = x*y*z
print(mul)
 """

""" def function1():
    print("First function")

def function2():
    print("Second function")

arguments = sys.argv[1:]

if len(arguments) != 1:
    print(f'ERROR: 1 argument expected, {len(arguments)} given!')
    sys.exit()

arguments = arguments[0]

if arguments == "f" or arguments == "first":
    function1()
elif arguments == "s" or arguments == "second":
    function2()
else:
    print(f'ERROR: {arguments} not available!') """



""" def function1(file):
    print("First function")
    print(file)

def function2(file):
    print("Second function")
    print(file)

arguments = sys.argv[1:]

if len(arguments) != 2:
    print(f'ERROR: 2 arguments expected, {len(arguments)} given!')
    sys.exit()

option = arguments[0]
filename = arguments[1]

if option == 'f':
    function1(filename)
elif option == 's':
    function2(filename)
else:
    print('ERROR: option not available') """


""" def function1():
    print("First function")

def function2():
    print("Second function")

arguments = sys.argv[1:]

if len(arguments) < 1:
    print(f'ERROR: at least 1 arguments expected, {len(arguments)} given!')
    sys.exit()

for arg in arguments:
    if arg not in ('f', 's'):
        print(f'ERROR, {arg} is wrong option')
        sys.exit()
    elif arg == 'f':
        function1()
    elif arg == 's':
        function2() """



""" def function1(file):
    print("-f")

def function2(file):
    print("-s")

def function3(file):
    print("only filename")

try:
    filename = sys.argv[1]
except IndexError:
    print('ERROR: filename expected!')
    sys.exit()

options = sys.argv[2:]

if options:
    for option in options:
        if option not in('-f', '--first', '-s', '--second'):
            print(f'ERROR: {option} not available')
            sys.exit()
    for option in options:
        if option == '-f' or option == '--first':
            function1(filename)
        elif option == '-s' or option == '--second':
            function2(filename)

else:
    function3(filename) """



""" def function1(file):
    print("-f")

def function2(file):
    print("-s")

def function3(file):
    print("only filename")

try:
    filename = sys.argv[1]
except IndexError:
    print('ERROR: filename expected!')
    sys.exit()

options = sys.argv[2:]
if options:
    for option in options:
        if option not in('-f', '--first', '-s', '--second'):
            print(f'ERROR: {option} not available')
            sys.exit()
    
    if('-f' in options or '--first' in options) and ('-s' in options or '--second' in options):
        function1(filename)
    elif '-f' in options or '--first' in options:
        function2(filename)
    elif ('-s' in options or '--second' in options) and not ('-f' in options or '--first' in options):
        print(f'ERROR: {options} cannot be used without -f/--first')
        sys.exit()

else:
    function3(filename) """



