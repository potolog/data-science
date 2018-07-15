
# coding: utf-8

# In[ ]:


## pandas 기본
#### 1.1 Series 객체 생성
#### 1.2 DataFrame 객체 생성
#### 1.3 DataFrame 인덱싱
#### 1.4 null 데이터 처리
#### 1.5 수학함수, Sorting


# In[3]:


import numpy as np
import pandas as pd


# In[4]:


print(np.__version__)
print(pd.__version__)


# ### 1.1 Series 객체 생성`

# In[8]:


# Series 객체 생성
ser1 = pd.Series([4, 7, -5, 3])
print(ser1, type(ser1))


# In[10]:


print(ser1.values)
print(ser1.index)
print(ser1.dtypes)


# In[11]:


# Series 객체를 생성 : index 값을 지정
ser2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(ser2, type(ser2))


# In[13]:


# Series 객체를 생성 : dict 타입
mydict = {
    '철수':5000,
    '영희':3000,
    '둘리':1000,
    }
print(mydict)

ser3 = pd.Series(mydict)
print(ser3)


# In[16]:


# index명과 컬럼명을 지정
ser3.name = '급여'
ser3.index.name = '이름'
print(ser3)


# ### 1.2 DataFrame 객체 생성

# In[17]:


mydict = {
    'names': ['철수', '영희', '둘리', '철수', '로그'],
    'year': [2017, 2018, 2016, 2015, 2018],
    'points': [1.5, 2.0, 3.0, 4.5, 5.8],
}
print(mydict)


# In[24]:


# dict 를 이용한 DataFrame 객체 생성
df1 = pd.DataFrame(mydict)
df1
# print(df1)


# In[28]:


# DataFrame 생성시 컴럼 순서 지정
df2 = pd.DataFrame(mydict, columns=['names', 'points', 'year'])
print(type(df2))
df2


# In[32]:


# DataFrame 크기, 컬럼명, 인덱스
print(df2.shape)
print(df2.columns)
print(df2.index)


# In[35]:


# DataFrame 의 값만 확인
print(df2.values)


# In[34]:


# info() : 컬럼 dtype, not null row 건수 등 확인
print(df2.info())


# In[33]:


# describe() : 숫자타입인 컬럼들의 집계함수
print(df2.describe())


# In[39]:


print(type(df2['names']))
df2.names


# ### 1.3 DataFrame 인덱싱

# ### 1.4 null 데이터 처리

# ### 1.5 수학함수, Sorting
