from olympics.__main__ import main
import pytest
import argparse


######### TESTING COMMAND ###########

# Testing command with top=number | top=10 (default) :  choices {countries, collective, individual}

def test_individual():
    argv = ['individual']
    main(argv)

def test_collective():
    argv = ['collective','--top','4']
    main(argv)

def test_countries():
    argv = ['countries','--top','10']
    main(argv)


# # Testing when command is missing

# def test_args_missing():
#     argv = []
#     with pytest.raises(SystemExit) as sysexit:
#         main(argv)
#     assert sysexit.value.code == 2


# # Testing wrong command (not among the choices)

# def test_main_wrong_argscommand():
#     argv = ['athletes']
#     try:
#         main(argv)
#     except SystemExit as sysexi:
#         assert sysexi.code == 2


# # Testing wrong type command (int or not str)

# def test_collective_not_string():
#     try:
#         argv = [collective]
#     except NameError as nm:
#         print(f"Erreur : {nm}")

# def test_argument_int():
#     argv = [123]
#     with pytest.raises(TypeError) as te:
#         main(argv)



# ######### TESTING TOP ARGUMENT ###########

# By default, top is 10. Testing 'ArgumentTypeError' for the '--top' argument.

## Code intelligent

@pytest.mark.parametrize("argv, expected", [
    (['individual', '--top', '0'], argparse.ArgumentTypeError),        # Testing top is 0
    (['collective', '--top', '-2'], argparse.ArgumentTypeError),       # Testing top is negative
    (['countries', '--top', '-10'], argparse.ArgumentTypeError),       # Testing top is negative too
    (['individual', '--top', 'abc'], SystemExit),                      # Testing when top is not 'int' but 'str'
])
def test_wrong_top_values(argv, expected):
    if expected == SystemExit:
        with pytest.raises(expected) as sysexit:
            main(argv)
        assert sysexit.value.code == 2
    else:
        with pytest.raises(expected):
            main(argv)


## premier essai 

# Testing top is 0

# def test_top_zero():
#     argv = ['individual','--top','0']
#     with pytest.raises(argparse.ArgumentTypeError):
#         main(argv)


# Testing top is negative

# def test_top_negative():     
#     argv = ['collective','--top','-2']
#     with pytest.raises(argparse.ArgumentTypeError):
#         main(argv)

# def test_top_negative_2():     
#     argv = ['countries','--top','-10']
#     with pytest.raises(argparse.ArgumentTypeError):
#         main(argv)


# Testing when top is not 'int' but 'str'

# def test_collective_str_top():
#     argv = ['individual','--top','abc']
#     try:
#         main(argv)
#     except SystemExit as sysexit:
#         sysexit.code == 2
