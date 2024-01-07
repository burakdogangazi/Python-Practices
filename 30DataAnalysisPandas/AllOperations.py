import numpy as np
import pandas as pd

#Pandas Serileri

labels_list = ["Mustafa","Kemal","Atatürk","Burak","Doğan"]

data_list = [10,20,30,40,50]


pd.Series(data=data_list,index=labels_list)

# Mustafa    10
# Kemal      20
# Murat      30
# Kadir      40
# Zeynep     50
# dtype: int64


pd.Series(data_list)

# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64


npArray = np.array([10,20,30,40,50])

pd.Series(npArray,labels_list)

# Mustafa    10
# Kemal      20
# Murat      30
# Kadir      40
# Zeynep     50
# dtype: int32


pd.Series(data = npArray,index = ["A","B","C","D","E"])

# A    10
# B    20
# C    30
# D    40
# E    50
# dtype: int32


dataDict ={"Kadir":30,"Kemal":80,"Kamuran":60}

pd.Series(dataDict)

# Kadir      30
# Kemal      80
# Kamuran    60
# dtype: int64


ser2017 = pd.Series([5,10,14,20],["Buğday","Mısır","Kiraz","Erik"])


# Buğday     5
# Mısır     10
# Kiraz     14
# Erik      20
# dtype: int64


ser2018 = pd.Series([2,12,12,6],["Buğday","Mısır","Çilek","Erik"])


# Buğday     2
# Mısır     12
# Çilek     12
# Erik       6
# dtype: int64

total = ser2017 + ser2018

# Buğday     7.0
# Erik      26.0
# Kiraz      NaN
# Mısır     22.0
# Çilek      NaN
# dtype: float64

total["Erik"] #26.0
total["Çilek"] #nan


#Dataframe Tanımlamaları

from numpy.random import randn

randn(3) # array([-0.31899844, -0.60651244,  0.0115352 ])

randn(3,3)

# array([[-1.27756556, -0.26529808, -0.62057683],
#        [-0.41800723,  1.51336574,  0.99838554],
#        [-0.06537945, -0.03931435, -0.37186047]])


df = pd.DataFrame(data = randn(3,3), index = ["A","B","C"], columns = ["Column1","Column2","Column3"])

df
# 	Column1 	Column2 	Column3
# A 	-0.957277 	0.050216 	0.375921
# B 	0.579557 	1.121642 	0.123859
# C 	0.040049 	-0.057692 	-1.013646

df["Column1"]
# A   -0.957277
# B    0.579557
# C    0.040049
# Name: Column1, dtype: float64


type(df["Column2"]) # pandas.core.series.Series


df.loc["A"]

# Column1   -0.957277
# Column2    0.050216
# Column3    0.375921
# Name: A, dtype: float64

type(df.loc["A"]) #pandas.core.series.Series


df[["Column1","Column3"]]

# 	Column1 	Column3
# A 	-0.957277 	0.375921
# B 	0.579557 	0.123859
# C 	0.040049 	-1.013646



df
# 	Column1 	Column2 	Column3
# A 	-0.957277 	0.050216 	0.375921
# B 	0.579557 	1.121642 	0.123859
# C 	0.040049 	-0.057692 	-1.013646


df["Column5"] = df["Column1"] + df["Column2"] + df["Column3"]

# 	Column1 	Column2 	Column3 	Column4 	Column5
# A 	-0.957277 	0.050216 	0.375921 	0.420434 	-0.531139
# B 	0.579557 	1.121642 	0.123859 	-2.358564 	1.825058
# C 	0.040049 	-0.057692 	-1.013646 	1.141054 	-1.031289

df.drop("Column5",axis = 1,inplace = True)# axis = 0 yatay axis = 1 dikey
#inplace kaydetmek için 

# 	Column1 	Column2 	Column3 	Column4
# A 	-0.957277 	0.050216 	0.375921 	0.420434
# B 	0.579557 	1.121642 	0.123859 	-2.358564
# C 	0.040049 	-0.057692 	-1.013646 	1.141054

df["Column1"]

# A   -0.957277
# B    0.579557
# C    0.040049
# Name: Column1, dtype: float64


df.loc["A"]

# Column1   -0.957277
# Column2    0.050216
# Column3    0.375921
# Column4    0.420434
# Name: A, dtype: float64


df.iloc[0]

# Column1   -0.957277
# Column2    0.050216
# Column3    0.375921
# Column4    0.420434
# Name: A, dtype: float64


df.loc["A","Column1"]
# -0.9572769073836257

