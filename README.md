# Topological Analysis of Narrative Network
Using an open source Python tool (SpaCy), we analysed the Dependency of the vocabulary based on natural language processing techniques
and refined it using the Anaphora Resolution algorithm to extract SVO Triples.Two Samples T Test was used to filter the feature verbs. The SVO Triples with high relevance to the topic are retained.The topological analysis was carried out based on graph theory to investigate the centrality of the nodes and the scale-free nature of the graph. Extracting the scale-free scale-free network’s story framework and summarised the content features of crime news based on the interaction between the core characters.<br><br>

In this GitHub project, I uploaded two key Py files, nameed SVO_Extractor and SVO_Network separately. The function of former one is extracting subject-verb-object triples from text, and SVO_Network will transform the triples into a narrative network to support the following topological analysis.


## Instructions about usage of this SVO_Extractor
This method uses the en_core_web_sm corpus package in SpaCy to define the Dependency of words in a sentence. The subject predicate and object of the sentence are then extracted according to the grammatical features of English itself. This code can be used to refine the knowledge graph, the main story frame of a narrative text, and also for temporal extraction.<br>
### 1.Check the validation of libraries
Ensure that nltk, en_core_web_sm, SpaCy are installed when using this extractor.<br>


### 2.Import functions from code
Add the following code to a new project.<br><br>
<i>from SVO_Extractor import</font> extract_triple_list</i><br>


### 3.Explaination of the function 
The input is the path of the text file. You need to ensure that the format of the file is txt and the language must be English. <br><br>
The output is the SVO triples extracted from the file and stored in the list.<br><br>
For example:<br><br>
<i>final_triples=extract_triple_list("/Users/Desktop/NLP/target_file.txt")</i><br>
