from src.Data_Ingestion import DataIngestion
from src.Data_Preprocessing import Preprocessing
from utils.model import load_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

# Data ingestion
data = DataIngestion(r"F:\TitanicE2E\data\data.csv")

# Feature–target split
x = data.drop(columns=['survived'])
y = data['survived']

# Train–test split
xtrain, xtest, ytrain, ytest = train_test_split(
    x, y, train_size=0.70, random_state=10
)

# Preprocessing
preprocessor_obj = Preprocessing(xtrain)
preprocessor = preprocessor_obj.run()

xtrain_preprocessed = preprocessor.fit_transform(xtrain)
xtest_preprocessed = preprocessor.transform(xtest)

# Model training
model = load_model()
model.fit(xtrain_preprocessed, ytrain)

# Evaluation
ypred = model.predict(xtest_preprocessed)
print("accuracy_score:", accuracy_score(ytest, ypred))
print("precision_score:", precision_score(ytest, ypred))
print("recall_score:", recall_score(ytest, ypred))
print("f1_score:", f1_score(ytest, ypred))

