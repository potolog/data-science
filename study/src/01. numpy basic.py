
# coding: utf-8

# ## numpy 기본 사용
# ### 1.1 numpy array 생성
# ### 1.2 numpy의 수학함수 사용

# In[1]:


import numpy as np


# In[2]:


data = [6, 7.5, 9, 0, 10]
print(type(data))


# In[3]:


data


# ### numpy array

# In[4]:


# array 의 데이터형
arr = np.array(data)


# In[5]:


# array 생성
arr = np.array(data)
print(arr.shape)
arr


# In[6]:


# 모든 값이 1인 배열 생성
np.ones(10)


# In[7]:


# 대각선의 원소가 모두 1이고, 나머지는 0인 정사각 배열 생성
np.eye(4)


# In[8]:


# range 함수와 유사한 arange(start, stop, step, dtype=None)
data = np.arange(15)
print(data)
data = np.arange(11, 20)
print(data)
data = np.arange(2, 10.0, 2.5)
print(data)


# In[9]:


# 모든 값이 특정 상수인 배열 생성
np.full((3, 5), 7)


# In[10]:


# 랜덤한 실수형 값을 생성해주는 배열
np.random.random((3, 4))


# ### numpy array 형변환

# In[11]:


arr3 = np.array([1, 2, 3, 4, 5], dtype=np.int64)
arr3


# In[12]:


# int64 를 flot64 형변환
float_arr = arr3.astype(np.float64)
print(float_arr)
print(float_arr.dtype)


# In[13]:


# array 상에서 중복값을 제외한 unique 한 값 추출하기
names = np.array(["Charles", "Soyul", "Hayoung", "Charles", "Hayoung", "Soyul", "Soyul"])
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print("names =", names)


# In[14]:


# 이름에서 중복된 값을 제거함
np.unique(names)


# In[15]:


# 숫자에서 중복된 값을 제거함
np.unique(ints)


# ### array 계산

# In[16]:


arr1 = np.array([[1,2,3], [4,5,6]])
arr2 = np.array([[7,8,9], [10,11,12]])


# In[17]:


print(arr1 - arr2)


# In[18]:


print(arr1 * 3)


# In[19]:


arr1.sum()


# In[20]:


# 컬럼별로 sum
arr1.sum(axis=0)


# In[21]:


# 행별로 sum
arr1.sum(axis=1)


# In[22]:


### array 형태 변형하기
sap = np.array(['MMM', 'ABT', 'ABBT', 'ACN', 'ACE', 'ATVI', 'ADBE', 'ADT'])

# 대상 배열의 모양을 바꾼다. reshape() 함수의 파라미터로 배열의 새 차원을 정의할 수 있다.
sap2d = sap.reshape(2, 4)
sap2d


# In[23]:


# 2차원 배열에서는 행과 열이 뒤바뀐다.
sap2d.T


# In[24]:


# 3차원 array 생성
sap.reshape(2, 2, 2)


# ## array 인덱싱

# In[25]:


# 1차원 배열의 인덱싱
arr1d = np.arange(1,17)
print(arr1d)       # 전체
print(arr1d[5])    # 특정 선택
print(arr1d[5:8])  # 부분 선택
print(arr1d[:])    # 전체 선택


# In[26]:


# 2차원 배열의 인덱싱
arr2d = arr1d.reshape(4,4)
print("arr2d = ", arr2d)
print(arr2d[1,3])  # 2행 4열
print(arr2d[1:3, :])  # 1:2행 전체열
print(arr2d[:, 1:3])  # 전체행, 1:3열


# ### 정수 인덱싱과 슬라이싱을 비교

# In[27]:


arr2d = np.arange(1, 17).reshape(4,4)
arr2d


# In[28]:


# 두번째 행을 1차원 배열로 (정수 인덱싱과 슬라이싱 혼합 사용)
row_r1 = arr2d[1, :]
print(row_r1, row_r1.shape)

# 두번째 행을 2차원 배열로 (슬라이싱만 사용)
row_r2 = arr2d[1:2, :]
print(row_r2, row_r2.shape)


# In[29]:


# 두번째 열을 1차원 배열로 (정수 인덱싱과 슬라이싱 혼합 사용)
col_r1 = arr2d[:, 1]
print(col_r1, col_r1.shape)

# 두번째 열을 2차원 배열로 (슬라이싱만 사용)
col_r2 = arr2d[:, 1:2]
print(col_r2, col_r2.shape)


# ### Boolean 인덱싱

# In[30]:


names = np.array(['자바', '파이썬', '스칼라', '자바', '코트린', '파이썬', '파이썬'])
print(names)
print(names == '자바')


# In[31]:


# ascending sort
print(np.sort(names))

# descending sort
print(np.sort(names)[::-1])

# unique 한 값만 출력
print(np.unique(names))


# In[32]:


# array 값 중에서 '자바' 인 것을 확인
names == '자바'


# In[33]:


# 0 ~ 7 까지의 랜덤한 정수형 숫자 배열 생성
numbers = np.random.randint(8, size=(7,4))
numbers


# In[34]:


numbers[names == '자바']


# In[35]:


# or 조건식
print(names)
print((names == '자바') | (names == '파이썬'))
print(numbers[(names == '자바') | (names == '파이썬')])

flag = (names == '자바') | (names == '파이썬')
print(numbers[flag])


# In[38]:


# 2차원 배열 열 방향으로 sort 하기
print(np.sort(numbers, axis=0))


# In[39]:


# 2차원 배열 행 방향으로 sort 하기
print(np.sort(numbers, axis=1))


# In[45]:


print(numbers)

# 4열의 데이터를 가져옴
print(numbers[:, 3])

# 4열의 데이터 중에서 3보다 작은 것은
print(numbers[:, 3] < 3)

# 4열의 데이터 중에서 3보다 작은 조건을 만족하는 행의 모든 컬럼을 가져오기
print(numbers[numbers[:, 3] < 3, :])

# 4열의 데이터 중에서 3보다 작은 조건을 만족하는 행의 2,3번째 컬럼을 가져오기
print(numbers[numbers[:, 3] < 3, 1:3])

