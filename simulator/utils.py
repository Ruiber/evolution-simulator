import os
import time
import pandas as pd


def export(reporter):
    file_name = int(time.time() * 1000)
    path = os.path.realpath(__file__)
    path = os.path.dirname(path)
    #TODO: tornar independente de OS
    path = path.replace('/simulator', '/output/' + str(file_name) + '.csv')
    pd.DataFrame(reporter).to_csv(path, index_label='Round')
