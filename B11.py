from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDFS, RDF, XSD

graph = Graph()
lab = Namespace("http://sdmlab.org/")


# Paper Superclass
graph.add((lab.Paper, RDF.type, RDFS.Class))
graph.add((lab.Paper, RDFS.label, Literal("Paper")))

graph.add((lab.paperTitle, RDF.type, RDF.Property))
graph.add((lab.paperTitle, RDFS.domain, lab.Paper))
graph.add((lab.paperTitle, RDFS.range, XSD.string))
graph.add((lab.paperTitle, RDFS.label, Literal("paperTitle")))

# Add - Shofi
graph.add((lab.paperAbstract, RDF.type, RDF.Property))
graph.add((lab.paperAbstract, RDFS.domain, lab.Paper))
graph.add((lab.paperAbstract, RDFS.range, XSD.string))
graph.add((lab.paperAbstract, RDFS.label, Literal("paperAbstract")))

graph.add((lab.isSubmittedTo, RDF.type, RDF.Property))
graph.add((lab.isSubmittedTo, RDFS.domain, lab.Paper))
graph.add((lab.isSubmittedTo, RDFS.range, lab.Venue))
graph.add((lab.isSubmittedTo, RDFS.label, Literal("isSubmittedTo")))

graph.add((lab.isPublishedInProc, RDF.type, RDF.Property))
graph.add((lab.isPublishedInProc, RDFS.domain, lab.Paper))
graph.add((lab.isPublishedInProc, RDFS.range, lab.Proceeding))
graph.add((lab.isPublishedInProc, RDFS.label, Literal("isPublishedInProc")))

graph.add((lab.isPublishedInVol, RDF.type, RDF.Property))
graph.add((lab.isPublishedInVol, RDFS.domain, lab.Paper))
graph.add((lab.isPublishedInVol, RDFS.range, lab.Volume))
graph.add((lab.isPublishedInVol, RDFS.label, Literal("isPublishedInVol")))

# Subclasses of Paper
# Poster
graph.add((lab.Poster, RDF.type, RDFS.Class))
graph.add((lab.Poster, RDFS.subClassOf, lab.Paper))
graph.add((lab.Poster, RDFS.label, Literal("Poster")))

# Full paper
graph.add((lab.FullPaper, RDF.type, RDFS.Class))
graph.add((lab.FullPaper, RDFS.subClassOf, lab.Paper))
graph.add((lab.FullPaper, RDFS.label, Literal("FullPaper")))

graph.add((lab.hasPaperDomain, RDF.type, RDF.Property))
graph.add((lab.hasPaperDomain, RDFS.domain, lab.Paper))
graph.add((lab.hasPaperDomain, RDFS.range, lab.Domain))
graph.add((lab.hasPaperDomain, RDFS.label, Literal("hasPaperDomain")))


# Person Superclass
graph.add((lab.Person, RDF.type, RDFS.Class))
graph.add((lab.Person, RDFS.label, Literal("Person")))

# Subclasses of Person
# Author
graph.add((lab.Author, RDF.type, RDFS.Class))
graph.add((lab.Author, RDFS.subClassOf, lab.Person))
graph.add((lab.Author, RDFS.label, Literal("Author")))

graph.add((lab.authorName, RDF.type, RDF.Property))
graph.add((lab.authorName, RDFS.domain, lab.Author))
graph.add((lab.authorName, RDFS.range, XSD.string))
graph.add((lab.authorName, RDFS.label, Literal("authorName")))

graph.add((lab.writes, RDF.type, RDF.Property))
graph.add((lab.writes, RDFS.domain, lab.Author))
graph.add((lab.writes, RDFS.range, lab.Paper))
graph.add((lab.writes, RDFS.label, Literal("writes")))

# Reviewer
graph.add((lab.Reviewer, RDF.type, RDFS.Class))
graph.add((lab.Reviewer, RDFS.subClassOf, lab.Person))
graph.add((lab.Reviewer, RDFS.label, Literal("Reviewer")))

