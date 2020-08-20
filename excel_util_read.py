import openpyxl

class ReadExcel(object):  # 读取excel数据的类
    def __init__(self, file_name):
        """
        这个是用来初始化读取对象的
        :param file_name: 文件名 ---> str类型
        """
        # 打开文件
        self.wb = openpyxl.load_workbook(file_name)
        # 选择表单
        self.sh = self.wb.active

    def read_data_line(self):
        # 按行读取数据转化为列表
        rows_data = list(self.sh.rows)
        # print(rows_data)
        # 获取表单的表头信息
        titles = []
        for title in rows_data[0]:
            titles.append(title.value)
        # print(titles)
        # 定义一个空列表用来存储测试用例
        cases = [titles]
        for row in rows_data[1:]:
            # print(row)
            data = []
            for cell in row:  # 获取一条测试用例数据
                # 判断该单元格是否为字符串，如果是字符串类型则需要使用eval();如果不是字符串类型则不需要使用eval()
                # if isinstance(cell.value, str):
                #     data.append(eval(cell.value))
                # else:
                    data.append(cell.value)
            # 将该条数据存放至cases中
            cases.append(data)
        return cases


if __name__ == '__main__':
    r = ReadExcel('02.xlsx')
    data1 = r.read_data_line()
    # for row in data1[1:]:

