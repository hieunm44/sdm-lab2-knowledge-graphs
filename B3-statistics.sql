-- Classes
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?class
FROM <http://localhost:7200/sdmlab2/>
WHERE {
    ?class a rdfs:Class
}
ORDER BY ?class

-- Properties

SELECT  DISTINCT ?p
FROM <http://localhost:7200/sdmlab2/>
WHERE{ 
    ?s ?p ?o
}

-- Total number of instances
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT (COUNT(?s) AS ?totalNumberOfInstances)
FROM <http://localhost:7200/sdmlab2/>
WHERE { 
    ?s rdf:type ?class .
    ?class rdf:type rdfs:Class . 
} 

-- Total number of triples
SELECT (COUNT(*) as ?Triples) 
FROM <http://localhost:7200/sdmlab2/>
WHERE { 
    ?s ?p ?o 
} 

-- Count of instances per class
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?class (COUNT(?s) AS ?totalNumberOfInstances)
FROM <http://localhost:7200/sdmlab2/>
WHERE { 
    ?s rdf:type ?class .
    ?class rdf:type rdfs:Class . 
} 
GROUP BY ?class
ORDER BY DESC(?totalNumberOfInstances)