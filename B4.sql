-- 1. Find all Authors.
PREFIX lab2: <http://sdmlab2.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?authorName
WHERE
{
    ?author rdf:type lab2:Author .
    ?author lab2:authorName ?authorName .
}


-- 2. Find all properties whose domain is Author.
PREFIX lab2: <http://sdmlab2.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?propertyName
WHERE
{
    ?propertyName rdfs:domain lab2:Author .
}



-- 3. Find all properties whose domain is either Conference or Journal.
PREFIX lab2: <http://sdmlab2.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?propertyName
WHERE 
{
    {?propertyName rdfs:domain lab2:Conference}
    UNION
    {?propertyName rdfs:domain lab2:Journal}
}


-- 4. Find all the papers written by a given author that where published in database conferences.
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lab2: <http://sdmlab2.org/>
SELECT (?pTitle as ?paper_title) (?pName as ?proc_name)
WHERE
{
    ?paper      rdf:type                lab2:Paper ;
                lab2:paperTitle         ?pTitle ;
                lab2:isPublishedInProc  ?proceeding .
    
    ?author     rdf:type                lab2:Author ;
                lab2:authorName         "J. Tate" ;
                lab2:writes             ?paper .
    
    ?proceeding lab2:procName           ?pName ;
                lab2:hasProcDomain      ?domain.
    
    ?domain     rdf:type                lab2:Domain ;
                lab2:domainName         "Database" .
}


-- 5. Find all editors who handle journals whose domain is "Engineering"
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lab2: <http://sdmlab2.org/>
SELECT (?eName as ?reviewer_name) (?jTitle as ?journal_title)
WHERE
{
    ?editor		rdf:type            lab2:Editor ;
    			lab2:authorName     ?eName ;
                lab2:handles        ?journal.
    
    ?journal    rdf:type            lab2:Journal ;
    			lab2:journalTitle   ?jTitle ;
                lab2:inVol          ?volume .
    
    ?volume     rdf:type            lab2:Volume ;
                lab2:hasVolDomain   ?domain.
    
    ?domain 	rdf:type            lab2:Domain ;
            	lab2:domainName     "Engineering" .
}


-- 6. Find all reviewers who give reviews to papers whose domain is "Business"
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lab2: <http://sdmlab2.org/>
SELECT (?rName as ?reviewer_name) (?pTitle as ?paper_title)
WHERE
{
    ?reviewer	rdf:type        	lab2:Reviewer ;
    			lab2:authorName 	?rName ;
    			lab2:gives 			?review .
    
    ?review     rdf:type        	lab2:Review ;
       		    lab2:isGivenTo  	?paper .
    
    ?paper   	rdf:type			lab2:Paper;
    			lab2:paperTitle		?pTitle ;
    			lab2:hasPaperDomain ?domain .
    
    ?domain 	rdf:type			lab2:Domain ;
            	lab2:domainName 	"Business" .
}