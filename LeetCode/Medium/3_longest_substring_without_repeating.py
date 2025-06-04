def naieve(input_string):
    n = len(input_string)

    max_count = 0

    for i in range(n):
        dup_set = set()
        local_max_count = 0
        for j in range(i + 1, n):
            if input_string[j] in dup_set:
                max_count = max(local_max_count, max_count)
                break
            else :
                dup_set.add(input_string[j])
                local_max_count += 1 
    return max_count

def optimised(input_string):
    n = len(input_string)
    lptr = 0
    max_count = 0
    unique_chars = set()

    for i in range(n):
        if input_string[i] in unique_chars:
            max_count = max(max_count, i - lptr)
            while input_string[i] != input_string[lptr]:
                unique_chars.remove(input_string[lptr])
                lptr += 1
            lptr +=1
        else :
            unique_chars.add(input_string[i])
            max_count = max(max_count, i - lptr + 1)

    return max_count


def clean_optimised(s: str) -> int:
    left, max_count = 0, 0
    char_set = set()

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_count = max(max_count, right - left + 1)

    return max_count




if __name__ == "__main__":
    inp_string = input()
    print(optimised(inp_string))