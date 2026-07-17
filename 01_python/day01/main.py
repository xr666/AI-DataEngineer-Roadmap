tables = [
"ODS"
,"DWD"
,"DWS"
,"ADS"
]
for table in tables:
    print(f"开始检查{table}")
    print(f"{table}检查完成")
    print("-" * 30)
print("全部检查完成")

def check_table(table):
    print(f"开始检查{table}")
    print(f"{table}检查完成")
    print("-" * 30)
tables = [
    "ods",
    "dwd",
    "dws",
    "ads"
]
for table in tables:
    check_table(table)
print("检查完成")
