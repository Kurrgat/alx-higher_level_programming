#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        first_char = None
    else:
        first_char = sentence[0]
    return len(sentence), first_char

if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
