import openpyxl
import excel_util_write as ew

# title_head = ['ID', 'PROVINCENAME', 'KEYWORD', 'ORGNAME', 'ADDRESSLINE', 'APPROVERNAME', 'REGISTRATIONNO',
#               'SPECIALTYPRACTICE', 'LEVELNAME','LEGALPERSON', 'CORPORATION', 'LICENCEPERIOD', 'DETAILHREF', 'SEARCHBATCHNO',
#               'CREATEDATE', 'IMPFLAG']
title_head = {'ID': 'id', 'PROVINCENAME': '省份', 'KEYWORD': '查询关键字', 'ORGNAME': '医疗机构名称', 'ADDRESSLINE': '地址',
               'APPROVERNAME': '审批机关','REGISTRATIONNO': '登记号', 'SPECIALTYPRACTICE': '诊疗科目', 'LEVELNAME': '级别',
               'LEGALPERSON': '法人', 'CORPORATION': '负责人', 'LICENCEPERIOD':'执业许可证有效期', 'DETAILHREF':'详细',
               'SEARCHBATCHNO': '查询批次', 'CREATEDATE': '创建日期', 'IMPFLAG': '是否已加入行业库'}
rows_data = [['id', '省份', '法人']]
rows_data.index(title_head, 0, 1)
head = rows_data[0]
for i in range(len(head)):
    for key, value in title_head.items():
        if head[i].__eq__(value):
            head[i] = key


ew.WriteExcel('excel01.xlsx', rows_data).write_data_line()
