# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:29:06 2021

@author: Daniel.Silva
"""
from selenium.webdriver import Chrome
import time
import pandas as pd
from bs4 import BeautifulSoup


class Search:
    def __init__(self, user, password, driver):
        self.user = user
        self.password = password
        self.driver = driver
        self.url = 'url'


    # call the page init
    def call(self):
        self.driver.get(self.url)
        self.operate()


    def init_query(self):
        list_query={
                'your query here!'
            }
        
        result_query=map(self.search_querys, list_query.values())
        result = list(result_query)
        self.export_table(result)


    # oper
    def operate(self):
        time.sleep(2)
        id = self.driver.find_element_by_name('strCpf')
        id.click()
        id.send_keys(self.user)
        time.sleep(2)
        password = self.driver.find_element_by_name('senha')
        password.send_keys(self.password)
        time.sleep(1)
        btn = self.driver.find_element_by_name('btEnviar')
        btn.click()
        time.sleep(2)
        sql_sed = self.driver.get('url')
        time.sleep(1)
        self.init_query()


    #search query
    def search_querys(self, query):
        btn_clear = self.driver.find_element_by_name('btLimpar').click()
        time.sleep(1)
        text_camp = self.driver.find_element_by_name('strCampoSQL')
        text_camp.click()
        time.sleep(1)
        text_camp.send_keys(query)
        time.sleep(1)
        search = self.driver.find_element_by_name('btPesquisar').click()
        parser = self.parser_table()
        return parser


    #init parser with beautifulsoup    
    def parser_table(self):
        html_table = self.driver.find_element_by_xpath('/html/body/form/table[2]').get_attribute('outerHTML')
        soup = BeautifulSoup(html_table, 'html.parser')
        soup_t = soup.find(name='table')
        df_full = pd.read_html(str(soup_t))[0]
        return df_full


    #export table
    def export_table(self, table):
        with pd.ExcelWriter('/output/base_copy.xlsx', engine='xlsxwriter') as writer:  
            table[0].to_excel(writer, sheet_name='', index=False, encoding='UTF-8')
            table[0].to_excel(writer, sheet_name='', index=False, encoding='UTF-8')
            table[1].to_excel(writer, sheet_name='', index=False, encoding='UTF-8')
            table[1].to_excel(writer, sheet_name='', index=False, encoding='UTF-8')
            table[2].to_excel(writer, sheet_name='', index=False, encoding='UTF-8')
            table[3].to_excel(writer, sheet_name='', index=False, encoding='UTF-8')
            table[4].to_excel(writer, sheet_name='', index=False, encoding='UTF-8')
            
        table[0].to_csv('/output/name.csv', index=False, encoding='utf-8-sig')    
        table[1].to_csv('/output/name.csv', index=False,  encoding='utf-8-sig')
        table[2].to_csv('/output/name.csv', index=False,  encoding='utf-8-sig')
        table[3].to_csv('/output/name.csv', index=False,  encoding='utf-8-sig')
        table[4].to_csv('/output/name.csv', index=False, encoding='utf-8-sig')


    #driver quit
    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    browser = Chrome(executable_path='/driver/chromedriver')
    start = Search('login', 'pass', browser)
    start.call()
    start.quit()    