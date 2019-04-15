import hashlib
text = 'aaacbbb'


def get_dif_str(text):
    hash_arr = []
    for i in range(1, len(text)):
        for j in range(len(text) - i + 1):
            hash = hashlib.sha1(text[j:j+i].encode('utf-8')).hexdigest()
            if hash not in hash_arr:
                hash_arr.append(hash)
                #print(text[j:j+i])
    return len(hash_arr)


print(f"Количество различных подстрок в строке {text}: {get_dif_str(text)}")
