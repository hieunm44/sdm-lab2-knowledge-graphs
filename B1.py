from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDFS, RDF, XSD

graph = Graph()
lab2 = Namespace("http://sdmlab2.org/")


# Paper Superclass
graph.add((lab2.Paper, RDF.type, RDFS.Class))
graph.add((lab2.Paper, RDFS.label, Literal("Paper")))

graph.add((lab2.paperTitle, RDF.type, RDF.Property))
graph.add((lab2.paperTitle, RDFS.domain, lab2.Paper))
graph.add((lab2.paperTitle, RDFS.range, XSD.string))
graph.add((lab2.paperTitle, RDFS.label, Literal("paperTitle")))

graph.add((lab2.isSubmittedTo, RDF.type, RDF.Property))
graph.add((lab2.isSubmittedTo, RDFS.domain, lab2.Paper))
graph.add((lab2.isSubmittedTo, RDFS.range, lab2.Venue))
graph.add((lab2.isSubmittedTo, RDFS.label, Literal("isSubmittedTo")))

graph.add((lab2.isPublishedInProc, RDF.type, RDF.Property))
graph.add((lab2.isPublishedInProc, RDFS.domain, lab2.Paper))
graph.add((lab2.isPublishedInProc, RDFS.range, lab2.Proceeding))
graph.add((lab2.isPublishedInProc, RDFS.label, Literal("isPublishedInProc")))

graph.add((lab2.isPublishedInVol, RDF.type, RDF.Property))
graph.add((lab2.isPublishedInVol, RDFS.domain, lab2.Paper))
graph.add((lab2.isPublishedInVol, RDFS.range, lab2.Volume))
graph.add((lab2.isPublishedInVol, RDFS.label, Literal("isPublishedInVol")))

# Subclasses of Paper
# Poster
graph.add((lab2.Poster, RDF.type, RDFS.Class))
graph.add((lab2.Poster, RDFS.subClassOf, lab2.Paper))
graph.add((lab2.Poster, RDFS.label, Literal("Poster")))

# Full paper
graph.add((lab2.FullPaper, RDF.type, RDFS.Class))
graph.add((lab2.FullPaper, RDFS.subClassOf, lab2.Paper))
graph.add((lab2.FullPaper, RDFS.label, Literal("FullPaper")))

graph.add((lab2.hasPaperDomain, RDF.type, RDF.Property))
graph.add((lab2.hasPaperDomain, RDFS.domain, lab2.Paper))
graph.add((lab2.hasPaperDomain, RDFS.range, lab2.Domain))
graph.add((lab2.hasPaperDomain, RDFS.label, Literal("hasPaperDomain")))


# Person Superclass
graph.add((lab2.Person, RDF.type, RDFS.Class))
graph.add((lab2.Person, RDFS.label, Literal("Person")))

# Subclasses of Person
# Author
graph.add((lab2.Author, RDF.type, RDFS.Class))
graph.add((lab2.Author, RDFS.subClassOf, lab2.Person))
graph.add((lab2.Author, RDFS.label, Literal("Author")))

graph.add((lab2.authorName, RDF.type, RDF.Property))
graph.add((lab2.authorName, RDFS.domain, lab2.Author))
graph.add((lab2.authorName, RDFS.range, XSD.string))
graph.add((lab2.authorName, RDFS.label, Literal("authorName")))

graph.add((lab2.writes, RDF.type, RDF.Property))
graph.add((lab2.writes, RDFS.domain, lab2.Author))
graph.add((lab2.writes, RDFS.range, lab2.Paper))
graph.add((lab2.writes, RDFS.label, Literal("writes")))

# Reviewer
graph.add((lab2.Reviewer, RDF.type, RDFS.Class))
graph.add((lab2.Reviewer, RDFS.subClassOf, lab2.Person))
graph.add((lab2.Reviewer, RDFS.label, Literal("Reviewer")))

# Editor
graph.add((lab2.Editor, RDF.type, RDFS.Class))
graph.add((lab2.Editor, RDFS.subClassOf, lab2.Person))
graph.add((lab2.Editor, RDFS.label, Literal("Editor")))	

graph.add((lab2.handles, RDF.type, RDF.Property))
graph.add((lab2.handles, RDFS.domain, lab2.Editor))
graph.add((lab2.handles, RDFS.range, lab2.Journal))
graph.add((lab2.handles, RDFS.label, Literal("handles")))

# Chair
graph.add((lab2.Editor, RDF.type, RDFS.Class))
graph.add((lab2.Editor, RDFS.subClassOf, lab2.Person))
graph.add((lab2.Editor, RDFS.label, Literal("Chair")))

graph.add((lab2.manages, RDF.type, RDF.Property))
graph.add((lab2.manages, RDFS.domain, lab2.Chair))
graph.add((lab2.manages, RDFS.range, lab2.Conference))
graph.add((lab2.manages, RDFS.label, Literal("manages")))


# Venue Superclass
graph.add((lab2.Venue, RDF.type, RDFS.Class))
graph.add((lab2.Venue, RDFS.label, Literal("Venue")))

# Subclasses of Venue
# Conference
graph.add((lab2.Conference, RDF.type, RDFS.Class))
graph.add((lab2.Conference, RDFS.subClassOf, lab2.Venue))
graph.add((lab2.Conference, RDFS.label, Literal("Conference")))

graph.add((lab2.conferenceTitle, RDF.type, RDF.Property))
graph.add((lab2.conferenceTitle, RDFS.domain, lab2.Conference))
graph.add((lab2.conferenceTitle, RDFS.range, XSD.string))
graph.add((lab2.conferenceTitle, RDFS.label, Literal("conferenceTitle")))

