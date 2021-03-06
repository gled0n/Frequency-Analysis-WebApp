import streamlit as st
import os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

st.markdown(
"""
# Recent Trends in Systems and Network Security
## Telecooperation Lab (TK) - TU Darmstadt - Sommersemester 2020
"""
)

def generategraph(yacm,yusenix,yieee,yndss,word):
    lx = []
    for x in range(2010,2020):
        lx.append(x)
    plt.xlabel('Years')
    plt.ylabel('Percentage (%)')
    plt.plot(lx, yacm, label="ACM")
    plt.plot(lx, yusenix, label="USENIX")
    plt.plot(lx, yieee, label="IEEE")
    plt.plot(lx, yndss, label="NDSS")
    
    tick_spacing = 1
    plt.xticks(np.arange(min(lx), max(lx)+1, 1.0))
    plt.grid()

    plt.title('Use of the given words throughout the years.')

    plt.legend()
    # Plot the frequency graph.
    st.pyplot()

def getvalues(inputstring):
    listofkeywords = []
    # Separate the keywords
    listofkeywordstemp = inputstring.split(";")
    for m in listofkeywordstemp:
        listofkeywords.append(m)
    # The table of the results
    df2 = pd.DataFrame(columns=['Conference', 'Title'])
    conferences = ["acm","usenix","ieee","ndss"]
    yacm = []
    yusenix = []
    yieee = []
    yndss= []
    for conference in conferences:
        for x in range(2010,2020):
            templist = []
            if(not os.path.isfile("dataset/" + conference + "-" + str(x) + ".csv")):
                continue
        # The number of publications per conference
            size = sum(1 for row in csv.DictReader(open("dataset/" + conference + "-" + str(x) + ".csv")))
            # Only IEEE has a keywords field.
            if(conference == "ieee"):
                confname = conference.upper() + " - " + str(x)
                # Count the publications which include at least one of the keywords
                momcount = 0
                for a in listofkeywords:
                    for row in csv.DictReader(open("dataset/" + conference + "-" + str(x) + ".csv")):
                        if a.upper() in row['keywords'].upper() and row['title'] not in templist:
                            momcount += 1
                            templist.append(row['title'])
                # Calculate the frequency
                frequency = (momcount/size)*100
                yieee.append(frequency)
                for title in templist:
                    toinsert = [confname, title,]
                    df2.loc[len(df2)] = toinsert
            else:
                confname = conference.upper() + " - " + str(x)
                # Count the publications which include at least one of the keywords
                momcount = 0
                for a in listofkeywords:
                    for row in csv.DictReader(open("dataset/" + conference + "-" + str(x) + ".csv")):
                        if a.upper() in row['abstract'].upper() and row['title'] not in templist:
                            momcount += 1
                            templist.append(row['title'])
                # Calculate the frequency
                frequency = (momcount/size)*100
                for title in templist:
                    toinsert = [confname, title,]
                    df2.loc[len(df2)] = toinsert
                if(conference == "acm"):
                    yacm.append(frequency)
                if(conference == "usenix"):
                    yusenix.append(frequency)
                if(conference == "ndss"):
                    yndss.append(frequency)
    # Generate the graph
    generategraph(yacm,yusenix,yieee,yndss,a)
    yacm = []
    yusenix = []
    yieee = []
    yndss= []
    return df2

keywords = st.text_input('Enter keyword')
if keywords:
    df = getvalues(keywords)
    st.table(df)