# Editor
graph.add((lab.Editor, RDF.type, RDFS.Class))
graph.add((lab.Editor, RDFS.subClassOf, lab.Person))
graph.add((lab.Editor, RDFS.label, Literal("Editor")))	

graph.add((lab.handles, RDF.type, RDF.Property))
graph.add((lab.handles, RDFS.domain, lab.Editor))
graph.add((lab.handles, RDFS.range, lab.Journal))
graph.add((lab.handles, RDFS.label, Literal("handles")))

# Chair
graph.add((lab.Editor, RDF.type, RDFS.Class))
graph.add((lab.Editor, RDFS.subClassOf, lab.Person))
graph.add((lab.Editor, RDFS.label, Literal("Chair")))

graph.add((lab.manages, RDF.type, RDF.Property))
graph.add((lab.manages, RDFS.domain, lab.Chair))
graph.add((lab.manages, RDFS.range, lab.Conference))
graph.add((lab.manages, RDFS.label, Literal("manages")))


# Venue Superclass
graph.add((lab.Venue, RDF.type, RDFS.Class))
graph.add((lab.Venue, RDFS.label, Literal("Venue")))

# Subclasses of Venue
# Conference
graph.add((lab.Conference, RDF.type, RDFS.Class))
graph.add((lab.Conference, RDFS.subClassOf, lab.Venue))
graph.add((lab.Conference, RDFS.label, Literal("Conference")))

graph.add((lab.conferenceTitle, RDF.type, RDF.Property))
graph.add((lab.conferenceTitle, RDFS.domain, lab.Conference))
graph.add((lab.conferenceTitle, RDFS.range, XSD.string))
graph.add((lab.conferenceTitle, RDFS.label, Literal("conferenceTitle")))

# Add - Shofi
graph.add((lab.conferenceCity, RDF.type, RDF.Property))
graph.add((lab.conferenceCity, RDFS.domain, lab.Conference))
graph.add((lab.conferenceCity, RDFS.range, XSD.string))
graph.add((lab.conferenceCity, RDFS.label, Literal("conferenceCity")))

# Add - Shofi
graph.add((lab.conferenceYear, RDF.type, RDF.Property))
graph.add((lab.conferenceYear, RDFS.domain, lab.Conference))
graph.add((lab.conferenceYear, RDFS.range, XSD.int))
graph.add((lab.conferenceYear, RDFS.label, Literal("conferenceYear")))

graph.add((lab.inProc, RDF.type, RDF.Property))
graph.add((lab.inProc, RDFS.domain, lab.Conference))
graph.add((lab.inProc, RDFS.range, lab.Proceedings))
graph.add((lab.inProc, RDFS.label, Literal("inProc")))

# SubClasses of Conference
# Workshop
graph.add((lab.Workshop, RDF.type, RDFS.Class))
graph.add((lab.Workshop, RDFS.subClassOf, lab.Conference))
graph.add((lab.Workshop, RDFS.label, Literal("Workshop")))

# Main Conference
graph.add((lab.MainConference, RDF.type, RDFS.Class))
graph.add((lab.MainConference, RDFS.subClassOf, lab.Conference))
graph.add((lab.MainConference, RDFS.label, Literal("MainConference")))

# Journal
graph.add((lab.Journal, RDF.type, RDFS.Class))
graph.add((lab.Journal, RDFS.subClassOf, lab.Venue))
graph.add((lab.Journal, RDFS.label, Literal("Journal")))

graph.add((lab.journalTitle, RDF.type, RDF.Property))
graph.add((lab.journalTitle, RDFS.domain, lab.Journal))
graph.add((lab.journalTitle, RDFS.range, XSD.string))
graph.add((lab.journalTitle, RDFS.label, Literal("journalTitle")))

graph.add((lab.isOf, RDF.type, RDF.Property))
graph.add((lab.isOf, RDFS.domain, lab.Journal))
graph.add((lab.isOf, RDFS.range, lab.Volume))
graph.add((lab.isOf, RDFS.label, Literal("inVol")))