graph.add((lab2.inProc, RDF.type, RDF.Property))
graph.add((lab2.inProc, RDFS.domain, lab2.Conference))
graph.add((lab2.inProc, RDFS.range, lab2.Proceedings))
graph.add((lab2.inProc, RDFS.label, Literal("inProc")))

# SubClasses of Conference
# Workshop
graph.add((lab2.Workshop, RDF.type, RDFS.Class))
graph.add((lab2.Workshop, RDFS.subClassOf, lab2.Conference))
graph.add((lab2.Workshop, RDFS.label, Literal("Workshop")))

# Main Conference
graph.add((lab2.MainConference, RDF.type, RDFS.Class))
graph.add((lab2.MainConference, RDFS.subClassOf, lab2.Conference))
graph.add((lab2.MainConference, RDFS.label, Literal("MainConference")))

# Journal
graph.add((lab2.Journal, RDF.type, RDFS.Class))
graph.add((lab2.Journal, RDFS.subClassOf, lab2.Venue))
graph.add((lab2.Journal, RDFS.label, Literal("Journal")))

graph.add((lab2.journalTitle, RDF.type, RDF.Property))
graph.add((lab2.journalTitle, RDFS.domain, lab2.Journal))
graph.add((lab2.journalTitle, RDFS.range, XSD.string))
graph.add((lab2.journalTitle, RDFS.label, Literal("journalTitle")))

graph.add((lab2.isOf, RDF.type, RDF.Property))
graph.add((lab2.isOf, RDFS.domain, lab2.Journal))
graph.add((lab2.isOf, RDFS.range, lab2.Volume))
graph.add((lab2.isOf, RDFS.label, Literal("inVol")))


# Proceeding Class
graph.add((lab2.Proceeding, RDF.type, RDFS.Class))
graph.add((lab2.Proceeding, RDFS.label, Literal("Proceeding")))

graph.add((lab2.procName, RDF.type, RDF.Property))
graph.add((lab2.procName, RDFS.domain, lab2.Proceedings))
graph.add((lab2.procName, RDFS.range, XSD.string))
graph.add((lab2.procName, RDFS.label, Literal("procName")))	

graph.add((lab2.procYear, RDF.type, RDF.Property))
graph.add((lab2.procYear, RDFS.domain, lab2.Proceeding))
graph.add((lab2.procYear, RDFS.range, XSD.int))
graph.add((lab2.procYear, RDFS.label, Literal("procYear")))

graph.add((lab2.hasProcDomain, RDF.type, RDF.Property))
graph.add((lab2.hasProcDomain, RDFS.domain, lab2.Proceeding))
graph.add((lab2.hasProcDomain, RDFS.range, lab2.Domain))
graph.add((lab2.hasProcDomain, RDFS.label, Literal("hasProcDomain")))

# Volume Class
graph.add((lab2.Volume, RDF.type, RDFS.Class))
graph.add((lab2.Volume, RDFS.label, Literal("Volume")))

# Adding properties for volume
graph.add((lab2.volumeName, RDF.type, RDF.Property))
graph.add((lab2.volumeName, RDFS.domain, lab2.Volume))
graph.add((lab2.volumeName, RDFS.range, XSD.string))
graph.add((lab2.volumeName, RDFS.label, Literal("volName")))	

graph.add((lab2.volumeYear, RDF.type, RDF.Property))
graph.add((lab2.volumeYear, RDFS.domain, lab2.Volume))
graph.add((lab2.volumeYear, RDFS.range, XSD.int))
graph.add((lab2.volumeYear, RDFS.label, Literal("volYear")))

graph.add((lab2.hasVolDomain, RDF.type, RDF.Property))
graph.add((lab2.hasVolDomain, RDFS.domain, lab2.Volume))
graph.add((lab2.hasVolDomain, RDFS.range, lab2.Domain))
graph.add((lab2.hasVolDomain, RDFS.label, Literal("hasVolDomain")))


# Domain Class
graph.add((lab2.Domain, RDF.type, RDFS.Class))
graph.add((lab2.Domain, RDFS.label, Literal("SubjectDomain")))

graph.add((lab2.keywords, RDF.type, RDF.Property))
graph.add((lab2.keywords, RDFS.domain, lab2.Domain))
graph.add((lab2.keywords, RDFS.range, XSD.string))
graph.add((lab2.keywords, RDFS.label, Literal("keywords")))


# Review Class
graph.add((lab2.Review, RDF.type, RDFS.Class))
graph.add((lab2.Review, RDFS.label, Literal("Review")))

graph.add((lab2.reviewText, RDF.type, RDF.Property))
graph.add((lab2.reviewText, RDFS.domain, lab2.Review))
graph.add((lab2.reviewText, RDFS.range, XSD.string))
graph.add((lab2.reviewText, RDFS.label, Literal("reviewText")))

graph.add((lab2.decision, RDF.type, RDF.Property))
graph.add((lab2.decision, RDFS.domain, lab2.Review))
graph.add((lab2.decision, RDFS.range, XSD.boolean))
graph.add((lab2.decision, RDFS.label, Literal("decision")))

graph.add((lab2.gives, RDF.type, RDF.Property))
graph.add((lab2.gives, RDFS.domain, lab2.Reviewer))
graph.add((lab2.gives, RDFS.range, lab2.Review))
graph.add((lab2.gives, RDFS.label, Literal("gives")))

graph.add((lab2.isGivenTo, RDF.type, RDF.Property))
graph.add((lab2.isGivenTo, RDFS.domain, lab2.Review))
graph.add((lab2.isGivento, RDFS.range, lab2.Paper))
graph.add((lab2.isGivento, RDFS.label, Literal("isGivenTo")))


ttl = graph.serialize(destination='data/tbox.ttl', format="ttl")
print(ttl)