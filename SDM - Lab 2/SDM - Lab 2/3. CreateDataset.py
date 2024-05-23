#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pandas as pd
import datetime
import random
import numpy as np
random.seed(10)


# In[2]:


with open('data/dataset.json', encoding='utf-8') as inputfile:
    df = json.load(inputfile)
inputfile.close()


# In[3]:


df[1]


# In[4]:


conferences = []
conferenceUrls = []

journals = []
journalUrls = []

authors = []
authorUrls = []

domains = []

for i in range(len(df)):
    details = df[i]['_data']  
    if details['publicationVenue']:
        if 'type' in details['publicationVenue']:
            if details['publicationVenue']['type'] == 'journal':
                jName = details['publicationVenue']['name']
                myId = details['publicationVenue']['id']
                if jName not in journals:
                    journals.append(jName)
                    journalUrls.append(myId)
            elif details['publicationVenue']['type'] == 'conference':
                cName = details['publicationVenue']['name']
                myId = details['publicationVenue']['id']
                if cName not in conferences:
                    conferences.append(cName)
                    conferenceUrls.append(myId)
    if details['authors']:
        for i in range(len(details['authors'])):
            aName = details['authors'][i]['name']
            myId = details['authors'][i]['authorId']
            if aName not in authors:
                authors.append(aName)
                authorUrls.append(str(myId))
    if details['fieldsOfStudy']:
        for i in details['fieldsOfStudy']:
            if i not in domains:
                domains.append(i)


# ## Proceedings

# In[5]:


proceedingChoices = []

ids = []
for i in range(len(conferences)):
    ids.append('cp'+str(i))
    
    proceedingChoices.append('proceeding' + str(i))
        
proceedingsDF = pd.DataFrame(ids, columns = ['proceedingId'])
proceedingsDF['proceedingName'] = proceedingChoices

proceedingsDF.to_csv('data/proceedings.csv',index = False, header = True, mode = 'w')


# In[6]:


proceedingsDF.head()


# ## Conferences

# In[7]:


ids = []

for i in range(len(conferences)):
    ids.append('c'+str(i))

conferencesDF = pd.DataFrame(ids, columns = ['conferenceId'])


# In[8]:


cTypes = ['workshop','mainConference']

conferenceTypes = []
conferenceTypes = random.choices(cTypes, weights=[0.5,0.5], k=len(conferencesDF))


# In[9]:


cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

conferenceCity = np.random.choice(cities, size=len(conferencesDF))


# In[10]:


conferenceYear = np.random.randint(2020, 2023 + 1, size=len(conferencesDF))


# In[11]:


conferencesDF['conferenceUrl'] = conferenceUrls
conferencesDF['conferenceTitle'] = conferences
conferencesDF['conferenceType'] = conferenceTypes
conferencesDF['conferenceCity'] = conferenceCity
conferencesDF['conferenceYear'] = conferenceYear

conferencesDF['conferenceProceedingIds'] = proceedingsDF['proceedingId']
conferencesDF.to_csv('data/conferences.csv',index = False, header = True, mode = 'w')


# In[12]:


conferencesDF.head()


# ## ConferenceProceedings

# In[13]:


conferenceProceedingsDF = conferencesDF.merge(
    proceedingsDF,
    how = 'inner',
    left_on = ['conferenceProceedingIds'],
    right_on = ['proceedingId']
    ).drop(columns = ['proceedingId'], axis = 1)

conferenceProceedingsDF.to_csv('data/conferenceProceedings.csv',index = False, header = True, mode = 'w')


# In[14]:


conferenceProceedingsDF.head()


# ## Volumes

# In[15]:


volumeChoices = []
volumeYears = []

ids = []
for i in range(len(journals)):
    ids.append('jv'+str(i))
    
    volumeChoices.append('journal' + str(i))
    volumeYears.append(np.random.randint(2020, 2023 + 1))
        
