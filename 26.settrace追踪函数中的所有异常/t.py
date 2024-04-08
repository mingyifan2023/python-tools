import sys

# def trace_func(frame, event, arg):
#     if event == 'exception':
#         exception_type, exception_value, traceback = arg
#         if not hasattr(trace_func, 'first_exception'):
#             trace_func.first_exception = {
#                 'exception_type': exception_type,
#                 'exception_value': exception_value,
#                 'traceback': traceback
#             }
#         else:
#             print("First Exception:")
#             print(f"Type: {trace_func.first_exception['exception_type']}")
#             print(f"Value: {trace_func.first_exception['exception_value']}")
#             print("Second Exception:")
#             print(f"Type: {exception_type}")
#             print(f"Value: {exception_value}")
#             print("-"*16)
#
#     return trace_func
all_exception_values = []
def trace_func(frame, event, arg):
    global all_exception_values
    if event == 'exception':
        exception_type, exception_value, traceback = arg
        all_exception_values.append(exception_value)
        # if not hasattr(trace_func, 'all_exception_values'):
        #     trace_func.all_exception_values = set()
        # 
        # trace_func.all_exception_values.add(exception_value)

    return trace_func

def func():

    ok = ""
    for item in range(1):

        try:
            b_check()
            ok="1"
        except Exception as e:
            continue
    if ok=="":
        print("00")

def b_check():
    try:
        x = 1 / 0  # First exception (ZeroDivisionError)

    except Exception :
        raise "check error "


sys.settrace(trace_func)
func()
sys.settrace(None)

print(trace_func.all_exception_values)
