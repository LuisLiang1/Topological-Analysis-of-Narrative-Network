# SVO-Triples-Extraction
This method uses the en_core_web_sm corpus package in SpaCy to define the Dependency of words in a sentence. The subject predicate and object of the sentence are then extracted according to the grammatical features of English itself. This code can be used to refine the knowledge graph, the main story frame of a narrative text, and also for temporal extraction.

# Instructions about usage of this extractor
## 1.Check the validation of libraries
Ensure that nltk, en_core_web_sm, SpaCy are installed when using this extractor.<br>


## 2.Import functions from code
Add the following code to a new project.<br>
<font color="green"> from</font> SVO_Extractor <font color="green"> import</font> extract_triple_list<br>



