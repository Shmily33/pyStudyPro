from data_define import Record
import json


class FileReader:
    def read_data(self) -> list[Record]:
        pass


class TextFileReader(FileReader):  # 读取文本文件

    def __init__(self, path):
        self.path = path  # 定义成员变量，记录文件路径

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='utf-8')
        record_list = []
        for line in f.readlines():
            line = line.strip()  # 回车就是换行，换行就是空格组成
            # print(line)
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='utf-8')
        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], data_dict["money"], data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list


if __name__ == '__main__':
    # text_file_reader = TextFileReader('数据\\2011年1月销售数据.txt')
    # text_file_reader.read_data()
    json_file_reader = JsonFileReader("数据\\2011年2月销售数据JSON.txt")
    list = json_file_reader.read_data()
    for record in list:
        print(record)
