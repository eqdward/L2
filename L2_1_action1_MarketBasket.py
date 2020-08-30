# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 19:12:27 2020

@author: yy
"""

import pandas as pd

data = pd.read_csv(r"C:\Users\yy\Desktop\BI\L2\L2-1\L2-code\MarketBasket\Market_Basket_Optimisation.csv", header=None)

def strip(x):
    x = str(x).strip()
    return x

data = data.applymap(strip)   # 去除空格，有一个asparagus包含了空格


# 使用efficient_apriori
def rule1():
    from efficient_apriori import apriori
    transactions = []
    for i in range(data.shape[0]):
        temp = []
        for j in range(data.shape[1]):
            if data.values[i][j] != 'nan':
                temp.append(data.values[i][j])
        transactions.append(temp)
    
    itemsets, rules = apriori(transactions, min_support=0.03,  min_confidence=0.3)
    print('频繁项集：', itemsets)
    print('关联规则：', rules)
    
rule1()



# 使用mlxtend.frequent_patterns
def rule2():
    from mlxtend.frequent_patterns import apriori
    from mlxtend.frequent_patterns import association_rules

    transactions = []
    for i in range(data.shape[0]):
        temp = data.iloc[i,:]
        tran = temp.str.cat(sep='|')
        transactions.append(tran)

    df = pd.DataFrame(data=transactions, columns=['goods'])
    hot_encoded = df.drop('goods',1).join(df.goods.str.get_dummies(sep='|'))
    hot_encoded.drop('nan', axis=1, inplace=True)

    frequent_itemsets = apriori(hot_encoded, min_support=0.03, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.1)
    print("频繁项集：", frequent_itemsets)
    print("关联规则：", rules[ (rules['lift'] >= 1) & (rules['confidence'] >= 0.3) ])

rule2()
