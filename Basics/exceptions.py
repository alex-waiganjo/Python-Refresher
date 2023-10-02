# Exception Errors
# - KeyError
# - NameError
# - ImportError
# - ZeroDivisionError
# - FloatingPointError
# - FileNotFoundError


name = 'lorna'
try:
    print(names)
except NameError:
    print('Error')
except:
    print("Something went wrong")
finally:
    print("Try block has come to a halt!")


# class DataTypeMismatchError(Exception):
#     pass

# try:
#     m = 9
#     p = 7.9
#     if type(m) != type(p):
#         raise DataTypeMismatchError("Not of same type")
#     print('Same Data Type')
# except DataTypeMismatchError as e:
#     print(f'Error: {e}')

# except FloatingPointError:
#     print('floating point error')    



try:
    r=9.0
    l=0.0
    t =r/l
    print(t)    
except ZeroDivisionError:
    print("Floating point error occurred")
except FloatingPointError:
    print("error")    


f_names= {
    "Name":"Rose",
    "Name":"Ale",
    "Name":"Pauline",
    "Name":"Ken"     
}
ll = list(f_names['Name'])
try:
    print(ll)
except IndexError:
    print("Cannot find the Index ")    