# Topological Analysis of Narrative Network



## Instructions about usage of this extractor
This method uses the en_core_web_sm corpus package in SpaCy to define the Dependency of words in a sentence. The subject predicate and object of the sentence are then extracted according to the grammatical features of English itself. This code can be used to refine the knowledge graph, the main story frame of a narrative text, and also for temporal extraction.<br>
## 1.Check the validation of libraries
Ensure that nltk, en_core_web_sm, SpaCy are installed when using this extractor.<br>


### 2.Import functions from code
Add the following code to a new project.<br><br>
<i>from SVO_Extractor import</font> extract_triple_list</i><br>


### 3.Explaination of the function 
The input is the path of the text file. You need to ensure that the format of the file is txt and the language must be English. <br><br>
The output is the SVO triples extracted from the file and stored in the list.<br><br>
For example:<br><br>
<i>final_triples=extract_triple_list("/Users/Desktop/NLP/target_file.txt")</i><br>
