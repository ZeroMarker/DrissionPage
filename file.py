import pandas as pd

# 读取CSV文件
csv_file = 'C:\\Users\\ttft3\\Downloads\\需求-综合查询_20240601165517.csv'  # 替换为你的CSV文件路径
df = pd.read_csv(csv_file)

# 检查列名是否包含"标题"和"内容"
if '标题' in df.columns and '内容' in df.columns:
    # 提取"标题"和"内容"列
    selected_columns = df[['标题']]
    print(selected_columns)

    # 将提取的数据保存到新的CSV文件中
    output_csv = 'selected_columns.csv'  # 输出CSV文件的名称
    selected_columns.to_csv(output_csv, index=False)  # index=False表示不将行索引写入文件
else:
    print("CSV文件中没有找到'标题'或'内容'列")
