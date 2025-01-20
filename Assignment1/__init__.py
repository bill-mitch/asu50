import check50

@check50.check()
def exists():
    """Assignment1.py Exists"""
    check50.exists("assignment1.py")
    
@check50.check(exists)
def question1():
    """Q1 Output Validation"""
    expected = "Hello\n*****\nWorld"
    output = check50.run("python3 assignment1.py").stdout()

    if expected not in output:
        raise check50.Failure("Expected output not found. Check your formatting!")
    
@check50.check(exists)
def question2():
    """Q2 Output Validation"""
    expected = "Hello\n     *****\n          World"
    output = check50.run("python3 assignment1.py").stdout()

    if expected not in output:
        raise check50.Failure("Expected output not found. Check your formatting!")

@check50.check(exists)
def question3():
    """Q3 Output Validation"""
    expected = "\n50\n"
    output = check50.run("python3 assignment1.py").stdout()

    if expected not in output:
        raise check50.Failure("Expected output not found. Check your formatting!")

@check50.check(exists)
def question4():
    """Q4 Output Validation"""
    expected = "\nHello World\n"
    output = check50.run("python3 assignment1.py").stdout()

    if expected not in output:
        raise check50.Failure("Expected output not found. Check your formatting!")
    
@check50.check(exists)
def question5():
    """Q5 Output Validation"""
    expected = "\n10.0\n"
    output = check50.run("python3 assignment1.py").stdout()

    if expected not in output:
        raise check50.Failure("Expected output not found. Check your formatting!")
    
@check50.check(exists)
def question6():
    """Q6 Output Validation"""
    expected = "\nThe earth is round!\n"
    output = check50.run("python3 assignment1.py").stdout()

    if expected not in output:
        raise check50.Failure("Expected output not found. Check your formatting!")