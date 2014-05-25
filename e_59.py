#!/usr/bin/env python
'''
Created on 10 feb. 2012

@author: Julien Lengrand-Lambert

DESCRIPTION: Solves problem 59 of Project Euler
Each character on a computer is assigned a unique code
and the preferred standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key
on the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message,
and the key is made up of random bytes.
The user would keep the encrypted message and the encryption key in different locations,
and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users,
so the modified method is to use a password as a key. If the password is
shorter than the message, which is likely, the key is repeated cyclically
throughout the message. The balance for this method is using a sufficiently
long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher1.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
 text must contain common English words, decrypt the message and find
 the sum of the ASCII values in the original text.
'''
import itertools
import string

base = 16 # hey, its hex!
printable_letters = string.printable # list of all printable characters

#frequency of english letters
en_freq = {'a': 0.08167,
            'b': 0.01492,
            'c':0.02782,
            'd':0.04253,
            'e':0.12702,
            'f':0.02228,
            'g':0.02015,
            'h':0.06094,
            'i':0.06966,
            'j':0.00153,
            'k':0.00772,
            'l':0.04025,
            'm':0.02406,
            'n':0.06749,
            'o':0.07507,
            'p':0.01929,
            'q':0.00095,
            'r':0.05987,
            's':0.06327,
            't':0.09056,
            'u':0.02758,
            'v':0.00978,
            'w':0.02360,
            'x':0.00150,
            'y':0.01974,
            'z':0.00074}


def _xorhex(a, b):
    """
    XORs a against b and returns the result
    a and b are expected to be int values

    XOR Truth Table
    Input   Output
    A   B
    0   0   0
    0   1   1
    1   0   1
    1   1   0
    """
    long_res = a ^ b
    string_res = '%x' % long_res # returns a string version
    return long_res


def load_data(filename):
    "Loads the data of the filename into a table"
    file = open(filename, "r")
    stuff = file.read()
    return [int(val) for val in stuff.split(',')]

def all_passwords(range, length):
    '''
    Returns all possible passwords given a range of ascii_values, and the length of the password
    '''
    return list(set(itertools.combinations(range*3, length)))

def apply_password(value, password):
    """
    Applies a given password to the message.
    """
    long_pass = repeat_password(password, len(value))
    return [_xorhex(a, b) for a, b in zip(value, long_pass)]


def repeat_password(password, length):
    """
    Repeats a password to match the requested size.
    Ex : [1, 2, 3], 7 => [1, 2, 3, 1, 2, 3, 1]
    """
    repeat = length / len(password)
    rest = length % len(password)

    return password * repeat + password[:rest]

def all_solutions(data, pass_range, length):
    """
    Prints all possible solutions
    """
    res = []
    all_pass = all_passwords(pass_range, length)
    total = len(all_pass)
    print total
    idx = 0
    for password in all_pass:
        idx += 1
        print "%d / %d" % (idx, total)
        sol = apply_password(data, password)
        res.append([to_ascii(sol), password])
    return res

def to_ascii(data):
    """
    Turns a list of ascii values into a proper string
    """
    res = ""
    for el in data:
        res += chr(el)
    return res

def discard_non_printable(solutions):
    """
    We discard from a list of hex all the elements that cannot be printed.
    #FIXME: Do better
    """
    res = []
    for val in solutions:

        is_printable = True
        for v in val[0]:
            if not(v in printable_letters):
                is_printable = False

        if is_printable:
            res.append(val)

    return res

def letter_freq(work_val):
    """
    Calculate the frequency of the elements in the string val
    Returns a dictionary of the form {element: frequency} for all elements of val.
    Only present elements will be present in the dictionary (frequency > 0)
    """
    counts = map(work_val.count ,work_val) # gets count of each element of hex_val
    freqs = [(float(x) / len(work_val)) for x in counts]
    #freqs = [x for x in counts]
    return dict(zip(work_val,freqs)) # transforms into dict of unique values associated to frequencies

def chi2(ref_dict, test_dict, length):
    """
    Performs a chi2 adequation testing.

    Given a reference dictionary and a corresponding dctionary to be tested, returns a score corresponding to
    the similitude between the test data and the reference data.
    The lower the score, the higher the similitude.

    Dictionaries are expected to be under the {value:frequency} form.
    Example : chi2({a:0.08, b:0.92}, {a:0.80, b:0.20}, 12)

    length corresponds to the number of elements needed to acquire test_dict

    Returns a float value

    """
    my_keys = ref_dict.keys()
    score = 0
    for m in my_keys:
        if test_dict.has_key(m): # testing if occurence happened
            freq_val = length * test_dict[m]
        else:
            freq_val = 0
        ref_val = length * ref_dict[m]
        score += pow(freq_val - ref_val, 2) / ref_val
    return score

def strip_string_to_lowercase(s):
    """
    Returns s in lowercase, with all its special characters stripped
    Taken from here: http://stackoverflow.com/questions/638893/what-is-the-most-efficient-way-in-python-to-convert-a-string-to-all-lowercase-st#639325
    """
    tmpStr = s.lower().strip()
    retStrList = []
    for x in tmpStr:
        if x in string.ascii_lowercase:
            retStrList.append(x)

    return ''.join(retStrList)

def close_to_english(element):
    """
    Returns a score of likeliness for element to be english
    The computed score is the chi2 adequation test.

    The closest to 0, the most probable the sentence is to be in english
    Table can be found here, solutions at row 25 (english is 26 degrees of liberty).
    http://www.medcalc.org/manual/chi-square-table.php to get the values to compare to
    """
    # cleans the hex val of special characters, and puts to lowercase
    stripped_el = strip_string_to_lowercase(element)
    length_el = len(stripped_el)
    #calculates the letters frequency of element
    freqs = letter_freq(stripped_el)

    return chi2(en_freq, freqs, length_el)

def find_most_probable(data, pass_range, length):
    solutions = all_solutions(data, pass_range, length)
    # discards easy fuck ups
    solutions = discard_non_printable(solutions)

    best_candidate = ""
    best_chi = 1000000
    for sol in solutions:
        score = close_to_english(sol[0])
        if score < best_chi:
            best_chi = score
            best_candidate = sol

    return best_candidate

def get_solution(data, pass_range, length):
    solution = find_most_probable(data, ascii_range, 3)[0]
    sum = 0
    for val in solution:
        sum+=ord(val)
    return sum


if __name__ == '__main__':
    data = load_data("e_59_cipher1.txt")
    ascii_range = range(ord('a'), ord('z') + 1 )
    print get_solution(data, ascii_range, 3)