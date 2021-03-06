# BreakingBERT@IITK at SemEval-2021
# Introduction

Task 9 : Statement Verification and Evidence Finding with Tables

Recently, there has been an interest in factual
verification and prediction over structured data
like tables and graphs. To circumvent any false
news incident, it is necessary to not only model
and predict over structured data efficiently but
also to explain those predictions. In this paper, as part of the SemEval-2021 Task 9, we
tackle the problem of fact verification and evidence finding over tabular data. There are two
subtasks. Given a table and a statement/fact,
subtask A determines whether the statement is
inferred from the tabular data, and subtask B
determines which cells in the table provide evidence for the former subtask. We make a comparison of the baselines and state-of-the-art approaches over the given SemTabFact dataset.
We also propose a novel approach CellBERT
to solve evidence finding as a form of the Natural Language Inference task. We obtain a 3-
way F1 score of 0.69 on subtask A and an F1
score of 0.65 on subtask B.


Subtask 1: 2 way Classification of the statements as Entailed and Refuted and 3 way Classification of the statements as Entailed, Refuted and Unknown

Subtask 2: Classifying the Cells as the Relevant and Irrelevant
            
           
# Corpus Description

The corpus has two versions of training data:
- [Manual Dataset](https://drive.google.com/file/d/1yObzEEZJ8qM7ZjrMcbtKZ-jofpL820ft/view)
- [Autogenerated Dataset](https://drive.google.com/file/d/1fz-g3wmAIwav_wQoF9t64NXEuQwyInZq/view)

For more information refer [this](https://sites.google.com/view/sem-tab-facts)

# Requirements
- Python 3.5
- Pytorch 1.2.0
- Pytorch_Pretrained_Bert 0.6.2 (Huggingface Implementation)
- Pandas
- tqdm-4.35
- TensorboardX
- unidecode
- nltk: wordnet, averaged_perceptron_tagger

# Preprocessing Data
**Preprocessing for Table transformers**

Refer this **Preprocessing_Code.ipynb** notebook.

The folder "data" contains the raw data given by Semeval organization. We included the modified version dataset **(D1)** which contained the Manual dataset along with the Autogenerated statements. Autogenerated statements that have common tables with
the manual dataset were used to create this version. For complete raw version refer corpus description above.
These two files in total contains roughly **72k** statements, the positive and negative satements are balanced
Use the following code to perform entity linking on raw dataset.
```sh
!python preprocess_data.py
```
Tokenization was performed on the preprocess data.
```sh
!python preprocess_BERT.py --scan horizontal
```

**Preprocessing for TAPAS**

Same as that of TableBERT.

# TableSciBERT

Training the model on train.tsv and dev.tsv fle.
```sh
!python "run_SciBERT.py" --do_eval --do_train --scan horizontal --fact first --output_dir output folder --train_batch_size 6 --period 3000 --bert_model "allenai/scibert_scivocab_uncased" --learning_rate 0.00001
```

# Tapas
For this download the tapas code from its main repository and follow the tapas collab.
```sh
!git clone https://github.com/google-research/tapas
```

Since the Model is quite big, the finetuned model is privately stored in the Google cloud.
# Heuristic
Tapas using Table Pruning to handle Large Tables and large statements.

# CellBERT
Train CellBERT using CellBERT_train.py and evaluate using CellBERT_eval.py

# How to cite
You can cite our ACML 2021 [paper](https://arxiv.org/abs/2104.03071) for the latest work on table based statement verification.

# Contact information
For help or issues, please submit a GitHub issue.


