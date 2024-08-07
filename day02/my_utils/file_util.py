def print_file_info(file_name):
    f = None  # 先定义None,防止finally无法close
    try:
        f = open(file_name, 'r', encoding='utf-8')
        for line in f:
            print(line)
    except Exception as e:
        print(f"异常：{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = open(file_name, 'a', encoding='utf-8')
    f.write("\n")
    f.write(data)
    f.close()


if __name__ == '__main__':
    print_file_info("D:\\Nginx\\bil.txt")
    append_to_file("D:\\Nginx\\bill.txt", "abcd")
