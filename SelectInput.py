import ipywidgets as widgets
import pandas as pd
import numpy as np
import io, os, sys,pickle

with open('country_dict.pickle','rb') as f:
        country_dict = pickle.load(f)
country_dict['Other']='Other'

with open('sic_reg.pickle','rb') as f:
        sic_reg = pickle.load(f)
        
def company_name_widget():
    return widgets.Text(
                        #value='',
                        placeholder='Zara Inc',
                        description='Name',
                        disabled=False)

def country_select_widget():
    l = [key for key,v in country_dict.items()]
    return widgets.Select(
            options=sorted(l),
            value='United States of America',
            row = 5,
            description='Country:',
            disabled=False)

def state_select_widget(countryba):
    if countryba == 'US':
        with open('us_state_list.pickle','rb') as f:
            us_state_list = pickle.load(f)
        return widgets.Select(
            options=list(us_state_list),
            value='VA',
            row = 5,
            description='US State:',
            disabled=False)
    if countryba == 'CA':
        with open('canada_state_list.pickle','rb') as f:
            canada_state_list = pickle.load(f)
        return widgets.Select(
            options=list(canada_state_list),
            value='ON',
            row = 5,
            description='Canada State:',
            disabled=False)

def division_select_widget():
    division_list = sorted(list(set(sic_reg['division'])))
    return widgets.Select(
        options=division_list,
        value='Manufacturing',
        rows=5,
        description='Division',
        disabled=False)

def industry_select_widget(div):
    industry_list = sorted(list(set(sic_reg[sic_reg['division']==div]['industry'])))
    return widgets.Select(
        options=industry_list,
        value=industry_list[0],
        rows=5,
        description='Industry',
        disabled=False)

def afs_select_widget():
    afs_list = ['afs_1-LAF','afs_2-ACC','afs_3-SRA','afs_4-NON','afs_5-SML']
    return widgets.Select(
        options=afs_list,
        value=afs_list[0],
        rows=5,
        description='Size',
        disabled=False)