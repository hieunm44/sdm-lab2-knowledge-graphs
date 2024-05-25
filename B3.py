import pandas as pd
from rdflib.namespace import RDF, URIRef
from rdflib import Graph
from rdflib import Namespace


def connect_isSubmittedTo():
    for k in range(len(papers_df['paperId'])):
        graph.add((URIRef(lab2+papers_df['paperId'][k]), RDF.type, lab2.Paper))


def connect_hasPaperDomain():
    for k in range(len(domainsPapers_df['paperId'])):
        graph.add((URIRef(domainsPapers_df['domainId'][k]), RDF.type, lab2.Domain))


def connect_isPublishedInProcVol():  
    for k in range(len(papers_df['paperId'])):
        if papers_df['conferenceJournalId'][k][0] == 'c':
            graph.add((URIRef(lab2+papers_df['proceedingsVolumesIds'][k]), RDF.type, lab2.Proceeding))
        else:
            graph.add((URIRef(lab2+papers_df['proceedingsVolumesIds'][k]), RDF.type, lab2.Volume))


def connect_writes():
    for k in range(len(authorsPapers_df['authorId'])):
        graph.add((URIRef(lab2+authorsPapers_df['authorId'][k]), RDF.type, lab2.Author))
        ptype = authorsPapers_df['paperType'][k]
        if ptype == "fullPaper":
            graph.add((URIRef(lab2+authorsPapers_df['paperId'][k]), RDF.type, lab2.FullPaper))
        elif ptype == "poster":
            graph.add((URIRef(lab2+authorsPapers_df['paperId'][k]), RDF.type, lab2.Poster))


def connect_manages():
    for k in range(len(chairs_df['conferenceId'])):
        graph.add((URIRef(lab2+chairs_df['authorId'][k]), RDF.type, lab2.Chair))
        graph.add((URIRef(lab2+chairs_df['conferenceId'][k]), RDF.type, lab2.Conference))


def connect_handles():
    for k in range(len(editors_df['journalId'])):
        graph.add((URIRef(lab2+editors_df['authorId'][k]), RDF.type, lab2.Editor))
        graph.add((URIRef(lab2+editors_df['journalId'][k]), RDF.type, lab2.Journal))


def connect_inProc():
    for k in range(len(confProcs_df['conferenceId'])):
        graph.add((URIRef(lab2+confProcs_df['conferenceProceedingIds'][k]), RDF.type, lab2.Proceeding))
        ctype = confProcs_df['conferenceType'][k]
        if ctype == 'mainConference':
            graph.add((URIRef(lab2+confProcs_df['conferenceId'][k]), RDF.type, lab2.MainConference))
        elif ctype == 'workshop':
            graph.add((URIRef(lab2+confProcs_df['conferenceId'][k]), RDF.type, lab2.Workshop))


def connect_inVol():
    for k in range(len(journalVols_df['journalId'])):
        graph.add((URIRef(lab2+journalVols_df['journalId'][k]), RDF.type, lab2.Journal))
        graph.add((URIRef(lab2+journalVols_df['journalVolumeIds'][k]), RDF.type, lab2.Volume))


def connect_hasProcVolDomain():
    for k in range(len(domainsProcsVols_df['proceedingsVolumesIds'])):
        if domainsProcsVols_df['proceedingsVolumesIds'][k][0] == 'c':
            graph.add((URIRef(lab2+domainsProcsVols_df['proceedingsVolumesIds'][k]), RDF.type, lab2.Proceeding))
        else:
            graph.add((URIRef(lab2+domainsProcsVols_df['proceedingsVolumesIds'][k]), RDF.type, lab2.Volume))


def connect_gives():
    for k in range(len(reviewers_df['rId'])):
        graph.add((URIRef(lab2+reviewers_df['authorId'][k]), RDF.type, lab2.Reviewer))
        graph.add((URIRef(lab2+reviewers_df['rId'][k]), RDF.type, lab2.Review))


def connect_isGivenTo():
    for k in range(len(reviews_df['reviewId'])):
        graph.add((URIRef(lab2+reviews_df['reviewId'][k]), RDF.type, lab2.Review))
        graph.add((URIRef(lab2+reviews_df['paperId'][k]), RDF.type, lab2.Paper))


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

    connect_isSubmittedTo()
    connect_hasPaperDomain()
    connect_isPublishedInProcVol()
    connect_writes()
    connect_manages()
    connect_handles()
    connect_inProc()
    connect_inVol()
    connect_hasProcVolDomain()
    connect_gives()
    connect_isGivenTo()

    ttl = graph.serialize(destination='data/abox_tbox_connection.ttl', format="ttl")
    print(ttl)