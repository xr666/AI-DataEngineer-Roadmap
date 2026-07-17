# 1、写法 ''  "" 都可以
a = '测试'
b = "测试"
print(a,b)

# 2、字符串拼接 用f""  变量写在{}里

schema = "ads_sk"

table = "app_trs_bank_acct_bal_df"

print(f"{schema}.{table}")

# 3、常见字符串写法

# 3.1 upper() 大写
table  = "app_trs_bank_acct_bal_df"
print(table.upper())
# 3.2 lower()  小写
# 3.3 replace() 替换
company = "中国责任有限公司"
company = company.replace("有限公司","")
print(company)
# 3.4 split() 切分 
data = "2026-07-17"
print(data.split("-"))
# 3.5 strip() 去空格
name = " 你好 "
print(name.strip())