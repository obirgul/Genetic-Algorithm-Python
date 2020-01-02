# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:14:06 2020

@author: orcunb
"""

import numpy as np

def uyumf(arr):
    for i in range(0,len(arr)):
        dizi = arr[i,:]
        if sum(dizi*[20,18,22,16])>= 200:
            if sum(dizi*[50,40,40,60])>= 800:
                if sum(dizi*[20,15,20,25])>= 250:
                    if sum(dizi*[100,90,116,100])>= 70:
                        if sum(dizi*[18,16,15,20])>= 24:
                            if sum(dizi*[1000,800,850,900])>= 1500:
                                uyum = 1
        return uyum

liste = []
while len(liste) < 10:
    a = np.random.uniform(low=0, high=25.0, size=[1,4])
    if uyumf(a) == 1:
        liste.append(a)

liste = np.asarray(liste, dtype=np.float32)

def amac_fonk(arr):
    amac = []
    for i in range(0,len(arr)):
        amac.append(sum(arr[i,:]*[55,94,50,55]))
    return amac

amac_deger = amac_fonk(liste)

oran_cap = np.random.uniform(low=0, high=1.0, size=10)

def cap_list(arr,oran,oran_cap):
    liste = []
    for i in range(0,len(oran_cap)):
        if oran_cap[i] >= oran:
            liste.append(arr[i,:])
    return liste

cap = cap_list(liste,0.4,oran_cap)
cap = np.asarray(cap, dtype=np.float32)

def carp(cap):
    liste = []
    for i in range(0,len(cap)):
        for j in range(i+1,len(cap)+1):
            k =np.random.randint(0,3)
            c1 = cap[i,:k] + cap[j,k:]
            c2 = cap[j,:k] + cap[i,k:]
            if uyumf(c1) == 1: 
                liste.append(c1)
            if uyumf(c2) == 1:
                liste.append(c2)
    return liste

liste2 = carp(cap)

### To be continued...


