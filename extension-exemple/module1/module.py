import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import numpy as np
import os

class Module1:
    def __init__(self):
        self.dataframe = pd.DataFrame({}) 
        self.subject = pd.DataFrame({})
        self.frequent_items = pd.DataFrame({})
        self.rules = pd.DataFrame({})
        # self.data = pd.DataFrame({'A': [1, 2, 3]})
        # self.data = np.array([1, 2, 3, 4, 5, 6])
    def load_dataset(self):
        dataset_path = os.path.expanduser('~') + '/.datasets/module1/Online Retail.xlsx'
        df = pd.read_excel(dataset_path, nrows=10)
        df['Description'] = df['Description'].str.strip()
        df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
        df['InvoiceNo'] = df['InvoiceNo'].astype('str')
        df = df[~df['InvoiceNo'].str.contains("C")]
        self.dataframe = df 

    def get_columns(self):
        return self.dataframe.columns

    def get_selectable_values(self):
        return self.dataframe['Country'].unique()

    def get_dataframe(self):
        return self.dataframe

    def get_subject_data(self):
        return self.subject

    def get_rules(self):
        return self.rules

    def get_frequent_items(self):
        return self.frequent_items

    def extract_frequent_items(self, min_support = 0.1, low_memory=False, max_len=None):
        self.frequent_items = apriori(self.subject, min_support=min_support, use_colnames=True, low_memory=low_memory, max_len=max_len)


    def extract_rules(self, min_confidence=0.1):
        rules = association_rules(self.frequent_items, metric='lift', min_threshold=min_confidence, support_only=True)
        df = pd.DataFrame(rules)
        df['Itemset'] = df.apply(lambda row: '+'.join(str(x) for x in row['antecedents']), axis=1)
        df['Rule'] = df.apply(lambda row: '->'.join([str(x) for x in row['consequents']]), axis=1)
        df.dropna(subset=['Itemset'], inplace=True)
        df['Itemset'] = df['Itemset'].apply(lambda x: x.split('+'))
        df.dropna(inplace=True)
        self.rules = df



    def train(self, min_support = 0.1, min_confidence = 0.1, low_memory=False, max_len=None):
        frequent_items = apriori(self.subject, min_support=min_support, use_colnames=True, low_memory=low_memory, max_len=max_len)
        print(frequent_items)
        rules = association_rules(frequent_items, metric='lift', min_threshold=min_confidence, support_only=True)
        df = pd.DataFrame(rules)
        df['Itemset'] = df.apply(lambda row: '+'.join(str(x) for x in row['antecedents']), axis=1)
        df['Rule'] = df.apply(lambda row: '->'.join([str(x) for x in row['consequents']]), axis=1)
        df.dropna(subset=['Itemset'], inplace=True)
        df['Itemset'] = df['Itemset'].apply(lambda x: x.split('+'))
        df.dropna(inplace=True)
        print(df)
        return df


    def set_subject(self, sub_val):
        self.subject = self.select_subject(sub_val)

    def select_subject(self, sub_val):
        df = self.dataframe
        subject = (df[df['Country'] == sub_val]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))
        subset_enc = subject.applymap(self.hot_encode)
        subset = subset_enc
        return subset
    
    def hot_encode(self, x):
        try:
            x = int(x)
            if(x<= 0):
                return 0
            if(x>= 1):
                return 1
        except:
            return 0


if __name__ == "__main__":
    a = Module1()
    a.load_dataset()
    # print(a.get_selectable_values())
    # print(a.get_dataframe().shape)
    # print(a.get_dataframe().shape[1])
    # print([ 'X' for x  in range(a.get_dataframe().shape[1])])
    a.set_subject('United Kingdom')
    print(a.get_subject_data())
    # res = a.train(min_support=0.0001, min_confidence=0.0001)
    # print(res)

    # print(a.get_colums())
    # print(a.get_selectable_values())

