import numpy as np
import datetime

def RentCalculator(purpose, area, income, price, start, end):
    if start >= end:
        rent = None
        return rent

    period = int((end-start).total_seconds()/86400)+1
    if purpose == '경작':
        income_applied = area*income*(period/365)
        price_applied = area*price*(period/365)
        
        income_rate = 0.1
        price_rate = 0.01
        
        rent_by_income = income_applied * income_rate
        rent_by_price = price_applied * price_rate
        
        rent = int(np.round(min(rent_by_income, rent_by_price), 0))
    elif purpose == '비경작':
        price_applied = area*price*(period/365)
        
        price_rate = 0.05
        vat = 0.1
        
        rent_by_price = (price_applied * price_rate)
        rent = int(np.round(rent_by_price*(1+vat), 0))
    
    return rent