volumesDF = pd.DataFrame(ids, columns = ['volumeId'])
volumesDF['volumeName'] = volumeChoices
volumesDF['volumeYear'] = volumeYears
volumesDF.to_csv('data/volumes.csv',index = False, header = True, mode = 'w')


# In[16]:


volumesDF.head()


# ## Journals

# In[17]:


ids = []
volumes = []

for i in range(len(journals)):
    ids.append('j'+str(i))

journalsDF = pd.DataFrame(ids, columns = ['journalId'])
journalsDF['journalUrl'] = journalUrls
journalsDF['journalTitle'] = journals

journalsDF['journalVolumeIds'] = volumesDF['volumeId']

journalsDF.to_csv('data/journals.csv',index = False, header = True, mode = 'w')


# In[18]:


journalsDF.head()


# ## JournalVolumes

# In[19]:


journalVolumesDF = journalsDF.merge(
    volumesDF,
    how = 'inner',
    left_on = ['journalVolumeIds'],
    right_on = ['volumeId']
    ).drop(columns = ['volumeId'], axis = 1)
journalVolumesDF.to_csv('data/journalVolumes.csv',index = False, header = True, mode = 'w')


# In[20]:


journalVolumesDF.head()


# ## Authors

# In[21]:


ids = []
for i in range(len(authors)):
    ids.append('a'+str(i))

authorsDF = pd.DataFrame(ids, columns = ['authorId'])
authorsDF['authorUrl'] = authorUrls
authorsDF['authorName'] = authors
authorsDF.to_csv('data/authors.csv',index = False, header = True, mode = 'w')


# In[22]:


authorsDF.head()


# ## Domains

# In[23]:


ids = []
for i in range(len(domains)):
    ids.append('d'+str(i))

domainDF = pd.DataFrame(ids, columns = ['domainId'])
domainDF['domainName'] = domains
domainDF.to_csv('data/domain.csv',index = False, header = True, mode = 'w')


# In[24]:


domainDF.head()


# ## Papers

# In[25]:


papers = []

paperUrlNum = 0

for i in range(len(df)):
    paperCurr = [] 
    details = df[i]['_data']
    
    currPaperUrlNum = 'p'+str(paperUrlNum)
    paperCurr.append(currPaperUrlNum)
    paperCurr.append(details['paperId'])
    
    if details['publicationVenue']:
        if 'type' in details['publicationVenue']:
            if details['publicationVenue']['type'] == 'journal':
                jName = details['publicationVenue']['name']
                paperCurr.append(journalsDF[journalsDF['journalTitle'] == jName]['journalId'].values[0])
                paperCurr.append(jName)
            elif details['publicationVenue']['type'] == 'conference':
                cName = details['publicationVenue']['name']
                paperCurr.append(conferencesDF[conferencesDF['conferenceTitle'] == cName]['conferenceId'].values[0])
                paperCurr.append(cName)

            else:
                paperCurr.append('None')
                paperCurr.append('None')
        else:
            paperCurr.append('None')
            paperCurr.append('None')
    else:
        paperCurr.append('None') # conferenceJournalUrl
        paperCurr.append('None') # conferenceJournal
    
    paperCurr.append(details['title'])
    paperCurr.append(details['abstract'])
    paperUrlNum += 1
    papers.append(paperCurr)


# In[26]:


paperColumns = ['paperId','paperUrl','conferenceJournalId','conferenceJournalTitle','paperTitle','paperAbstract']

papersDF = pd.DataFrame(papers, columns = paperColumns)


# In[27]:


paperTypes = []

for index, row in papersDF.iterrows():
    if row['conferenceJournalId'] == 'None':
        paperTypes.append('poster')
    else:
        paperTypes.append('fullPaper')
papersDF['paperType'] = paperTypes


# In[28]:


