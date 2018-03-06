import csv
import json


def transform():
    # 打开文件
    csv_file = open("spider_file/lagou_job.csv", "w")
    json_file = open("spider_file/lagou_job.json", "r")
    # 创建csv写入器
    csv_write = csv.writer(csv_file)
    # 写入数据
    job_list = json.load(json_file)  # 将json类型的文件转换为python对象
    # print(job_list)
    table_head = job_list[0].keys()
    table_data_list = []
    for job in job_list:
        table_data_list.append(job.values())
    # 写入表头
    csv_write.writerow(table_head)
    csv_write.writerows(table_data_list)

    # print(table_head)
    # 关闭文件
    csv_file.close()
    json_file.close()


if __name__ == '__main__':
    transform()


# def json_to_csv():
#     # 打开json文件
#     json_file = open("spider_file/tencent.json", "r")
#     # 打开csv文件
#     csv_file = open("spider_file/tencent.csv", "w")
#     # 创建写入器
#     csv_writer = csv.writer(csv_file)
#     # 提取表头
#     json_list = json.load(json_file)
#     table_head = json_list[0].keys()
#     # 提取内容
#     content_list = []
#     for dict_data in json_list:
#         content_list.append(dict_data.values())
#
#     # 写入表头
#     csv_writer.writerow(table_head)
#     # 写入内容
#     csv_writer.writerows(content_list)
#     # 关闭文件
#     csv_file.close()
#     json_file.close()
#
#
# if __name__ == '__main__':
#     json_to_csv()