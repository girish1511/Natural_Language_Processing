from keras_bert import extract_embeddings
import tensorflow as tf
import numpy as np
from tempfile import TemporaryFile

flags = tf.compat.v1.flags
FLAGS = flags.FLAGS

flags.DEFINE_string("input_file", None, "")

outfile = TemporaryFile()


BEFORE_CANCER_PATH = "/home/chennuri/CliNER/bef_canc_mod_treatments/"
BIO_BERT_PATH = '/home/gowtham/biobert_v1.1_pubmed'

with open(BEFORE_CANCER_PATH + file_name, 'r') as f:
	data = f.readlines()
	f.close()

output = extract_embeddings(BIO_BERT_PATH, data)
np.save(outfile, output)