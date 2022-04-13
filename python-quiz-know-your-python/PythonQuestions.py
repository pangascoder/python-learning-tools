questions_list = [
{
    "question": "Who developed Python Programming Language?",
    "choices": """
    (a) Wick van Rossum
    (b) Rasmus Lerdorf
    (c) Guido van Rossum
    (d) Niene Stom""",
    "answer": "c",
    "feedback": "Python language is designed by a Dutch programmer Guido van Rossum in the Netherlands."
},
{
    "question": "Which type of programming does Python support?",
    "choices": """
    (a) object-oriented programming
    (b) structured programming
    (c) functional programming
    (d) all of the mentioned""",
    "answer": "d",
    "feedback": "Python is an interpreted programming language, which supports object-oriented, structured, and functional programming."
},
{
    "question": "Which of the following is the correct extension of the Python file?",
    "choices": """
    (a) .python 
    (b) .pl 
    (c) .py 
    (d) .p""",
    "answer": "c",
    "feedback": "‘.py’ is the correct extension of the Python file. Python programs can be written in any text editor. To save these programs we need to save in files with file extension ‘.py’."
},
{
    "question": "All keywords in Python are in ____",
    "choices": """
    (a) Capitalized 
    (b) lower case 
    (c) UPPER CASE 
    (d) None of the mentioned""",
    "answer": "d",
    "feedback": "True, False and None are capitalized while the others are in lower case."
},
{
    "question": "Which of the following is used to define a block of code in Python language?",
    "choices": """
    (a) Indentation 
    (b) Key 
    (c) Brackets 
    (d) All of the mentioned""",
    "answer": "a",
    "feedback": "In Python, to define a block of code we use indentation. Indentation refers to whitespaces at the beginning of the line."
},
{
    "question": "Which keyword is used for function in Python language?",
    "choices": """
    (a) function 
    (b) def 
    (c) fun 
    (d) define""",
    "answer": "b",
    "feedback": "Def stands for 'defining' a function."
},
{
    "question": "Which of the following character is used to give single-line comments in Python?",
    "choices": """
    (a) // 
    (b) # 
    (c) ! 
    (d) /*""",
    "answer": "b",
    "feedback": "To write single-line comments in Python use the Numero sign (#) at the beginning of the line. To write multi-line comments, close the text between triple quotes."
},
{
    "question": "Which of the following is true for variable names in Python?",
    "choices": """
    (a) underscore and ampersand are the only two special characters allowed 
    (b) unlimited length 
    (c) all private members must have leading and trailing underscores 
    (d) none of the mentioned""",
    "answer": "b",
    "feedback": "Variable names can be of any length."
},
{
    "question": "Which of the following functions is a built-in function in Python?",
    "choices": """
    (a) factorial() 
    (b) print() 
    (c) seed() 
    (d) sqrt()""",
    "answer": "b",
    "feedback": "The function seed is a function which is present in the random module. The functions sqrt and factorial are a part of the math module. The print function is a built-in function which prints a value directly to the system output."
},
{
    "question": "What arithmetic operators cannot be used with strings in Python?",
    "choices": """
    (a) * 
    (b) - 
    (c) + 
    (d) All of the above""",
    "answer": "b",
    "feedback": "+ is used to concatenate and * is used to multiply strings."
},
{
    "question": """What will be the value of the following Python expression?

    4 + 3 % 5
    """,
    "choices": """
    (a) 7 
    (b) 2 
    (c) 4 
    (d) 1""",
    "answer": "a",
    "feedback": "The order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7."
},
{
    "question": """What will be the output of the following Python code?

    i = 1
    while True:
        if i%3 == 0:
            break
        print(i)
    
        i + = 1
    """,
    "choices": """
    (a) 1 2 3
    (b) Error 
    (c) 1 2 
    (d) none of the mentioned""",
    "answer": "b",
    "feedback": "This will throw a SyntaxError because there shouldn’t be a space between + and =. It should be i += 1."
},
{
    "question": "What is the order of precedence in python?",
    "choices": """
    (a) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction
    (b) Exponential, Parentheses, Division, Multiplication, Addition, Subtraction
    (c) Parentheses, Exponential, Multiplication, Division, Subtraction, Addition
    (d) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction""",
    "answer": "d",
    "feedback": "For order of precedence, just remember this PEMDAS (similar to BODMAS)."
},
{
    "question": "Which of the following is not a core data type in Python programming?",
    "choices": """
    (a) Tuples
    (b) Lists
    (c) Class
    (d) Dictionary""",
    "answer": "c",
    "feedback": "Class is a user-defined data type."
},
{    "question": """What will be the output of the following Python function?

    len(["hello",2, 4, 6])
    """,
    "choices": """
    (a) Error
    (b) 6
    (c) 4
    (d) 3""",
    "answer": "c",
    "feedback": "The function len() returns the length of the number of elements in the iterable. Therefore the output of the function shown above is 4."
},
{    "question": """What will be the output of the following Python code?

    x = 'abcd'
    for i in x:
        print(i.upper())
    """,
    "choices": """
    (a) a B C D
    (b) a b c d
    (c) A B C D
    (d) Error""",
    "answer": "c",
    "feedback": "The instance of the string returned by upper() is being printed."
},
{    "question": """What will be the output of the following Python code?

    print("abc. DEF".capitalize())
    """,
    "choices": """
    (a) Abc. def
    (b) abc. def
    (c) Abc. Def
    (d) ABC. DEF""",
    "answer": "a",
    "feedback": "With capitalize(), the first letter of the string is converted to uppercase and the others are converted to lowercase."
},
{    "question": "To add a new element to a list we use which Python command?",
    "choices": """
    (a) my_list.addEnd(5)
    (b) my_list.addLast(5)
    (c) my_list.append(5)
    (d) my_list.add(5)""",
    "answer": "c",
    "feedback": "We use the function append to add an element to the list."
},
{    "question": "Which of the following is a Python tuple?",
    "choices": """
    (a) {1, 2, 3}
    (b) {}
    (c) [1, 2, 3]
    (d) (1, 2, 3)""",
    "answer": "d",
    "feedback": "Tuples are represented with round brackets."
},
{    "question": """What will be the output of the following Python code?
    print("Hello {0[0]} and {0[1]}".format(('foo', 'bin')))
    """,
    "choices": """
    (a) Hello (‘foo’, ‘bin’) and (‘foo’, ‘bin’)
    (b) Hello foo and bin
    (c) Error
    (d) None of the mentioned""",
    "answer": "b",
    "feedback": "The elements of the tuple are accessed by their indices."
},
{    "question": "Why are local variable names beginning with an underscore discouraged?",
    "choices": """
    (a) They are used to indicate a private variables of a class.
    (b) They confuse the interpreter.
    (c) They are used to indicate global variables.
    (d) They slow down execution""",
    "answer": "a",
    "feedback": "As Python has no concept of private variables, leading underscores are used to indicate variables that must not be accessed from outside the class."
},
{    "question": "Which of the following is an invalid statement?",
    "choices": """
    (a) abc = 1,000,000
    (b) a b c = 1000 2000 3000
    (c) a,b,c = 1000, 2000, 3000
    (d) a_b_c = 1,000,000""",
    "answer": "b",
    "feedback": "Spaces are not allowed in variable names."
},
{    "question": """What error occurs when you execute the following Python code snippet?
    apple = mango
    """,
    "choices": """
    (a) SyntaxError
    (b) NameError
    (c) ValueError
    (d) TypeError""",
    "answer": "b",
    "feedback": "The mango variable is not defined hence the name error."
},
{    "question": """What will be the output of the following Python code?
    print(0xA + 0xB + 0xC)
    """,
    "choices": """
    (a) 0xA0xB0xC
    (b) 0x22
    (c) 33
    (d) Error""",
    "answer": "c",
    "feedback": " 0xA and 0xB and 0xC are hexadecimal integer literals representing the decimal values 10, 11 and 12 respectively. There sum is 33."
},
{    "question": """What will be the output of the following Python code snippet?
    print('Ab!2'.swapcase())
    """,
    "choices": """
    (a) AB!@
    (b) ab12
    (c) aB!2
    (d) aB1@""",
    "answer": "c",
    "feedback": "Lowercase letters are converted to uppercase and vice-versa."
},
]