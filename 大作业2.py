# encoding: utf-8
import string

def encrypt(plaintext, substitution_table):
    ciphertext = []
    for char in plaintext.lower():
        if char.isalpha():
            encrypted_char = substitution_table.get(char, char)  # 使用替换表替换字母，保留非字母字符不变
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)  # 非字母字符保持不变
    return ''.join(ciphertext)

def decrypt(ciphertext, substitution_table):
    decryption_table = {v: k for k, v in substitution_table.items()}  # 构建解密用的替换表
    plaintext = []
    for char in ciphertext.lower():
        if char.isalpha():
            decrypted_char = decryption_table.get(char, char)  # 使用解密替换表恢复字母，保留非字母字符不变
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)  # 非字母字符保持不变
    return ''.join(plaintext)

with open('代换表存储地址') as f:
    keys=f.read()
Key = keys.split('\n')

substitution_table = {
    'a': Key[0], 'b': Key[1], 'c': Key[2], 'd': Key[3], 'e': Key[4],
    'f': Key[5], 'g': Key[6], 'h': Key[7], 'i': Key[8], 'j': Key[9],
    'k': Key[10], 'l': Key[11], 'm': Key[12], 'n': Key[13], 'o': Key[14],
    'p': Key[15], 'q': Key[16], 'r': Key[17], 's': Key[18], 't': Key[19],
    'u': Key[20], 'v': Key[21], 'w': Key[22], 'x': Key[23], 'y': Key[24],
    'z': Key[25]
  }

def bubble_sort_dict_by_value(input_dict):
    items = list(input_dict.items())
    n = len(items)
    
    # 冒泡排序
    for i in range(n):
        # 每轮冒泡将最大的数移动到最前
        for j in range(0, n-i-1):
            if items[j][1] < items[j+1][1]:
                # 交换元素
                items[j], items[j+1] = items[j+1], items[j]
    
    sorted_dict = dict(items)
    return sorted_dict

def suggest_decryption(text):
    # 初始化字母频率字典
    frequencies = {char: 0 for char in string.ascii_lowercase}
    total_chars = 0

    # 遍历文本，统计每个字母出现的次数
    for char in text.lower():
        if char in frequencies:
            frequencies[char] += 1
            total_chars += 1
    
    # 将频率转换为百分比
    for char in frequencies:
        frequencies[char] = frequencies[char] / total_chars * 100

    sorted_frequencies = bubble_sort_dict_by_value(frequencies)

    normal_frequencies = {
        'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
        'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
        'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
        'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
        'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974,
        'z': 0.074
    }
    sorted_normal_frequencies = bubble_sort_dict_by_value(normal_frequencies)
    suggestions=[]
    for char in sorted_normal_frequencies:
         suggestions.append((char))

    keys1 = list(sorted_frequencies.keys())
    keys2 = list(sorted_normal_frequencies.keys())
    
    for i in range(26):
        print(f"建议将{keys1[i]}替换为{keys2[i]},明文文本频率为{sorted_frequencies[keys1[i]]}%")

    return frequencies

Choose = input("请选择你想实现的功能：\n[1]单表代换加解密\n[2]单表代换密码破译\n")
choose = int(Choose)
if choose == 1 :
    Way = input("请选择加解密：\n[1]单表代换加密\n[2]单表代换解密\n")
    way = int(Way)
    if way == 1:
        plaintext = input("请输入已知密文：")
        encrypted_text = encrypt(plaintext, substitution_table)
        print("加密后的明文是:", encrypted_text)
    elif way == 2:
        plaintext = input("请输入已知明文：")
        decrypted_text = decrypt(plaintext, substitution_table)
        print("解密后的密文是:", decrypted_text)
elif choose == 2:
    ciphertext = input("请输入要破译的密文: ").strip().lower()

    # 初始破译建议
    initial_suggestions = suggest_decryption(ciphertext) 




