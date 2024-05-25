import pandas as pd
from rdflib.namespace import XSD, URIRef
from rdflib import Graph
from rdflib import Namespace
from rdflib import Literal    


def paperTitle_ABox():
    graph.add((lab2.Paper, lab2.paperTitle, XSD.string))
    for k in range(len(papers_df['paperId'])):
        graph.add((URIRef(lab2+papers_df['paperId'][k]), lab2.paperTitle, Literal(papers_df['paperTitle'][k])))


def isSubmittedTo_ABox():
    graph.add((lab2.Paper, lab2.isSubmittedTo, lab2.Venue))
    for k in range(len(papers_df['paperId'])):
        graph.add((URIRef(lab2+papers_df['paperId'][k]), lab2.isSubmittedTo, URIRef(lab2+papers_df['conferenceJournalId'][k])))


def hasPaperDomain_ABox():
    graph.add((lab2.Paper, lab2.hasPaperDomain, lab2.Domain))
    for k in range(len(domainsPapers_df['paperId'])):
        graph.add((URIRef(domainsPapers_df['paperId'][k]), lab2.hasPaperDomain, URIRef(lab2+domainsPapers_df['domainId'][k])))


def isPublishedInProcVol_ABox():
    graph.add((lab2.Paper, lab2.isPublishedInProc, lab2.Proceeding))  
    graph.add((lab2.Paper, lab2.isPublishedInVol, lab2.Volume))
    for k in range(len(papers_df['paperId'])):
        if papers_df['conferenceJournalId'][k][0] == 'c':
            graph.add((URIRef(lab2+papers_df['paperId'][k]), lab2.isPublishedInProc, URIRef(lab2+papers_df['proceedingsVolumesIds'][k])))
        else:
            graph.add((URIRef(lab2+papers_df['paperId'][k]), lab2.isPublishedInVol, URIRef(lab2+papers_df['proceedingsVolumesIds'][k])))


def authorName_ABox():
    graph.add((lab2.Author, lab2.authorName, XSD.string))
    for k in range(len(authors_df['authorId'])):
        graph.add((URIRef(lab2+authors_df['authorId'][k]), lab2.authorName, Literal(authors_df['authorName'][k])))


def writes_ABox():
    graph.add((lab2.Author, lab2.writes, lab2.Paper))   
    for k in range(len(authorsPapers_df['authorId'])):
        graph.add((URIRef(lab2+authorsPapers_df['authorId'][k]), lab2.writes, URIRef(lab2+authorsPapers_df['paperId'][k])))


def manages_ABox():
    graph.add((lab2.Chair, lab2.manages, lab2.Conference))
    for k in range(len(chairs_df['conferenceId'])):
        graph.add((URIRef(lab2+chairs_df['authorId'][k]), lab2.manages, URIRef(lab2+chairs_df['conferenceId'][k])))


def handles_ABox():
    graph.add((lab2.Editor, lab2.handles, lab2.Journal))
    for k in range(len(editors_df['journalId'])):
        graph.add((URIRef(lab2+editors_df['authorId'][k]), lab2.handles, URIRef(lab2+editors_df['journalId'][k])))


def confTitle_ABox():
    graph.add((lab2.Conference, lab2.confTitle, XSD.string))
    for k in range(len(confs_df['conferenceId'])):
        graph.add((URIRef(lab2+confs_df['conferenceId'][k]), lab2.conferenceTitle, Literal(confs_df['conferenceTitle'][k])))


def procName_ABox():
    graph.add((lab2.Proceeding, lab2.procName, XSD.string))
    for k in range(len(proceedings_df['proceedingId'])):
        graph.add((URIRef(lab2+proceedings_df['proceedingId'][k]), lab2.procName, Literal(proceedings_df['proceedingName'][k])))


def procYear_ABox():
    graph.add((lab2.Proceeding, lab2.procYear, XSD.int))
    for k in range(len(proceedings_df['proceedingId'])):
        graph.add((URIRef(lab2+proceedings_df['proceedingId'][k]), lab2.proceedingYear, Literal(proceedings_df['proceedingYear'][k])))


def inProc_ABox():
    graph.add((lab2.Conference, lab2.inProc, lab2.Proceeding))
    for k in range(len(confProcs_df['conferenceId'])):
        graph.add((URIRef(lab2+confProcs_df['conferenceId'][k]), lab2.inProc, URIRef(lab2+confProcs_df['conferenceProceedingIds'][k])))


def journalTitle_ABox():
    graph.add((lab2.Journal, lab2.journalTitle, XSD.string))
    for k in range(len(journals_df['journalId'])):
        graph.add((URIRef(lab2+journals_df['journalId'][k]), lab2.journalTitle, Literal(journals_df['journalTitle'][k])))


def volName_ABox():
    graph.add((lab2.Volume, lab2.volName, XSD.string))
    for k in range(len(volumes_df['volumeId'])):
        graph.add((URIRef(lab2+volumes_df['volumeId'][k]), lab2.volName, Literal(volumes_df['volumeName'][k])))


