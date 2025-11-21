# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
import keyword

def convert_source_file(input_path, output_path):
    # 1. 获取Python保留字集合
    reserved_words = set(keyword.kwlist)
    
    # 2. 读取源文件内容
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 3. 处理内容（按单词拆分，保留符号）
    processed_content = []
    current_word = []
    for char in content:
        if char.isalnum() or char == '_':  # 字母、数字、下划线属于单词部分
            current_word.append(char)
        else:
            # 处理当前积累的单词
            if current_word:
                word = ''.join(current_word)
                if word not in reserved_words:
                    # 非保留字，转为大写
                    processed_content.append(word.upper())
                else:
                    # 保留字，保持原样
                    processed_content.append(word)
                current_word = []
            # 添加符号
            processed_content.append(char)
    # 处理最后一个单词
    if current_word:
        word = ''.join(current_word)
        if word not in reserved_words:
            processed_content.append(word.upper())
        else:
            processed_content.append(word)
    
    # 拼接处理后的内容
    result = ''.join(processed_content)
    
    # 4. 保存到输出文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

# 调用函数（假设源文件是random_int.py，输出文件是converted_random_int.py）
convert_source_file('random_int.py', 'converted_random_int.py')