papersDF['conferenceJournalId'] = papersDF.apply(lambda x: random.choice(conferencesDF.conferenceId) if x['paperType'] == 'poster' else x['conferenceJournalId'], axis = 1)
papersDF['conferenceJournalTitle'] = papersDF.apply(lambda x: conferencesDF[conferencesDF['conferenceId'] == x['conferenceJournalId']]['conferenceTitle'].item() if x['paperType'] == 'poster' else x['conferenceJournalTitle'], axis = 1)


# In[29]:


procVols = []
for k in range(len(papersDF['paperId'])):
    currConfJourId = papersDF['conferenceJournalId'][k]
    if currConfJourId[0] == 'c':
        getProcVol = conferencesDF[conferencesDF['conferenceId'] == currConfJourId]['conferenceProceedingIds'].item()
    else:
        getProcVol = journalsDF[journalsDF['journalId'] == currConfJourId]['journalVolumeIds'].item()
    procVols.append(getProcVol)
papersDF['proceedingsVolumeIds'] = procVols


# In[30]:


papersDF.head()


# In[31]:


papersDF['paperAbstract'] = papersDF.apply(lambda x: 'Abstract' if x['paperAbstract'] == None else x['paperAbstract'], axis = 1)


# In[32]:


papersDF.to_csv('data/papers.csv',index = False, header = True, mode = 'w')


# ## Papers Domains

# In[33]:


subject_domain_ids = []
pIds = []

paperUrlNum = 0

for i in range(len(df)):
    paperCurr = [] 
    details = df[i]['_data']
    
    currPaperUrlNum = 'p'+str(paperUrlNum)
    
    # Adding pId to subjectDomainId
    if details['fieldsOfStudy']:
        for i in range(len(details['fieldsOfStudy'])):
            subjectDomainId = details['fieldsOfStudy'][i]
            subject_domain_ids.append(subjectDomainId)
            pIds.append(currPaperUrlNum)
    paperUrlNum += 1

subjectsPapersDF = pd.DataFrame(subject_domain_ids, columns = ['domainName'])
subjectsPapersDF['paperId'] = pIds


# In[34]:


subjectsPapersDF = subjectsPapersDF.merge(
                    domainDF,
                    how = 'inner',
                    left_on = ['domainName'],
                    right_on = ['domainName']
                    )


# In[35]:


subjectsPapersDF = subjectsPapersDF.merge(
                    papersDF,
                    how = 'inner',
                    left_on = ['paperId'],
                    right_on = ['paperId']
                    )
subjectsPapersDF.to_csv('data/subjectsPapers.csv',index = False, header = True, mode = 'w')


# In[36]:


subjectsPapersDF.head()


# ## proceedings - domain and volumes - domain

# In[37]:


subjectsConferencesJournalsDF = subjectsPapersDF[['conferenceJournalId','proceedingsVolumeIds','domainId']]


# In[38]:


subjectsConferencesJournalsDF.head()


# In[39]:


subjectsConferencesJournalsDF.to_csv('data/subjectsProceedingsVolumes.csv',index = False, header = True, mode = 'w')


# ## Authors Papers

# In[40]:


aUrlIds = []
pIds = []

paperUrlNum = 0

for i in range(len(df)):
    paperCurr = [] 
    details = df[i]['_data']
    currPaperUrlNum = 'p'+str(paperUrlNum)
    
    # Appending the pId to authorsDF
    if details['authors']:
        for i in range(len(details['authors'])):
            aUrlId = details['authors'][i]['authorId']
            aUrlIds.append(str(aUrlId))
            pIds.append(currPaperUrlNum)
    paperUrlNum += 1

authorsPapersDF = pd.DataFrame(aUrlIds, columns = ['authorUrl'])
authorsPapersDF['paperId'] = pIds


# In[41]:


authorsPapersDF = authorsPapersDF.merge(
                    authorsDF,
                    how = 'inner',
                    left_on = ['authorUrl'],
                    right_on = ['authorUrl']
                    )


# In[42]:


