num_test_cases = int(input())

for _ in range(num_test_cases):
    word_pos = int(input())
    sentence = input()
    
    words = sentence.split(" ")
    
    if len(sentence)> 0:
        if len(words) > word_pos:
            total = 0
            for ch in words[word_pos]:
                total += ord(ch)
            print(total)
            continue

    print(-1)
