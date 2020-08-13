from feynman.S_run_aifeynman import run_aifeynman
import tempfile, os, pdb

def solve(X,Y):
    assert len(X) == len(Y), 'uneven X,Y'
    with tempfile.NamedTemporaryFile(suffix='.csv', prefix=os.path.basename(__file__), mode = "w", delete=False) as tf:
        for it in range(len(X)):
            for val in X[it]:
                tf.write(f"{val}\t")
            tf.write(f"{Y[it]}\n")
        tf.close()
        tf_directory = os.path.dirname(tf.name)
    return run_aifeynman('', tf.name, BF_try_time=30,BF_ops_file_type='19ops.txt', polyfit_deg=4, NN_epochs=4000)

import numpy as np
X = [[np.random.uniform(-10, 10), np.random.uniform(-10, 10)] for i in range(10)]
Y = [np.sqrt(x[0] * x[0] + x[1] * x[1]) for x in X]
print(solve(X,Y))