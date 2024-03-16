
# 上面的结果无法针对于mock的进行统计
#
# import sys
#
# def count_variable_final_value(func, variable_name):
#     variable_values = {}
#
#     def trace(frame, event, arg):
#         if event == 'line':
#             co_varnames = frame.f_code.co_varnames
#             co_name = frame.f_code.co_name
#             if variable_name in co_varnames:
#                 local_vars = frame.f_locals
#                 variable_values[co_name] = local_vars.get(variable_name)
#
#         return trace
#
#     sys.settrace(trace)
#
#     try:
#         func()
#     finally:
#         sys.settrace(None)
#
#     return variable_values
#
# # Test function
# def abc(ddd):
#     print(ddd)
#     aaa = 2
#     commit()
#     commit()
#     aaa = 9
#     delete()
#
# # Functions to be tested
# def commit():
#     pass
#
# def delete():
#     pass
#
# # Test case for counting the final value of variable aaa inside abc with parameter
# def test_variable_final_value():
#     ddd_value = "Test Parameter"
#     variable_values = count_variable_final_value(lambda: abc(ddd_value), 'aaa')
#     print("Final values of variable 'aaa' in abc:")
#     for func_name, final_value in variable_values.items():
#         print(f"{func_name}: {final_value}")
#
# # Run the test case
# test_variable_final_value()

import sys

def count_function_calls(func, *func_names):
    local_var_count = {func_name: 0 for func_name in func_names}

    def trace(frame, event, arg):
        if event == 'call' and frame.f_code.co_name in local_var_count:
            local_var_count[frame.f_code.co_name] += 1
        return trace

    sys.settrace(trace)

    try:
        func()
    finally:
        sys.settrace(None)

    return local_var_count

# Test function
def abc(ddd):
    print(ddd)
    commit()
    commit()
    a = 0
    delete(a)

# Functions to be tested
def commit():
    pass

def delete(a):
    pass

# Test case for counting function calls inside abc
def test_abc_function_calls():
    ddd_value = "Test Parameter"
    function_counts = count_function_calls(lambda: abc(ddd_value), 'commit', 'delete')
    print("Function call counts inside abc:")
    for func_name, count in function_counts.items():
        print(f"{func_name}() called {count} times")

# Run the test case
test_abc_function_calls()
