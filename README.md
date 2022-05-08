# Reproducibility of Harmonized Representation Learning on Dynamic EHR

This following is the code and instructions necessary for my attempt to reproduce the results from ["Harmonized representation learning on dynamic EHR graphs"](https://www.sciencedirect.com/science/article/pii/S153204642030054X) [1]. The original repo for the paper can be found [here](https://github.com/donalee/HORDE).

## Dataset
The experiments are run on the MIMIC-III dataset. Data access can be found after completing a training course and request access though [PhysioNet](https://physionet.org/). 

The MIMIC-III dataset should be place in `./physionet.org/files/mimiciii/1.4/` directory.

## Baseline Models
The baseline models use `Python 2.7` and share the following dependencies: `theano==1.0.5`, `sklearn==0.0`, `numpy==1.16.6`, `pandas==0.24.2`, `scipy==1.2.3`

### med2vec
The code for med2vec is slighly modified from it's [original implementation](https://github.com/mp2893/med2vec) base off the paper "Multi-layer Representation Learning for Medical Concepts" [2]. 

**Working Directory:**`cd med2vec`

**Preprocess MIMIC-III:** `python process_mimic.py ../physionet.org/files/mimiciii/1.4/ADMISSIONS.csv ../physionet.org/files/mimiciii/1.4/DIAGNOSES_ICD.csv MIMIC-III`

**Train + Evaluate Model:** `python med2vec.py MIMIC-III.seqs 4894 ./output/model --label_file MIMIC-III.3digitICD9.seqs --n_output_codes 942 --batch_size 100 `

### DoctorAI
The code for DoctorAI is slighly modified from it's [original implementation](https://github.com/mp2893/doctorai) base off the paper "Doctor AI: Predicting Clinical Events via Recurrent Neural Networks" [3]. 

**Preprocess MIMIC-III:** `python process_mimic.py ../physionet.org/files/mimiciii/1.4/ADMISSIONS.csv ../physionet.org/files/mimiciii/1.4/DIAGNOSES_ICD.csv MIMIC-III`

**Train + Evaluate Model:** `python doctorAI.py MIMIC-III.seqs 4894 MIMIC-III.3digitICD9.seqs 942 ./output/model`=

## HORDE
The code for this model is a slightly modified version from [HORDE-pytorch](https://github.com/Lishany/HORDE-pytorch) repository.

[WRITE THIS LATER]
`Python 3.7`, `numpy==`, `torch==`, `torch-geometric==`, `torch_sparse==`

### Extracting medical entities (via MetaMap)
1. Format the data for MetaMap: `cd MetaMap`, `python preprocess.py`. This will output a file named `mimic_notes.txt`.
2. Pass this file though National Library of Medicine (NLM) [Batch MetaMap](https://ii.nlm.nih.gov/Batch/UTS_Required/MetaMap.html) interface. You need permission and agree to comply with UMLS Metathesaurus License first. For my experiment, I chose two flags "Unformatted XML Output (`--XMLn`)" and "Word Sense Disambiguation (`-y`)". And retricted semantic types to the following `anab, comd, clnd, diap, dsyn, drdd, hops, horm, topp`.
3. Place the "text.out" file inside the MetaMap directory.
4. Format output file: `python postprocess.py`

This will leave`./MetaMap/NOTEEVENT.csv`. This is `NOTEEVENT.csv` except the text column only contains UMLS entities. 

### Running the Model
**Format data:** `python format_data.py`, `mv mimic_III.npy ./HORDE-pytorch/data`, `cd HORDE-pytorch` 

**Preprocess data:** `python process_data.py`

**Train + Evaluate Model:** `python main.py`

## Results
[ADD HERE]


## References
[1] D. Lee, X. Jiang, and H. Yu, “Harmonized representation learning on dynamic EHR graphs,” J. Biomed. Inform., vol. 106, no. November 2019, p. 103426, 2020.

[2] E. Choi et al., “Multi-layer representation learning for medical concepts,” Proc. ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., vol. 13-17-Augu, pp. 1495–1504, 2016.

[3] E. Choi, M. T. Bahadori, A. Schuetz, W. F. Stewart, and J. Sun, “Doctor AI: Predicting Clinical Events via Recurrent Neural Networks.,” JMLR Workshop Conf. Proc., vol. 56, pp. 301–318, 2016.