df.loc["B","Column2"]
#1.121641501647012


df.loc[["A","B"],["Column1","Column2"]]
# 	Column1 	Column2
# A 	-0.957277 	0.050216
# B 	0.579557 	1.121642


#DataFrame Filtreleme

df = pd.DataFrame(randn(4,3),["A","B","C","D"],["Column1","Column2","Column3"])


# 	Column1 	Column2 	Column3
# A 	1.201322 	-1.240382 	-0.524557
# B 	2.018686 	-0.809915 	-1.407355
# C 	1.362349 	1.100202 	1.203840
# D 	0.211224 	-0.270672 	-1.031963


df > -1

# 	Column1 	Column2 	Column3
# A 	True 	False 	True
# B 	True 	True 	False
# C 	True 	True 	True
# D 	True 	True 	False


df > 0

# 	Column1 	Column2 	Column3
# A 	True 	False 	False
# B 	True 	False 	False
# C 	True 	True 	True
# D 	True 	False 	False

booleanDf = df > 0


booleanDf

# 	Column1 	Column2 	Column3
# A 	True 	False 	False
# B 	True 	False 	False
# C 	True 	True 	True
# D 	True 	False 	False


df[booleanDf]

# 	Column1 	Column2 	Column3
# A 	1.201322 	NaN 	NaN
# B 	2.018686 	NaN 	NaN
# C 	1.362349 	1.100202 	1.20384
# D 	0.211224 	NaN 	NaN


df[ df > 0]

# 	Column1 	Column2 	Column3
# A 	1.201322 	NaN 	NaN
# B 	2.018686 	NaN 	NaN
# C 	1.362349 	1.100202 	1.20384
# D 	0.211224 	NaN 	NaN


df["Column1"]

# A    1.201322
# B    2.018686
# C    1.362349
# D    0.211224
# Name: Column1, dtype: float64



df["Column1"] > 0

# A    True
# B    True
# C    True
# D    True
# Name: Column1, dtype: bool


df["Column1"] > 1

# A     True
# B     True
# C     True
# D    False
# Name: Column1, dtype: bool


df[df["Column1"]>1]

# 	Column1 	Column2 	Column3
# A 	1.201322 	-1.240382 	-0.524557
# B 	2.018686 	-0.809915 	-1.407355
# C 	1.362349 	1.100202 	1.203840


df[df["Column2"]> 1]

# 	Column1 	Column2 	Column3
# C 	1.362349 	1.100202 	1.20384

df[(df["Column1"]> 1) & (df["Column2"]> 1) ]


# 	Column1 	Column2 	Column3
# C 	1.362349 	1.100202 	1.20384


df[(df["Column1"]> 1) | (df["Column2"]> 1)]

# 	Column1 	Column2 	Column3
# A 	1.201322 	-1.240382 	-0.524557
# B 	2.018686 	-0.809915 	-1.407355
# C 	1.362349 	1.100202 	1.203840


df["Column4"] = pd.Series(randn(4),["A","B","C","D"])

# 	Column1 	Column2 	Column3 	Column4
# A 	1.201322 	-1.240382 	-0.524557 	-0.464258
# B 	2.018686 	-0.809915 	-1.407355 	2.456147
# C 	1.362349 	1.100202 	1.203840 	0.148764
# D 	0.211224 	-0.270672 	-1.031963 	-0.548775


df["Column5"] = randn(4)


# 	Column1 	Column2 	Column3 	Column4 	Column5
# A 	1.201322 	-1.240382 	-0.524557 	-0.464258 	0.547996
# B 	2.018686 	-0.809915 	-1.407355 	2.456147 	0.057294
# C 	1.362349 	1.100202 	1.203840 	0.148764 	-0.213625
# D 	0.211224 	-0.270672 	-1.031963 	-0.548775 	1.141542

df["Column6"] = ["newValue1","newValue2","newValue3","newValue4"]


# 	Column1 	Column2 	Column3 	Column4 	Column5 	Column6
# A 	1.201322 	-1.240382 	-0.524557 	-0.464258 	0.547996 	newValue1
# B 	2.018686 	-0.809915 	-1.407355 	2.456147 	0.057294 	newValue2
# C 	1.362349 	1.100202 	1.203840 	0.148764 	-0.213625 	newValue3
# D 	0.211224 	-0.270672 	-1.031963 	-0.548775 	1.141542 	newValue4


df.set_index("Column6",inplace = True)


