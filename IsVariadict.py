from collections import defaultdict


class Function:
    def __init__(self, name, argument_types, is_variadic):
        self.name = name
        self.argument_types = argument_types
        self.is_variadic = is_variadic

    def __repr__(self):
        return self.name


'''
tuple(args + T/F) -> list of functions  
('String', 'Integer', 'Integer', False): [func_a], 
('String', 'Integer', True): [func_b], 
('Integer', True): [func_c], 
('Integer', 'Integer', True): [func_d], 
('Integer', 'Integer', 'Integer', False): [func_e], 
('String', False): [func_f], ('Integer', False): [func_g]

F = function cnt 
A = argument cnt 
'''
class FunctionLibrary:
    def __init__(self):
        self.arg_variadic_to_function_dict = defaultdict(list)

    # O(F*A)
    def register(self, functions):
        # O(F)
        for function in functions:
            # O(A)
            self.register_function(function)
        print(self.arg_variadic_to_function_dict)

    # argument_types = length K
    # e.g., ["Integer", "Integer", "Integer", "Integer"]
    # O(K^2 + F)
    def find_matches(self, argument_types):
        # O(K)
        tail_cnt = self.get_tail_arg_type_cnt(argument_types)
        tail_arg_type = argument_types[-1]
        # O(K)
        exclude_tail_arg_type = argument_types[:len(argument_types) - tail_cnt]
        matching_functions = []

        # false
        # O(K)
        # form the keys
        arg_variadic_key = exclude_tail_arg_type + [tail_arg_type] * tail_cnt + [False]
        # no append, extend
        # O(F)
        matching_functions.extend(self.arg_variadic_to_function_dict[tuple(arg_variadic_key)])
        # if use append instead: matching_functions = [[func_a, func_b]]
        # what we want: matching_functions = [func_a, func_b]

        # true
        # O(K)
        for cnt in range(1, tail_cnt + 1):
            # O(K)
            arg_variadic_key = exclude_tail_arg_type + [tail_arg_type] * cnt + [True]
            # O(F)
            matching_functions.extend(self.arg_variadic_to_function_dict[tuple(arg_variadic_key)])

        return matching_functions

    def register_function(self, function):
        argument_types = function.argument_types
        is_variadic = function.is_variadic
        argument_types.append(is_variadic)
        # why tuple? list is not hashable
        # O(A)
        self.arg_variadic_to_function_dict[tuple(argument_types)].append(function)

    def get_tail_arg_type_cnt(self, argument_types):
        if not argument_types:
            return 0

        tail_arg_type = argument_types[-1]
        tail_arg_type_cnt = 0
        for i in range(len(argument_types) - 1, -1, -1):
            if argument_types[i] == tail_arg_type:
                tail_arg_type_cnt += 1

        return tail_arg_type_cnt


# Test cases
func_library = FunctionLibrary()
func_a = Function("func_a", ["String", "Integer", "Integer"], False)
func_b = Function("func_b", ["String", "Integer"], True)
func_c = Function("func_c", ["Integer"], True)
func_d = Function("func_d", ["Integer", "Integer"], True)
func_e = Function("func_e", ["Integer", "Integer", "Integer"], False)
func_f = Function("func_f", ["String"], False)
func_g = Function("func_g", ["Integer"], False)
func_susan = Function("func_susan", ["String", "Integer", "Integer"], False)

func_library.register([func_a, func_b, func_c, func_d, func_e, func_f, func_g, func_susan])
print(func_library.find_matches(["String"])) # [func_f]
print(func_library.find_matches(["Integer"])) # [func_g, func_c]
print(func_library.find_matches(["Integer", "Integer", "Integer", "Integer"])) # [func_c, func_d]
print(func_library.find_matches(["Integer", "Integer", "Integer"])) # [func_e, func_c, func_d]
print(func_library.find_matches(["String", "Integer", "Integer", "Integer"])) # [func_b]
print(func_library.find_matches(["String", "Integer", "Integer"])) # [func_a, func_b]