#formatt MetaMap's outputs to only contain mapping information
import json
import copy
import pandas as pd

file_name = "./test.out" #output file from MetaMap

with open(file_name, "r") as read_file:
    data = json.load(read_file)

docs = []
for i in range(len(data["AllDocuments"])):
	token_list = []
	utterances = data["AllDocuments"][i]["Document"]["Utterances"]
	for u in range(len(utterances)):
		phrases = utterances[u]["Phrases"]
		for p in range(len(phrases)):
			mappings = phrases[p]["Mappings"]
			for m in range(len(mappings)):
				word = mappings[m]["MappingCandidates"][0]["CandidateMatched"]
				score = mappings[m]["MappingCandidates"][0]["CandidateScore"] 
				#print(len(mappings[m]["MappingCandidates"])) #check how many mapping per phrase...
				#print(word + "\t" + str(score)) #NONE SCORE POSITIVE, but matching to positive numbers in non json type...

				token_list.append(word)
	docs.append(copy.deepcopy(token_list))
#paste the same way as pickling noteevent.csv...
#TODO

out_file = "./NOTEEVENTS.csv"
df = pd.DataFrame({'TEXT':docs})
df.to_csv(out_file,index=False)
print("File saved to " + str(out_file))

