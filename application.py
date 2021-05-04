from flask import Flask, render_template, Response, request, redirect, url_for,jsonify
import pickle
import difflib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
import base64
from io import BytesIO
from flask import Flask
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#from matplotlib.figure import Figure
#import matplotlib.pyplot as plt
import numpy as np
import os
import random
from flask import Response
import io

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

model = pickle.load(open('./model/book_model.pkl','rb'))

df2 = pd.read_csv('./model/Book1.csv')

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['Desc'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['title'])
all_titles = [df2['title'][i] for i in range(len(df2['title']))]

def get_recommendations(title):
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    book_indices = [i[0] for i in sim_scores]
    titl = df2['title'].iloc[book_indices]
    dat = df2['original_publication_year'].iloc[book_indices]
    descp = df2['Desc'].iloc[book_indices]
    atr  = df2['authors'].iloc[book_indices]
    dwnl = df2['pdf'].iloc[book_indices]
    return_df = pd.DataFrame(columns=['Title','Year','Description','Authors','Download'])
    return_df['Title'] = titl
    return_df['Year'] = dat
    return_df['Description'] = descp
    return_df['Authors'] = atr
    return_df['Download'] = dwnl
    return return_df

def get_auto():
    books_corr_auto = pd.DataFrame(['Autobiography'],index=np.arange(1), columns=['Genre'])
    corr_books1 = pd.merge(books_corr_auto, df2, on='Genre')

# for i in corr_books1['image_url']:
#     response = requests.get(i)
#     img = Image.open(BytesIO(response.content))
#     plt.figure()
#     print(plt.imshow(img))
#     plt.savefig('/static/images/new_plot.png')
    popularity_threshold = 3
    genre_book1= corr_books1.query('rating >= @popularity_threshold')
    titl = genre_book1['title']
    rat = genre_book1['rating']
    descp = genre_book1['Desc']
    atr  = genre_book1['authors']
    dwnl = genre_book1['pdf']
    return_auto = pd.DataFrame(columns=['Title','Rating','Description','Authors','Download'])
    return_auto['Title'] = titl
    return_auto['Rating'] = rat
    return_auto['Description'] = descp
    return_auto['Authors'] = atr
    return_auto['Download'] = dwnl
    return return_auto

# CLASSICS

def get_class():
    books_corr_class = pd.DataFrame(['Classics'], 
                                  index=np.arange(1), columns=['Genre'])
    corr_books2 = pd.merge(books_corr_class, df2, on='Genre')
# def ima():
#     for i in corr_books2['image_url']:
#         response = requests.get(i)
#         img = Image.open(BytesIO(response.content))
#         plt.figure()
#         print(plt.imshow(img))

    popularity_threshold = 4
    genre_book2= corr_books2.query('rating >= @popularity_threshold')
    titl = genre_book2['title']
    rat = genre_book2['rating']
    descp = genre_book2['Desc']
    atr  = genre_book2['authors']
    dwnl = genre_book2['pdf']
    return_class = pd.DataFrame(columns=['Title','Rating','Description','Authors','Download'])
    return_class['Title'] = titl
    return_class['Rating'] = rat
    return_class['Description'] = descp
    return_class['Authors'] = atr
    return_class['Download'] = dwnl
    return return_class

#FICTION

def get_fict():
    books_corr_fict = pd.DataFrame(['Fiction'], 
                                  index=np.arange(1), columns=['Genre'])
    corr_books3 = pd.merge(books_corr_fict, df2, on='Genre')
# def ima():
#     for i in corr_books3['image_url']:
#         response = requests.get(i)
#         img = Image.open(BytesIO(response.content))
#         plt.figure()
#         print(plt.imshow(img))

    popularity_threshold = 4
    genre_book3= corr_books3.query('rating >= @popularity_threshold')
    titl = genre_book3['title']
    rat = genre_book3['rating']
    descp = genre_book3['Desc']
    atr  = genre_book3['authors']
    dwnl = genre_book3['pdf']
    return_fict = pd.DataFrame(columns=['Title','Rating','Description','Authors','Download'])
    return_fict['Title'] = titl
    return_fict['Rating'] = rat
    return_fict['Description'] = descp
    return_fict['Authors'] = atr
    return_fict['Download'] = dwnl
    return return_fict

#MYSTERY

def get_myst():
    books_corr_myst = pd.DataFrame(['Mystery'], 
                                  index=np.arange(1), columns=['Genre'])
    corr_books4 = pd.merge(books_corr_myst, df2, on='Genre')
# def ima():
#     for i in corr_books3['image_url']:
#         response = requests.get(i)
#         img = Image.open(BytesIO(response.content))
#         plt.figure()
#         print(plt.imshow(img))

    popularity_threshold = 3
    genre_book4= corr_books4.query('rating >= @popularity_threshold')
    titl = genre_book4['title']
    rat = genre_book4['rating']
    descp = genre_book4['Desc']
    atr  = genre_book4['authors']
    dwnl = genre_book4['pdf']
    return_myst = pd.DataFrame(columns=['Title','Rating','Description','Authors','Download'])
    return_myst['Title'] = titl
    return_myst['Rating'] = rat
    return_myst['Description'] = descp
    return_myst['Authors'] = atr
    return_myst['Download'] = dwnl
    return return_myst

