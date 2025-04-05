import pandas as pd

def merge_with_pandas(input_path, output_path):
    # 读取Markdown表格
    df = pd.read_table(input_path, sep='|', skipinitialspace=True)
    df = df.dropna(axis=1, how='all')  # 删除空列
    
    # 合并前两行
    df.iloc[0] = df.iloc[0].str.cat(df.iloc[1], sep=' ')
    df = df.drop(1)  # 删除第二行
    
    # 保存为Markdown
    with open(output_path, 'w') as f:
        f.write(df.to_markdown(index=False))

# 使用示例
merge_with_pandas('input.md', 'output.md')