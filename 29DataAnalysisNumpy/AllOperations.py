import numpy as np

#Numpy Arraylerin Temel Operasyonları


# arr1 = np.array([10,20,30,40,50,60])
# arr2 = np.array([2,3,4,5,6])

# arr1 + arr2
# # array([12, 23, 34, 45, 56, 67])

# arr1 - arr2
# # array([ 8, 17, 26, 35, 44, 53])

# arr1 * arr2
# array([ 20,  60, 120, 200, 300, 420])


# arr1 + 10
# array([20, 30, 40, 50, 60, 70])

# np.sqrt(arr1)
# array([3.16227766, 4.47213595, 5.47722558, 6.32455532, 7.07106781,7.74596669])



#Numpy Array Ypaısı Ve İşlemleri


#Numpy Arrayleri Oluşturma
arr = np.array([[10,20,30],[40,50,60,],[70,80,90]])
data_list2 = [[10,20,30],[40,50,60],[70,80,90]]
arr2 = np.array(data_list2)
arr2
# array([[10, 20, 30],
#        [40, 50, 60],
#        [70, 80, 90]])


arr3 = np.array([1,2,3,4,5])
arr3[4] #5
arr2[2,2] # 2.satır 2.sütun 90


#Arange Fonksiyonu
np.arange(0,100,3)

# array([ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48,
#        51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99])




#Zeros ve Ones Fonksiyonları
np.zeros(10)

# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

np.ones(10)

# array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])


np.zeros((3,4))

# array([[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]])

np.ones((3,5))

# array([[1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.]])



#Linspace Fonksiyonu

np.linspace(0,100,5)

# array([  0.,  25.,  50.,  75., 100.])

np.linspace(0,1,6)

# array([0. , 0.2, 0.4, 0.6, 0.8, 1. ])



#Eye Fonksiyonu

np.eye(6)

# array([[1., 0., 0., 0., 0., 0.],
#        [0., 1., 0., 0., 0., 0.],
#        [0., 0., 1., 0., 0., 0.],
#        [0., 0., 0., 1., 0., 0.],
#        [0., 0., 0., 0., 1., 0.],
#        [0., 0., 0., 0., 0., 1.]])


#Random Randn Randint Rand Fonksiyonları

np.random.randint(15) # 0 ile 15  15 dahil değil
np.random.randint(0,10) # 0 ile 10 10 dahil değil
np.random.randint(1,10,5) # 1 dahil 10 değil 5 sayı array yap
# array([8, 9, 5, 9, 9])



np.random.rand(5)
# array([0.00138603, 0.50002514, 0.2056032 , 0.49300374, 0.7897421 ])

np.random.randn(5)
# array([ 1.51673567, -1.56595834, -0.64582724, -0.70464953,  0.41237665])



#Reshape Fonksiyonu

arr = np.arange(25)

# arr

# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
#        17, 18, 19, 20, 21, 22, 23, 24])


arr.reshape(5,5)

# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14],
#        [15, 16, 17, 18, 19],
#        [20, 21, 22, 23, 24]])


# Max Min Sum Mean Argmax Argmin Fonksiyonları


newArray = np.random.randint(1,100,10)

newArray

# array([52, 44,  2, 67, 49, 12, 47,  2, 17, 80])

newArray.max()#80
newArray.min()#2
newArray.sum()#372
newArray.mean()#37.2 ortalama bulur
newArray.argmax() # 9 max olan elemanın indeks döner
newArray.argmin() # 2 min olan elemanın indeks döner



#Linalg.det Determinant Hesabı

detArray = np.random.randint(1,100,25)
# array([15, 69, 37, 79, 99, 46, 38, 40, 21, 91, 24, 82, 96, 97, 57, 37,  9,
#        75, 54, 19, 48, 45, 85, 38, 24]

detArray = detArray.reshape(5,5)

# array([[15, 69, 37, 79, 99],
#        [46, 38, 40, 21, 91],
#        [24, 82, 96, 97, 57],
#        [37,  9, 75, 54, 19],
#        [48, 45, 85, 38, 24]])


np.linalg.det(detArray)# 176725776.0

round(np.linalg.det(detArray)) #-2



# Numpy Arraylerin Parçalanması Ve İndekslenmesi

arr = np.arange(1,10)

arr[3]#4

arr[1:5] # array([2, 3, 4, 5])

arr[::-1] # array([9, 8, 7, 6, 5, 4, 3, 2, 1])



arr[:3] = 25 # array([25, 25, 25,  4,  5,  6,  7,  8,  9])



arr2 = arr



arr2[:3] = 100

# arr2 array([100, 100, 100,   4,   5,   6,   7,   8,   9])

# arr array([100, 100, 100,   4,   5,   6,   7,   8,   9])

#Referans tipyle kayıt ediliyor


# arr2 = arr.copy() referans tipiyle kayıt etmek istemezsek böyle oluşturabiliriz



#Matris İndeksleme


newArray = np.arange(1,21)

# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12],
#        [13, 14, 15, 16],
#        [17, 18, 19, 20]])


newArray[0,0]#1


newArray[:,:2]

# array([[ 1,  2],
#        [ 5,  6],
#        [ 9, 10],
#        [13, 14],
#        [17, 18]]


newArray[:3,:3]

# array([[ 1,  2,  3],
#        [ 5,  6,  7],
#        [ 9, 10, 11]])

newArray[:2,:]

# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])

newArray[:2]

# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])



#Boolean Array Oluşturmak

arr = np.arange(1,11) # array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

arr > 3

# array([False, False, False,  True,  True,  True,  True,  True,  True,
#         True])


booleanArray = arr > 3
# array([False, False, False,  True,  True,  True,  True,  True,  True,
#         True])


arr[booleanArray] # false olanlar bastırılmaz

# array([ 4,  5,  6,  7,  8,  9, 10]



arr[arr >5 ]

# array([ 6,  7,  8,  9, 10])


booleanArray

# array([False, False, False,  True,  True,  True,  True,  True,  True,
#         True])