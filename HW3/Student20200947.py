import numpy as np
import os
import sys
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

training_folder = sys.argv[1]
test_folder = sys.argv[2]

training_files = os.listdir(training_folder)
test_files = os.listdir(test_folder)

training_data = []
test_data = []

# 훈련 데이터 생성
for file in training_files:
    if file.endswith(".txt"):
        file_path = os.path.join(training_folder, file)
        
        digit, data_id = map(int, file.split('.')[0].split('_'))
        
        with open(file_path, 'r') as f:
            file_data = [int(char) for char in f.read().replace('\n', '')]
            
            training_data.append([digit, data_id] + file_data)
            
columns = ['label', 'data_id'] + [f"{i}x{j}" for i in range(1, 33) for j in range(1, 33)]
training_df = pd.DataFrame(training_data, columns=columns)

X_train = np.array(training_df.iloc[:, 2:])
y_train = np.array(training_df['label'])

# 테스트 데이터 생성
for file in test_files:
    if file.endswith(".txt"):
        file_path = os.path.join(test_folder, file)
        
        digit, data_id = map(int, file.split('.')[0].split('_'))
        
        with open(file_path, 'r') as f:
            file_data = [int(char) for char in f.read().replace('\n', '')]
            
            test_data.append([digit, data_id] + file_data)

# 여기서 training_data 대신 test_data를 사용해야 함
test_df = pd.DataFrame(test_data, columns=columns)

X_test = np.array(test_df.iloc[:, 2:])
y_test = np.array(test_df['label'])

total_samples = len(y_test)

for k_value in range(1, 21):
    clf = KNeighborsClassifier(n_neighbors=k_value)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    error_rate = (1 - accuracy_score(y_test, y_pred))
    
    print(f'{int(error_rate * total_samples)}')