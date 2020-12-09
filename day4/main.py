# same thing as before
def char_position(string, char):
    # list to store positions for each 'char' in 'string'
    pos = []
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos


# after part 1 i realized that there is a much better way to parse the input
# now every passport is a list containing fields
# and there's also a master list containing all of the passports
def string_parsing(string):
    big_list = []
    small_list = []
    new_string = ''
    file1 = open(string, 'r')
    lines = file1.readlines()
    for line in lines:
        new_line = line[:-1]
        new_line = new_line + "/"
        if new_line == "/":
            big_list.append(small_list)
            small_list = []
        else:
            for char in new_line:
                if char == '/' or char == ' ':
                    small_list.append(new_string)
                    new_string = ""
                else:
                    new_string = new_string + char

    file1.close()
    return big_list


# checks if a given field is valid
# not really that hard, just long
def field_validation(field):
    type = field[0:3]
    value = field[4:]
    hcl_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
    ecl_set = {"amb", "blu", "brn", "grn", "gry", "hzl", "oth"}

    if type == "byr":
        if 1920 <= int(value) <= 2002:
            return True
        else:
            return False

    elif type == "iyr":
        if 2010 <= int(value) <= 2020:
            return True
        else:
            return False

    elif type == "eyr":
        if 2020 <= int(value) <= 2030:
            return True
        else:
            return False

    elif type == "hgt":
        if value[-2:] == "in" and 59 <= int(value[:-2]) <= 76:
            return True
        elif value[-2:] == "cm" and 150 <= int(value[:-2]) <= 193:
            return True
        else:
            return False

    elif type == "hcl":
        if value[0] == '#':
            for char in value[1:]:
                if char not in hcl_set:
                    return False
            if len(value[1:]) == 6:
                return True
            else:
                return False
        else:
            return False

    elif type == "ecl":
        if value in ecl_set:
            return True
        else:
            return False

    elif type == "pid":
        if len(value) == 9:
            return True
        else:
            return False

    else:
        return True


# the supreme version of the previous check
def passport_check():
    valid_counter = 0
    req_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    lines = string_parsing('day4/data.txt')
    for passport in lines:
        fields = {"cid"}
        # if a field has invalid info, the loop terminates instantly
        # if all fields are ok, there is a final check if all the fields are present
        for field in passport:
            if field_validation(field) is False:
                break
            else:
                fields.add(field[0:3])
        if fields == req_fields:
            valid_counter += 1

    print(valid_counter)

passport_check()