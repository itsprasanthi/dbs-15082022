#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, render_template, request


# In[4]:


app = Flask(__name__) 


# In[5]:


dir(app)


# In[6]:


#Decorator: Run the programme before the actual programme


# In[7]:


import joblib

@app.route("/", methods = ["GET","POST"]) #When there are multiple items in an array, use a square bracket
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression_DBS")
        r1 = model1. predict([[rates]])
        model2 = joblib.load("tree_DBS")
        r2 = model2. predict([[rates]])
        #When taking stuff from backend, you must cast the data structure. Don't simply let it be as it is
        return(render_template("index.html", result1=r1, result2=r2)) #DON'T double click the html to run it. The flask must run the html
    else:
        return(render_template("index.html", result1="waiting", result2="waiting"))


# In[ ]:


if __name__ == "__main__": 
    app.run(host="127.0.0.1", port=int("80"))


# In[ ]:


#If this programme is yours, then run. If not, don't run


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




