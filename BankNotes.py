# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 13:00:12 2025

@author: Dinesh kumar
"""
from pydantic import BaseModel
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float