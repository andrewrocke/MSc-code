import ydf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split




ds = pd.read_csv("ML Test/output_left_singlelabel_add_del_NST.csv")
print("total dataframe :",ds.shape)
#X=ds['sAddress','rAddress']
#y= ds['IT_B_Label']

#X_train, X_test, y_train,  y_test = train_test_split(X,y ,  
                          #random_state=104, 
                          #train_size=0.8, shuffle=True)

mask = np.random.rand(len(ds)) < 0.8
train_ds = ds[mask] 
test_ds = ds[~mask] 

train_ds.shape, test_ds.shape 

train_ds.to_excel("train_ds.xlsx")

test_ds.to_excel("test_ds.xlsx")

#test_ds = ds.tf.take(1000)
#train_ds = ds.tf.skip(1000)
print("train_ds count :" ,len(train_ds))
#test_ds = pd.read_csv("ML Test/output_left.csv")
print("test_ds count :" , len(test_ds))
#train_ds = pd.read_csv("ML Test/output_left_23.csv")
print("train_ds :" ,train_ds.head(5))
#test_ds = pd.read_csv("ML Test/output_left.csv")
print("test_ds :" ,test_ds.head(5))
model = ydf.GradientBoostedTreesLearner(label="NST_B_Label").train(train_ds)
model.describe()
print(model.evaluate(test_ds))
#print(model.benchmark(test_ds))
#model.analyze(test_ds, sampling=0.1)
model.save("my_model")

loaded_model = ydf.load_model("my_model")