#TECHNICAL
def get_tech():
    books_corr_tech = pd.DataFrame(['technical'], 
                                  index=np.arange(1), columns=['Genre'])
    corr_books5 = pd.merge(books_corr_tech, df2, on='Genre')
# def ima():
#     for i in corr_books3['image_url']:
#         response = requests.get(i)
#         img = Image.open(BytesIO(response.content))
#         plt.figure()
#         print(plt.imshow(img))

    popularity_threshold = 3
    genre_book5= corr_books5.query('rating >= @popularity_threshold')
    titl = genre_book5['title']
    rat = genre_book5['rating']
    descp = genre_book5['Desc']
    atr  = genre_book5['authors']
    dwnl = genre_book5['pdf']
    return_tech = pd.DataFrame(columns=['Title','Rating','Description','Authors','Download'])
    return_tech['Title'] = titl
    return_tech['Rating'] = rat
    return_tech['Description'] = descp
    return_tech['Authors'] = atr
    return_tech['Download'] = dwnl
    return return_tech

bg_img = os.path.join('static', 'images')
app.config['up_img'] = bg_img

# txt=genre_book1[['title']].to_string(index=False),rat=genre_book1[['rating']].to_string(index=False),dsc=corr_books1[['Desc']].to_string(index=False),authr=corr_books1[['authors']].to_string(index=False),
#                 dw=corr_books1[['pdf']].to_string(index=False),
@app.route('/genre',methods=['POST', 'GET'])
def genre():
    
    auto_filename = os.path.join(app.config['up_img'], 'autobiography.png')
    class_filename = os.path.join(app.config['up_img'], 'classics.jpg')
    fict_filename = os.path.join(app.config['up_img'], 'fiction.jpg')
    myst_filename = os.path.join(app.config['up_img'], 'mystery.jpeg')
    tech_filename = os.path.join(app.config['up_img'], 'technical.jpg')

    if request.method == 'POST':
        if 'aut' in request.form:
            result_final = get_auto()
            names = []
            rating = []
            desc = []
            author = []
            file = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                rating.append(result_final.iloc[i][1])
                desc.append(result_final.iloc[i][2])
                author.append(result_final.iloc[i][3])
                file.append(result_final.iloc[i][4])
            return render_template('autobio.html',book_names=names,book_rating=rating,book_desc=desc,book_author=author,book_file=file,
                user_image = auto_filename,search_name='Autobiography')
        if 'cls' in request.form:
            result_final = get_class()
            names = []
            rating = []
            desc = []
            author = []
            file = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                rating.append(result_final.iloc[i][1])
                desc.append(result_final.iloc[i][2])
                author.append(result_final.iloc[i][3])
                file.append(result_final.iloc[i][4])
            return render_template('classics.html',book_names=names,book_rating=rating,book_desc=desc,book_author=author,book_file=file,
                user_image = class_filename,search_name='Classics')
        if 'fi' in request.form:
            result_final = get_fict()
            names = []
            rating = []
            desc = []
            author = []
            file = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                rating.append(result_final.iloc[i][1])
                desc.append(result_final.iloc[i][2])
                author.append(result_final.iloc[i][3])
                file.append(result_final.iloc[i][4])
            return render_template('fiction.html',book_names=names,book_rating=rating,book_desc=desc,book_author=author,book_file=file,
                user_image = fict_filename,search_name='Fiction')
        if 'ms' in request.form:
            result_final = get_myst()
            names = []
            rating = []
            desc = []
            author = []
            file = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                rating.append(result_final.iloc[i][1])
                desc.append(result_final.iloc[i][2])
                author.append(result_final.iloc[i][3])
                file.append(result_final.iloc[i][4])
            return render_template('Mystery.html',book_names=names,book_rating=rating,book_desc=desc,book_author=author,book_file=file,
                user_image = myst_filename,search_name='Mystery')
        if 'tc' in request.form:
            result_final = get_tech()
            names = []
            rating = []
            desc = []
            author = []
            file = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                rating.append(result_final.iloc[i][1])
                desc.append(result_final.iloc[i][2])
                author.append(result_final.iloc[i][3])
                file.append(result_final.iloc[i][4])
            return render_template('technical.html',book_names=names,book_rating=rating,book_desc=desc,book_author=author,book_file=file,
                user_image = tech_filename,search_name='Technical')                    


@app.route('/search', methods=['GET', 'POST'])

def search():
    if request.method == 'GET':
        return(render_template('home.html'))
            
    if request.method == 'POST':
        m_name = request.form['book_name']
        m_name = m_name.title()
#        check = difflib.get_close_matches(m_name,all_titles,cutout=0.50,n=1)
        if m_name not in all_titles:
            return(render_template('negative.html',name=m_name))
        else:
            result_final = get_recommendations(m_name)
            names = []
            dates = []
            desc = []
            author = []
            file = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                dates.append(result_final.iloc[i][1])
                desc.append(result_final.iloc[i][2])
                author.append(result_final.iloc[i][3])
                file.append(result_final.iloc[i][4])

            return render_template('positive.html',book_names=names,book_date=dates,book_desc=desc,book_author=author,book_file=file,search_name=m_name)

            
if __name__ == "__main__":
    app.run(debug=True)
