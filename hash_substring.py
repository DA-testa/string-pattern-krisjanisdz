# python3

b = 13
q = 256
output = []

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    ievade = input()
    if 'I' in ievade:
        pattern = input()
        text = input()
        return (pattern.rstrip(), text.rstrip())

    elif 'F' in ievade:
        file = input()
        with open ("tests/"+file, 'r') as fails:
            pattern = fails.readline()
            text = fails.readline()
            return (pattern.rstrip(), text.rstrip())
    
    else:
        print("wrong command")

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    pattern_len = len(pattern)
    text_len = len(text)
    h = 1

    for i in range(pattern_len - 1):
        h = (h * b) % q

    phash = 0
    thash = 0
    
    for i in range(pattern_len):
        phash = (b * phash + ord(pattern[i])) % q
        thash = (b * thash + ord(text[i])) % q

    for i in range(text_len - pattern_len + 1):
        if phash == thash:
            for j in range(pattern_len):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == pattern_len:
                output.append(i)

        if i < text_len - pattern_len:
            thash = (b * (thash - ord(text[i]) * h) + ord(text[i+pattern_len])) % q

            if thash < 0:
                thash = thash + q
    
    return output

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))