authorsPapersDF = authorsPapersDF.merge(
                    papersDF,
                    how = 'inner',
                    left_on = ['paperId'],
                    right_on = ['paperId']
                    )
authorsPapersDF.head()
authorsPapersDF.to_csv('data/authorsPapers.csv',index = False, header = True, mode = 'w')


# In[43]:


authorsPapersDF.head()


# ## Reviews

# In[44]:


ids = []
decisionChoices = ['accepted','rejected']

for i in range(len(papersDF)):
    ids.append('r'+str(i))

reviewsDF = pd.DataFrame(ids, columns = ['reviewId'])
reviewsDF['paperId'] = papersDF['paperId']
reviewsDF['reviewText'] = ['Review Comment'] * len(reviewsDF)
reviewsDF['reviewDecision'] = random.choices(decisionChoices, weights = [0.8,0.2], k = len(papersDF))
reviewsDF['paperTitle'] = papersDF['paperTitle']
reviewsDF.to_csv('data/reviews.csv',index = False, header = True, mode = 'w')


# In[45]:


reviewsDF.head()


# ## Reviewer

# In[46]:


all_authors = list(authorsPapersDF['authorId'].unique())
paperAuthors = authorsPapersDF.groupby('paperId', as_index = False, sort = False)['authorId'].agg(lambda x: [l for l in x])


# In[47]:


paperAuthors.head()


# In[48]:


totalPapers = len(papersDF)
set_authors = set(all_authors)

ids = []
papers = []
reviewers = []

for i in range(totalPapers * 2):
    ids.append('r'+str(i))
    papers.append(papersDF['paperId'][i//2])
    
    curr_pId = papersDF['paperId'][i//2]
    curr_authors = paperAuthors[paperAuthors['paperId'] == curr_pId]['authorId'].tolist()
    
    availableReviewers = [x for x in set_authors if not x in curr_authors]
    reviewers.append(random.choice(availableReviewers))


# In[49]:


reviewersDF = pd.DataFrame(ids, columns = ['rId'])
reviewersDF['paperId'] = papers
reviewersDF['authorId'] = reviewers


# In[50]:


reviewersDF = reviewersDF.merge(
            authorsDF,
            how = 'inner',
            left_on = ['authorId'],
            right_on = ['authorId']
            )


# In[51]:


reviewersDF = reviewersDF.merge(
            papersDF,
            how = 'inner',
            left_on = ['paperId'],
            right_on = ['paperId']
            )


# In[52]:


reviewersDF.to_csv('data/reviewers.csv',index = False, header = True, mode = 'w')


# In[53]:


reviewersDF.head()


# ## Chairs

# In[54]:


confPapers = papersDF[papersDF['conferenceJournalId'].str[:1] == 'c']['conferenceJournalId'].tolist()

confPapersDF = pd.DataFrame(confPapers, columns = ['conferenceId'])

ids = []
for i in range(len(confPapersDF)):
    ids.append('chair'+str(i))
confPapersDF['chairId'] = ids

confPapersDF['authorId'] = random.choices(authorsDF['authorId'], k = len(confPapersDF))


# In[55]:


confPapersDF.to_csv('data/chairs.csv',index = False, header = True, mode = 'w')


# In[56]:


confPapersDF.head()


# ## Editors

# In[57]:


jourPapers = papersDF[papersDF['conferenceJournalId'].str[:1] == 'j']['conferenceJournalId'].tolist()

jourPapersDF = pd.DataFrame(jourPapers, columns = ['journalId'])

ids = []
for i in range(len(jourPapersDF)):
    ids.append('editor'+str(i))
jourPapersDF['editorId'] = ids

jourPapersDF['authorId'] = random.choices(authorsDF['authorId'], k = len(jourPapersDF))
jourPapersDF.to_csv('data/editors.csv',index = False, header = True, mode = 'w')


# In[58]:


jourPapersDF.head()


# In[59]:


jourPapersDF.to_csv('data/editors.csv',index = False, header = True, mode = 'w')

