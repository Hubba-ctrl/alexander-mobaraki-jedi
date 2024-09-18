def xo(string_input):
    string_input = string_input.lower()
    count_x = string_input.count("x")
    count_o = string_input.count("o")
    return count_x == count_o 