# Proceeding Class
graph.add((lab.Proceeding, RDF.type, RDFS.Class))
graph.add((lab.Proceeding, RDFS.label, Literal("Proceeding")))

graph.add((lab.procName, RDF.type, RDF.Property))
graph.add((lab.procName, RDFS.domain, lab.Proceedings))
graph.add((lab.procName, RDFS.range, XSD.string))
graph.add((lab.procName, RDFS.label, Literal("procName")))	

#Comment - Shofi
# graph.add((lab.procYear, RDF.type, RDF.Property))
# graph.add((lab.procYear, RDFS.domain, lab.Proceeding))
# graph.add((lab.procYear, RDFS.range, XSD.int))
# graph.add((lab.procYear, RDFS.label, Literal("procYear")))

graph.add((lab.hasProcDomain, RDF.type, RDF.Property))
graph.add((lab.hasProcDomain, RDFS.domain, lab.Proceeding))
graph.add((lab.hasProcDomain, RDFS.range, lab.Domain))
graph.add((lab.hasProcDomain, RDFS.label, Literal("hasProcDomain")))

# Volume Class
graph.add((lab.Volume, RDF.type, RDFS.Class))
graph.add((lab.Volume, RDFS.label, Literal("Volume")))

# Adding properties for volume
graph.add((lab.volumeName, RDF.type, RDF.Property))
graph.add((lab.volumeName, RDFS.domain, lab.Volume))
graph.add((lab.volumeName, RDFS.range, XSD.string))
graph.add((lab.volumeName, RDFS.label, Literal("volName")))	

graph.add((lab.volumeYear, RDF.type, RDF.Property))
graph.add((lab.volumeYear, RDFS.domain, lab.Volume))
graph.add((lab.volumeYear, RDFS.range, XSD.int))
graph.add((lab.volumeYear, RDFS.label, Literal("volYear")))

graph.add((lab.hasVolDomain, RDF.type, RDF.Property))
graph.add((lab.hasVolDomain, RDFS.domain, lab.Volume))
graph.add((lab.hasVolDomain, RDFS.range, lab.Domain))
graph.add((lab.hasVolDomain, RDFS.label, Literal("hasVolDomain")))


# Domain Class
graph.add((lab.Domain, RDF.type, RDFS.Class))
graph.add((lab.Domain, RDFS.label, Literal("SubjectDomain")))

graph.add((lab.keywords, RDF.type, RDF.Property))
graph.add((lab.keywords, RDFS.domain, lab.Domain))
graph.add((lab.keywords, RDFS.range, XSD.string))
graph.add((lab.keywords, RDFS.label, Literal("keywords")))


# Review Class
graph.add((lab.Review, RDF.type, RDFS.Class))
graph.add((lab.Review, RDFS.label, Literal("Review")))

graph.add((lab.reviewText, RDF.type, RDF.Property))
graph.add((lab.reviewText, RDFS.domain, lab.Review))
graph.add((lab.reviewText, RDFS.range, XSD.string))
graph.add((lab.reviewText, RDFS.label, Literal("reviewText")))

graph.add((lab.decision, RDF.type, RDF.Property))
graph.add((lab.decision, RDFS.domain, lab.Review))
graph.add((lab.decision, RDFS.range, XSD.boolean))
graph.add((lab.decision, RDFS.label, Literal("decision")))

graph.add((lab.gives, RDF.type, RDF.Property))
graph.add((lab.gives, RDFS.domain, lab.Reviewer))
graph.add((lab.gives, RDFS.range, lab.Review))
graph.add((lab.gives, RDFS.label, Literal("gives")))

graph.add((lab.isGivenTo, RDF.type, RDF.Property))
graph.add((lab.isGivenTo, RDFS.domain, lab.Review))
graph.add((lab.isGivento, RDFS.range, lab.Paper))
graph.add((lab.isGivento, RDFS.label, Literal("isGivenTo")))


ttl = graph.serialize(destination='data/tbox.ttl', format="ttl")
print(ttl)