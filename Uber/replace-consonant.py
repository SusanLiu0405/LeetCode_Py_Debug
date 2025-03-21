def replace_nth_consonant(message, n):
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonants_upper = consonants.upper()


    result = []
    consonant_count = 0

    for char in message:
        if char.lower() in consonants:
            consonant_count += 1
            if consonant_count % n == 0:
                if char.islower():
                    next_consonant = get_next_consonant(char, consonants)
                else:
                    next_consonant = get_next_consonant(char, consonants_upper)
                result.append(next_consonant)
            else:
                result.append(char)
        else:
            result.append(char)

    return "".join(result)


def get_next_consonant(char, consonant_list):
    index = consonant_list.index(char)
    return consonant_list[(index + 1) % len(consonant_list)]



message = "NNNNNN"
n = 3
print(replace_nth_consonant(message, n))
