import unicodedata

def jp_prolong(string):
    hyphen = "-"
    correct_string = ""
    for target in string:
        if target == hyphen and before_target != "Na":
            item = "ー"
        else:
            item = target
        before_target = unicodedata.east_asian_width(target)
        correct_string += item
    return correct_string

the_sheep_password = "バ-ラ-ミュ-"

print(jp_prolong(the_sheep_password))




