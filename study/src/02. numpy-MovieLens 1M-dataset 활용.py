
# coding: utf-8

# ### numpy를 사용한 데이터 분석 맛보기

# In[1]:


import numpy as np


# In[2]:


# 파일 읽기
# 1컬럼 : user id : 1 ~ 6040
# 2컬럼 : 영화 id : 1 ~ 3592
# 3컬럼 : 영화평점 : 1 ~ 5
# 4컬럼 : 타임스탬프
# 5컬럼 : 
data = np.loadtxt("data/movielens-1m/ratings.dat", delimiter="::", dtype=np.int64)
print(data)


# In[3]:


# 맨 앞의 5행의 데이터만 보기
data[:5, :]


# In[4]:


# 영화평점 컴럼만 선택
print("영화평점 : ", data[:, 2])

# 전체 평점의 평균 구하기
print('평점 평균 : ', data[:, 2].mean())
print('평점의 고유값 : ', np.unique(data[:, 2]))


# In[5]:


# unique 한 user id 값 출력하기
user_ids = np.unique(data[:, 0])
print('user ids : ', user_ids)
print('user ids shape: ', user_ids.shape)


# In[6]:


# 각 사용자별(user id) 평점(rating)의 평균 구하기
user_ids = np.unique(data[:, 0])   # unique 한 User ID 가져 오기
mean_rating_by_user_list = []      # user id 와 평점을 저장할 배열 선언
for user_id in user_ids:
    data_for_user = data[data[:, 0] == user_id, :]  # data[:, 0] == user_id 인 row 만 추출
    mean_rating_for_user = data_for_user[:, 2].mean()  # 평점의 평균을 구하여 저장
    mean_rating_by_user_list.append([user_id, mean_rating_for_user])  # userid 와 평균 저장


# In[7]:


# 각 사용자별(user id) 평점(rating)의 평균 구하기

#user_ids = np.unique(data[:, 0])[0:2]   # unique 한 User ID 중에서 첫번째, 두번째 id 가져 오기
#mean_rating_by_user_list = []      # user id 와 평점을 저장할 배열 선언
#for user_id in user_ids:
#    data_for_user = data[data[:, 0] == user_id, :]  # data[:, 0] == user_id 인 row 만 추출
#    print(data_for_user)
#    print('////')
#    mean_rating_for_user = data_for_user[:, 2].mean()  # 평점의 평균을 구하여 저장
#    print(user_id, mean_rating_for_user)
#    mean_rating_by_user_list.append([user_id, mean_rating_for_user])  # userid 와 평균 저장


# In[8]:


# List를 numpy array 로 변환
mean_rating_by_user_array = np.array(mean_rating_by_user_list, dtype=np.float32)
mean_rating_by_user_array


# In[10]:


# numpy array를 파일로 저장
print(mean_rating_by_user_array.shape)
np.savetxt("mean_rating_by_user.csv", mean_rating_by_user_array, fmt='%.3f', delimiter=',')

