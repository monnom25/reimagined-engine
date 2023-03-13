#!/usr/bin/env python
# coding: utf-8

# In[2]:


from IPython.core.display import display, HTML
display(HTML(
"""<style>
div.CodeMirror {font-family: Consolas; font-size: 15pt;}
</style>
"""))


# In[3]:


삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)


# In[4]:


시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))


# In[5]:


s = "hello"
t = "python"
print(s+"!",t)


# In[6]:


print(2 + 2* 3)


# In[7]:


a = 128
print(type(a))

a = "132"
print(type(a))


# In[8]:


num_str = "720"
num_int = int(num_str)
print(num_int+1, type(num_int))


# In[9]:


num = 100
result = str(num)
print(result, type(result))


# In[12]:


data = "15.79"
data = float(data)
print(data, type(data))


# In[11]:


year = "2020"
print(int(year)-3)  # 2017
print(int(year)-2)  # 2018
print(int(year)-1)  # 2019


# In[10]:


월 = 48584
총금액 = 월 * 36
print(총금액)


# In[ ]:


lang = 'python'
print(lang[0], lang[2])


# In[13]:


license_plate = "24가 2210"
print(license_plate[-4:])


# In[ ]:


string = "홀짝홀짝홀짝"
print(string[::2])


# In[ ]:


string = "PYTHON"
print(string[::-1])


# In[ ]:


phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)


# In[ ]:


phone_number = "010-1111-2222"
phone_number1 = phone_number.replace('-', '')
print(phone_number1)


# In[ ]:


url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])


# In[14]:


string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)


# In[15]:


a = "3"
b = "4"
print(a + b)


# In[ ]:


print("Hi" * 3)


# In[ ]:


print("-" * 80)


# In[16]:


t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)


# In[ ]:


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))


# In[ ]:


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))


# In[ ]:


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")


# In[17]:


상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))


# In[18]:


분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])


# In[19]:


data = "   삼성전자    "
data1 = data.strip()
print(data1)


# In[ ]:





# In[ ]:




