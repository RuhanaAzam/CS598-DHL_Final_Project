#This files converts NOTEEVENT.csv file in MIMIC-III dataset TEXT only that MetaMap can take as input
#Each seperate text entry is delimited by "\n"
import pandas as pd


file_name = "../physionet.org/files/mimiciii/1.4/NOTEEVENTS.csv" #path to NOTEEVENTS.csv file here
df = pd.read_csv(file_name, header=0)

print("Writing " + str(len(df)) +  " lines...")

with open('mimic_notes.txt', 'w') as f:
	for index, row in df.iterrows():
		string = row['TEXT'].replace('\n',' ')
		f.write(string)
		f.write('\n\n')

print("Done...")
