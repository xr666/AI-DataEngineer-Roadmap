# 变量，就是给一块数据起了一个名字

# company = "腾讯集团"
# print(company)

# # sql场景 
# table_name = "ads_sk.app_trs_bank_acct_bal_df"
# sql = f"""
# select * from {table_name} limit 10
# """
# print(sql)

# 练习
# 1、定义变量：公司名称、企业编码、统计月份 并打印出来
company = "不知名"
code = "adsad12554"
month = "2026-07"
print(company,code,month)

# 2、定义table_name schema_name 并拼接起来
table_name = "app_trs_bank_acct_bal_df" 
schema_name = "ads_sk"
table = f"{schema_name}.{table_name}"
print(table)