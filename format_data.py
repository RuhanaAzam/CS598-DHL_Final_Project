
import numpy as np
import pandas as pd
import statistics
# import nltk
# nltk.download('punkt')

note_path = "./physionet.org/files/mimiciii/1.4/NOTEEVENTS_SMALLEST.csv" #MODIFY
metamap_path = "./MetaMAP/NOTEEVENTS_SMALLEST.csv" #MODIFY
lab_path = "./physionet.org/files/mimiciii/1.4/LABEVENTS.csv"
diag_path = "./physionet.org/files/mimiciii/1.4/DIAGNOSES_ICD.csv"

note = pd.read_csv(note_path, header=0)
metamap = pd.read_csv(metamap_path, header=0)
print("notes loaded...")

diag = pd.read_csv(diag_path, header=0)
print("diagnosis loaded...")

#combine NOTEEVENTS with corresponding metamap terms
note["TEXT"] = metamap["TEXT"]

#filter data by 'Discharge Summary' rows only
note[note['CATEGORY'] == 'Discharge summary']

#group ICD_Codes
diag = diag[["SUBJECT_ID", "HADM_ID", "ICD9_CODE"]]
diag = diag.dropna()
diag = diag.groupby(["SUBJECT_ID", "HADM_ID"], as_index=False)['ICD9_CODE'].agg(lambda x: list(x))#.apply(list)
print("ICD9_Codes aggregated...")

#join by SUBJECT_ID and HADM_ID
data = note.merge(diag, how='left', left_on = ["SUBJECT_ID", "HADM_ID"], right_on=["SUBJECT_ID", "HADM_ID"])
print("databases merged...")

data = data[["SUBJECT_ID", "HADM_ID", "ICD9_CODE", "TEXT"]]
#print(data)
#print(data.dtypes)

#calculating data stats
#might be interesting to see
print("Database Statistics: ")
num_p = len(data["SUBJECT_ID"].unique())
num_ad = len(data["HADM_ID"])
ad_count = data.groupby(["SUBJECT_ID"], as_index=False)["HADM_ID"].agg('count')
mean_ad, var_ad = statistics.mean(ad_count['HADM_ID']), statistics.variance(ad_count['HADM_ID'])
print("# of Patients: " + str(num_p))
print("# of visits total: " + str(num_ad))
print("# visits per Patient: " + str(mean_ad) + " +-" + str(var_ad))


# #convert "TEXT" into tokens
# data["TEXT"] = data.apply(lambda row: nltk.word_tokenize(row["TEXT"]), axis=1) #this step will be unneccessary with MetaMAP
# print("converted TEXT to token list...")
# # 	#print(data.iloc[0,:])
# # 	data["TEXT"] = data.apply(lambda row: row["TEXT"].split("Discharge Diagnosis")[-1].split("Discharge Condition")[0], axis=1)
	
# # 	# #print(len(data.iloc[0,:]["TEXT"].split("Discharge Diagnosis")))
# # 	# for i in range(len(data)):
# # 	# 	print(len(data.iloc[i,:]["TEXT"].split("Discharge Diagnosis")))
# # 	return data
# #print(data["ICD9_CODE"])
# print(data["TEXT"])
# #data = get_diagsum(data)
# #print(data.dtypes)

#convert in NUMPY type
np_data = data.to_numpy()

#save as .npy file
outfile = "./mimic_III.npy" #MODIFY
np.save(outfile, np_data ,allow_pickle=True)
print("\nSaved to " + str(outfile) + "!")
#print(np_data)

# #double check that it loads correctly
# out = np.load("data_small.npy", allow_pickle=True)
# print(out)