def volYear_ABox():
    graph.add((lab2.Volume, lab2.volYear, XSD.int))
    for k in range(len(volumes_df['volumeId'])):
        graph.add((URIRef(lab2+volumes_df['volumeId'][k]), lab2.volYear, Literal(volumes_df['volumeYear'][k])))


def inVol_ABox():
    graph.add((lab2.Journal, lab2.inVol, lab2.Volume))
    for k in range(len(journalVols_df['journalId'])):
        graph.add((URIRef(lab2+journalVols_df['journalId'][k]), lab2.inVol, URIRef(lab2+journalVols_df['journalVolumeIds'][k])))


def hasProcVolDomain_ABox():
    graph.add((lab2.Proceeding, lab2.hasProcDomain, lab2.Domain))
    graph.add((lab2.Volume, lab2.hasVolDomain, lab2.Domain))
    for k in range(len(domainsProcsVols_df['proceedingsVolumesIds'])):
        if domainsProcsVols_df['proceedingsVolumesIds'][k][0] == 'c':
            graph.add((URIRef(lab2+domainsProcsVols_df['proceedingsVolumesIds'][k]), lab2.hasProcDomain, URIRef(lab2+domainsProcsVols_df['domainId'][k])))
        else:
            graph.add((URIRef(lab2+domainsProcsVols_df['proceedingsVolumesIds'][k]), lab2.hasVolDomain, URIRef(lab2+domainsProcsVols_df['domainId'][k])))


def domainName_ABox():
    graph.add((lab2.Domain, lab2.domainName, XSD.string))
    for k in range(len(domains_df['domainId'])):
        graph.add((URIRef(lab2+domains_df['domainId'][k]), lab2.domainName, Literal(domains_df['domainName'][k])))


def reviewText_ABox():
    graph.add((lab2.Review, lab2.reviewText, XSD.string))
    for k in range(len(reviews_df['reviewId'])):
        graph.add((URIRef(lab2+reviews_df['reviewId'][k]), lab2.reviewText, Literal(reviews_df['reviewText'][k])))


def decision_ABox():
    graph.add((lab2.Review, lab2.decision, XSD.boolean))
    for k in range(len(reviews_df['reviewId'])):
        graph.add((URIRef(lab2+reviews_df['reviewId'][k]), lab2.decision, Literal(reviews_df['reviewDecision'][k])))


def gives_ABox():
    graph.add((lab2.Reviewer, lab2.gives, lab2.Review))
    for k in range(len(reviewers_df['rId'])):
        graph.add((URIRef(lab2+reviewers_df['authorId'][k]), lab2.gives, URIRef(lab2+reviewers_df['rId'][k])))


def isGivenTo_ABox():
    graph.add((lab2.Review, lab2.isGivenTo, lab2.Paper))
    for k in range(len(reviews_df['reviewId'])):
        graph.add((URIRef(lab2+reviews_df['reviewId'][k]), lab2.isGivenTo, URIRef(lab2+reviews_df['paperId'][k])))


if __name__ == '__main__':
    authors_df = pd.read_csv('data/authors.csv')
    authorsPapers_df = pd.read_csv('data/authorsPapers.csv')
    chairs_df = pd.read_csv('data/chairs.csv')
    confs_df = pd.read_csv('data/conferences.csv')
    confProcs_df = pd.read_csv('data/conferenceProceedings.csv')
    domains_df = pd.read_csv('data/domains.csv')
    domainsPapers_df = pd.read_csv('data/domainsPapers.csv')
    domainsProcsVols_df = pd.read_csv('data/domainsProceedingsVolumes.csv')
    editors_df = pd.read_csv('data/editors.csv')
    journals_df = pd.read_csv('data/journals.csv')
    journalVols_df = pd.read_csv('data/journalVolumes.csv')
    papers_df = pd.read_csv('data/papers.csv')
    proceedings_df = pd.read_csv('data/proceedings.csv')
    reviewers_df = pd.read_csv('data/reviewers.csv')
    reviews_df = pd.read_csv('data/reviews.csv')
    volumes_df = pd.read_csv('data/volumes.csv')

    graph = Graph()
    lab2 = Namespace("http://sdmlab2.org/")

    paperTitle_ABox()
    isSubmittedTo_ABox()
    hasPaperDomain_ABox()
    isPublishedInProcVol_ABox()
    authorName_ABox()
    writes_ABox()
    manages_ABox()
    handles_ABox()
    confTitle_ABox()
    procName_ABox()
    procYear_ABox()
    inProc_ABox()
    journalTitle_ABox()
    volName_ABox()
    volYear_ABox()
    inVol_ABox()
    hasProcVolDomain_ABox()
    domainName_ABox()
    reviewText_ABox()
    decision_ABox()
    gives_ABox()
    isGivenTo_ABox()
    
    ttl = graph.serialize(destination='data/abox.ttl', format="ttl")
    print(ttl)