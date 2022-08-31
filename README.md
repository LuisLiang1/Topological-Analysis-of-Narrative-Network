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

## Instructions about usage of this SVO_Network

### 1.Check the validation of libraries
Ensure that networkx and collections are installed when using this extractor.<br>

### 2.Import functions from code
Add the following code to a new project.<br><br>
<i>from SVO_Network import</font> net_graph_data</i><br><br>
net_graph_data is used to clean the triples and conduct a rough data pre-processing.<br><br>
<i>from SVO_Network import</font> draw_net_graph</i><br><br>
draw_net_graph is used to draw the network according to the triples.<br><br>

### 3.Explaination of the function 
For net_graph_data, the input is the triples stored in list and the two results will be generated, named triples_after_clean and the count_result seperately.<br><br>
For example:<br><br>
<i>triples_after_clean,count_result=net_graph_data(triples)</i>
<br><br>
For draw_net_graph, the input includs two parameters, which are exactly the outputs of net_graph_data. The output of this function is a graph.
<br><br>
For example:<br><br>
<i>draw_net_graph(triples_after_clean,count_result)</i>
<br><br>
