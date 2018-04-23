import numpy as np
import pandas as pd
import plotly as ply

class Continuous:
    
    def __init__(self,fileCSV=None):
        
        if fileCSV is None:
            self.pathBank = './dataset/dataset.csv'
            self.fileCSV = pd.read_csv(filepath_or_buffer=self.pathBank,delimiter = ',', header=0, index_col=1)
        else:
            self.fileCSV = fileCSV
            
        self.continuous = self.fileCSV.select_dtypes(include=[np.number])
        self.pathFileResult = './results/DQR-ContinuousFeatures.csv';
        
    def get_continuous(self):
        print("continuous : ",self.continuous)
        
        if self.continuous is not None:
            return self.continuous
        else:
            return pd.read_csv(filepath_or_buffer=self.pathFileResult)
    
    def write_results(self):
        pd.DataFrame(self.continuous).to_csv(path_or_buf=self.pathFileResult)
        
    def draw_DQR(self):
        
        for feature in self.get_continuous().items():
            
            feature_name = feature[0]
            print(feature[0])
#            count
#            miss_pourcentage
#            cardinality
#            min_value
#            first_quarter
#            mean
#            median
#            third_quarter
#            max_value
#            std_dev

cont = Continuous();
cont.draw_DQR();
