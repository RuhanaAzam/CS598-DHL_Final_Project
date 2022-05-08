# Reproducibility of Harmonized Representation Learning on Dynamic EHR (HORDE)

This following is the code and instructions necessary for my attempt to reproduce the results from ["Harmonized representation learning on dynamic EHR graphs"](https://www.sciencedirect.com/science/article/pii/S153204642030054X) [1]. The oringal repo for the paper can be found [here](https://github.com/donalee/HORDE).

The experiments are run on the MIMIC-III dataset which can be found after completing the “Data or Specimens Only Research” [CITI training course](https://www.citiprogram.org/index.cfm?pageID=154&icat=0&ac=0) and submitting an request to access MIMIC-III though [PhysioNet](https://physionet.org/). The files of the dataset are expected to be contained this this directory `./physionet.org/files/mimiciii/1.4/`.

## Baseline Models
The two baselines model utilize are run with `Python 2.7`. The dependencies are the following: `theano==1.0.5`, `sklearn==0.0`, `numpy==1.16.6`, `pandas==0.24.2`, `scipy==1.2.3`.

### med2vec

### DoctorAI

## HORDE

### Extracting medical entites (via MetaMap)
To train the HORDE model, we are interesting in untilizing clinical notes but only medical entities. MetaMap will allow us to extract unified medical language system (UMLS) only.

1. Format the data for MetaMap: `cd MetaMap`, `python preprocess.py`. This will output a file named `mimic_notes.txt`.
2. Pass this file though National Library of Medicine (NLM) [Batch MetaMap](https://ii.nlm.nih.gov/Batch/UTS_Required/MetaMap.html) interface. You need permission and agree to comply with UMLS Metathesaurus License first. For my experiment, I chose two flags "Unformatted XML Output (`--XMLn`)" and "Word Sense Disambiguation (`-y`)". And retricted semantic types to the following `anab, comd, clnd, diap, dsyn, drdd, hops, horm, topp`.
3. Place the "text.out" file inside the MetaMap directory.
4. Format output file: `python postprocess.py`

This will leave`./MetaMap/NOTEEVENT.csv`. This is `NOTEEVENT.csv` except the text column only contains UMLS entities. 

