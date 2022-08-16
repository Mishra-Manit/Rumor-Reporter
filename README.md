# Rumor-Reporter
Rumor Reporter is an AI based web app that analyzes a text article inputted by the user to see if the article is real or fake. It also uses Sentiment Analysis to see whether the article is overall positive or negative. We also have loads of information about Fake News on our webpage, check it out!

## About 
Our inspiration comes from the thousands of people that are given false beliefs or misled by some fake news. I have heard stories on how people have seriously damaged their body from trying something that they later found out was fake. After hearing these horrific stories, I thought to myself “ how can i make sure this never happens again”

As we did more research on this topic we realized this issue is much more common than we thought. According to pew research, “only 35% of people have unknowingly shared fake news”. After reading about this, we wanted to make sure no one gets mislead and eventually hurt from fake news again.

Thus we developed Rumor Reporter, an AI-based program explicitly designed to prevent people from being misled or hurt from fake news 

##What it does
Rumor Reporter is a cutting-edge web tool that helps people from being misled or hurt from fake news. 

Rumor Reporter  utilizes a passive aggressive classifier and a tf-idf vectorizer, to identify major signs of fake news and displays all this information in a user-friendly interface. Along with detecting fake news, Rumor Reporter provides users with a sentiment analysis. Rumor Reporter returns if the text is positive, negative or neutral. With this tool users can know if the text is generally positive or negative.

##How we built it
We divided our tasks into two main groups after about an hour of planning and brainstorming. Nilay focused mostly on the project's user interface and design, while Manit worked primarily on the machine learning model and backend.

Python is the best language to utilize because of its applications in machine learning, which is why we choose it as our language of choice. Rumor Reporter uses scikitlearn because it is the lightweight backend web development library that has become synonymous with Python. This implies that when using Rumor Reporter , our users get a quick and simple experience. In order to make it simpler for our model to recognize fake news and prevent people from being mislead, we also utilized a tf-idf vectorizer to perform a sentiment analysis .

Additionally, to train our model and get it precise enough to meet our standards, we used thousands of different articles from different news sources around the world. This worked really well as we achieved a 99.5% accuracy on our model.

##Challenges we ran into 
We ran into some problems while trying to train our model to make it more accurate. Using many articles was really time consuming but we needed to do it to increase our model’s accuracy. After countless hours of training our model we finally reached the accuracy of 99.5%.

##Accomplishments that we are proud of 
We are really proud of ourselves for being able to design a project that would have the potential to significantly alter the lives of numerous individuals all over the world while still remaining distinctive. We are astounded at how much we were able to complete in such a short period of time and how well the final product came together.

##What we learned
Throughout the course of this project, our team gained a great deal of knowledge regarding web development and machine learning. We gained knowledge of libraries like scikit learn and found some intriguing brand-new features in Python such as the passive aggressive classifier. We discovered how to employ computer vision to address problems in our neighborhood and how to incorporate our fixes into engaging applications.

##What's Next
In the future for Rumor Reporter , we hope to develop a Mobile App so that you can check for fake news where ever you want. We also plan on adding more features to the program such as reporting the fake news article

## Why Us?
- Easy to Use
    - Our software automatically detects fake news articles using a AI to ensure precision

- Fast
    - All of our analysis is done in a matter of seconds, so you get your results immediately

- Custom Reports
    - When you are finished inputting your article, our app tells you if the article is fake or not, and it gives a sentiment analysis.


## Requirements
- Latest version of Google Chrome, Edge, or Firefox
- Latest version of Python installed
- Use pip to install [mediapipe](https://pypi.org/project/mediapipe/), [flask](https://pypi.org/project/Flask/), and many others. Check the imports on the "app.py" file to see which libraries you will have to install.
- pip is automatically installed on your PC as part of your Python installation. Simply type this into your terminal
    - ``` python3 -m pip install [LIRBARY TO INSTALL] ```
    
## Instructions to Use
1. Download all the files from this repository into a folder on your computer
2. Open your folder and run main.py
3. Now, go into your broswer and type 127.0.0.1:5000 into the search bar
4. You should now be able to access the Rumor Reporter site and use it as much as you want.