# 	            Column1 	Column2 	Column3 	Column4 	Column5
# Column6 					
# newValue1 	1.201322 	-1.240382 	-0.524557 	-0.464258 	0.547996
# newValue2 	2.018686 	-0.809915 	-1.407355 	2.456147 	0.057294
# newValue3 	1.362349 	1.100202 	1.203840 	0.148764 	-0.213625
# newValue4 	0.211224 	-0.270672 	-1.031963 	-0.548775 	1.141542


df.index.names
# FrozenList(['Column6'])


#DataFramelerde MultiIndex Tanımlama

outerIndex = ["Group1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3"]


innerIndex = ["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]


list(zip(outerIndex,innerIndex))


# [('Group1', 'Index1'),
#  ('Group1', 'Index2'),
#  ('Group1', 'Index3'),
#  ('Group2', 'Index1'),
#  ('Group2', 'Index2'),
#  ('Group2', 'Index3'),
#  ('Group3', 'Index1'),
#  ('Group3', 'Index2'),
#  ('Group3', 'Index3')]


hierarchy = list(zip(outerIndex,innerIndex))


hierarchy = pd.MultiIndex.from_tuples(hierarchy)


hierarchy

# MultiIndex([('Group1', 'Index1'),
#             ('Group1', 'Index2'),
#             ('Group1', 'Index3'),
#             ('Group2', 'Index1'),
#             ('Group2', 'Index2'),
#             ('Group2', 'Index3'),
#             ('Group3', 'Index1'),
#             ('Group3', 'Index2'),
#             ('Group3', 'Index3')],
#            )

df = pd.DataFrame(randn(9,3),hierarchy,columns = ["Column1","Column2","Column3"])


# 		Column1 	Column2 	Column3
# Group1 	Index1 	-1.212740 	-0.898993 	-2.281579
#         Index2 	-1.319452 	-1.892799 	1.598520
#         Index3 	-0.519782 	-0.317485 	-1.464734
# Group2 	Index1 	-1.473614 	1.644832 	-0.592261
#         Index2 	-1.112540 	-0.308732 	1.661544
#         Index3 	-0.793026 	2.584869 	-0.308565
# Group3 	Index1 	0.111535 	0.521636 	0.200833
#         Index2 	-1.436732 	-0.985544 	-0.514861
#         Index3 	1.052452 	0.328317 	-0.766868


df["Column1"]

# Group1  Index1   -1.212740
#         Index2   -1.319452
#         Index3   -0.519782
# Group2  Index1   -1.473614
#         Index2   -1.112540
#         Index3   -0.793026
# Group3  Index1    0.111535
#         Index2   -1.436732
#         Index3    1.052452
# Name: Column1, dtype: float64

df.loc["Group1"]

# 	Column1 	Column2 	Column3
# Index1 	-1.212740 	-0.898993 	-2.281579
# Index2 	-1.319452 	-1.892799 	1.598520
# Index3 	-0.519782 	-0.317485 	-1.464734

df.loc[["Group1","Group2"]]


# 		Column1 	Column2 	Column3
# Group1 	Index1 	-1.212740 	-0.898993 	-2.281579
# Index2 	-1.319452 	-1.892799 	1.598520
# Index3 	-0.519782 	-0.317485 	-1.464734
# Group2 	Index1 	-1.473614 	1.644832 	-0.592261
# Index2 	-1.112540 	-0.308732 	1.661544
# Index3 	-0.793026 	2.584869 	-0.308565


df.loc["Group1"].loc["Index1"]["Column1"]
# -1.2127397783080827


df.index.names
# FrozenList([None, None])

df.index.names = ["Groups","Indexes"]


# 		            Column1 	Column2 	Column3
# Groups  Indexes 			
# Group1  Index1 	-1.212740 	-0.898993 	-2.281579
#         Index2 	-1.319452 	-1.892799 	1.598520
#         Index3 	-0.519782 	-0.317485 	-1.464734
# Group2  Index1 	-1.473614 	1.644832 	-0.592261
#         Index2 	-1.112540 	-0.308732 	1.661544
#         Index3 	-0.793026 	2.584869 	-0.308565
# Group3  Index1 	0.111535 	0.521636 	0.200833
#         Index2 	-1.436732 	-0.985544 	-0.514861
#         Index3 	1.052452 	0.328317 	-0.766868


df.xs("Group1").xs("Index1").xs("Column1")
# -1.2127397783080827


df.xs("Index1") # KeyError: 'Index1'


df.xs("Index1",level = "Indexes")

# 	        Column1 	Column2 	Column3
# Groups 			
# Group1 	-1.212740 	-0.898993 	-2.281579
# Group2 	-1.473614 	1.644832 	-0.592261
# Group3 	0.111535 	0.521636 	0.200833



#Kayıp Ve Bozuk Veriler

arr = np.array([[10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,10]])


# array([[10., 20., nan],
#        [ 5., nan, nan],
#        [21., nan, 10.]])

df = pd.DataFrame(arr,index = ["Index1","Index2","Index3"],columns = ["Column1","Column2","Column3"])


# 	Column1 	Column2 	Column3
# Index1 	10.0 	20.0 	NaN
# Index2 	5.0 	NaN 	NaN
# Index3 	21.0 	NaN 	10.0


df.dropna() # axis = 0 index göre bakar na olan satırları siler
#
	# Column1 	Column2 	Column3


df.dropna(axis = 1)

# 	Column1
# Index1 	10.0
# Index2 	5.0
# Index3 	21.0

df.dropna(thresh = 2) # index eğer 2 den fazla nan varsa çıkart eşik değeri

# 	Column1 	Column2 	Column3
# Index1 	10.0 	20.0 	NaN
# Index3 	21.0 	NaN 	10.0


df.fillna(value = 1) # na ları 1 ile doldurduk

# 	Column1 	Column2 	Column3
# Index1 	10.0 	20.0 	1.0
# Index2 	5.0 	1.0 	1.0
# Index3 	21.0 	1.0 	10.0

df.sum() # sütünları toplar

# Column1    36.0
# Column2    20.0
# Column3    10.0
# dtype: float64

df.sum().sum() # 66.0

df.size #9


df.isnull().sum()

# Column1    0
# Column2    2
# Column3    2
# dtype: int64


df.isnull().sum().sum() # 4


def calculateMean(df):
    totalSum = df.sum().sum()
    totalNum = df.size - df.isnull().sum().sum()
    return totalSum / totalNum

df.fillna(value = calculateMean(df),inplace = True)

df

# 	Column1 	Column2 	Column3
# Index1 	10.0 	20.0 	13.2
# Index2 	5.0 	13.2 	13.2
# Index3 	21.0 	13.2 	10.0



#Groupby Operasyonu

dataset = {
    
    "Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
    "Maaş":[3000,3500,2500,4500,4000,2000],
    "Çalışan":["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"]
    
}


df = pd.DataFrame(dataset)



# 	    Departman 	Maaş 	Çalışan
# 0 	Bilişim 	3000 	Mustafa
# 1 	İnsan Kaynakları 	3500 	Jale
# 2 	Üretim 	2500 	Kadir
# 3 	Üretim 	4500 	Zeynep
# 4 	Bilişim 	4000 	Murat
# 5 	İnsan Kaynakları 	2000 	Ahmet

DepGroup = df.groupby("Departman")

DepGroup #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001D69880A310>

DepGroup.sum()

# 	            Maaş
# Departman 	
# Bilişim 	     7000
# Üretim 	         7000
# İnsan Kaynakları 5500


df.groupby("Departman").sum().loc["Bilişim"]

# Maaş    7000
# Name: Bilişim, dtype: int64

int(df.groupby("Departman").sum().loc["Bilişim"]) # 7000



df.groupby("Departman").count()

#  	Maaş 	Çalışan
# Departman 		
# Bilişim 	2 	2
# Üretim 	2 	2
# İnsan Kaynakları 	2 	2


df.groupby("Departman").max()
#Maaşlar o gruptaki max sayıyı ve ismi en son olan alfede en büyük ismi döner

# 	Maaş 	Çalışan
# Departman 		
# Bilişim 	4000 	Mustafa
# Üretim 	4500 	Zeynep
# İnsan Kaynakları 	3500 	Jale


df.groupby("Departman").min()

#  	Maaş 	Çalışan
# Departman 		
# Bilişim 	3000 	Murat
# Üretim 	2500 	Kadir
# İnsan Kaynakları 	2000 	Ahmet


df.groupby("Departman").min()["Maaş"]


# Departman
# Bilişim             3000
# Üretim              2500
# İnsan Kaynakları    2000
# Name: Maaş, dtype: int64


df.groupby("Departman").min()["Maaş"]["Bilişim"] #3000


df.groupby("Departman").mean() # ortalama bulur


# 	Maaş
# Departman 	
# Bilişim 	3500
# Üretim 	3500
# İnsan Kaynakları 	2750


df.groupby("Departman").mean()["Maaş"]["İnsan Kaynakları"] # 2750












