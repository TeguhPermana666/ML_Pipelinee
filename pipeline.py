"""
Pipeline adalah cara sederhana untuk menjaga prapemrosesan data dan kode pemodelan Anda tetap teratur. Secara khusus, pipeline menggabungkan 
langkah-langkah prapemrosesan dan pemodelan sehingga Anda dapat menggunakan seluruh bundel seolah-olah itu adalah satu langkah.

Banyak ilmuwan data meretas model tanpa pipeline, tetapi pipeline memiliki beberapa manfaat penting. Diantaranya:.

-cleaner code:
Akuntansi data pada setiap langkah prapemrosesan bisa menjadi berantakan. 
Dengan pipeline, Anda tidak perlu melacak data pelatihan dan validasi secara manual di setiap langkah.

-fewer bug:
peluang untuk salah dalam penerapan langkah di setiap pemprosesan lebih sedikit

-Easier to Productionize:
kesulitan dalam mentrasisikan dari prototype ke dalam sebuah penerapan skala besar dengan pipeline masalah
tersebut dapat di selesaikan dengan mudah

-More options for data validation
ada banyak jenis option untuk memvalidasi data contohnya adalah teknik
cover cross-validasi

"""
import pandas as pd
from sklearn.model_selection import train_test_split
#read the data
file_data="Intermediate_ml\melb_data.csv"
data=pd.read_csv(file_data)
#spreate target from predictions
y=data.Price
X=data.drop(['Price'],axis=1)
#devide data to train and validation data
X_train_full,X_valid_full,y_train,y_valid=train_test_split(X,y,train_size=0.8,test_size=0.2,random_state=0)
#cardinality=>unique value yang ada pada column
#=>select data object with the low cardinality->mencari nilai pada column yang paling banyak yang sama
categorical_cols=[cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and X_train_full[cname].dtype == 'object']
#=>select data numeric 
numerical_cols=[cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64','float64']]

#keep selected columns only
my_cols=categorical_cols+numerical_cols
X_train=X_train_full[my_cols].copy()
X_valid=X_valid_full[my_cols].copy()
print(data)
print(data['Type'].nunique())
print(data['Method'].nunique())
print(data['Regionname'].nunique())
print(categorical_cols)
print(numerical_cols)
print(my_cols)

#Pada data yang ditampilkan terdapat sebuah data pada column yang bertipe categorial dan missing value
#=>dengan penerapan pipline maka masalah tersebut bisa diatasi
#->tiga tahap dalam penerapan pipeline:

#1.Define processing proses
"""
mirip dengan bagimana sebuah pipline membandle sebuah preprocessing dengan modeling 
=> CoulumnTransformer digunakan untuk membundle sebuah steps preprocessing yang berbeda

->imputes missing values in numerical data, and
->imputes missing values and applies a one-hot encoding to categorical data.
"""
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

#Preprocessing for numerical data
numerical_transfor=SimpleImputer(strategy="constant")

#Preprocessing for categorical data
categorical_transfor=Pipeline(steps=[
    ("imputer",SimpleImputer(strategy='most_frequent')),
    ("onehot",OneHotEncoder(handle_unknown='ignore'))
])
# Bundle preprocessing for numerical and categorical data
preprocessor=ColumnTransformer(transformers=[
    ('num',numerical_transfor,numerical_cols),
    ('cat',categorical_transfor,categorical_cols)
])
print("Tahap 1:\n")
print(numerical_transfor)
print(categorical_transfor)
print(preprocessor)

#2.Define the model
from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor(n_estimators=10,random_state=0)

#3.create and evaluate pipeline
"""
Terakhir, kami menggunakan kelas Pipeline untuk mendefinisikan pipeline 
yang menggabungkan langkah-langkah prapemrosesan dan pemodelan. Ada beberapa hal penting yang perlu diperhatikan:

=>Dengan pipeline, kami melakukan praproses data pelatihan dan menyesuaikan model dalam satu baris kode. 
(Sebaliknya, tanpa pipeline, kita harus melakukan imputasi, one-hot encoding, 
dan pelatihan model dalam langkah-langkah terpisah. Ini menjadi sangat berantakan jika kita harus berurusan dengan variabel numerik dan kategoris!)    

=Dengan pipeline, kami menyediakan fitur yang belum diproses di X_valid ke perintah predict(), dan pipeline secara otomatis memproses fitur 
sebelum menghasilkan prediksi. (Namun, tanpa pipeline, kita harus ingat untuk melakukan praproses data validasi sebelum membuat prediksi.)
"""
from sklearn.metrics import mean_absolute_error
#bundle preprocessor and modeling code in pipeline
my_pipeline=Pipeline(steps=[
    ('preprocesor',preprocessor),
    ('model',model)
])
# Preprocessing of training data, fit model 
my_pipeline=my_pipeline.fit(X_train, y_train)
# Preprocessing of validation data, get predictions
preds=my_pipeline.predict(X_valid)
print(data['Price'])
print(preds)
#evaluate model
MAE=mean_absolute_error(y_valid, preds)
print(MAE)
"""
Pipeline berguna untuk membersihkan kode pembelajaran mesin dan menghindari kesalahan, dan sangat berguna untuk alur kerja dengan prapemrosesan data yang canggih.
"""