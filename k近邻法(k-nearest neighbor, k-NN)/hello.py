from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
x=[[1],[2],[3],[4],[5],[6],[7]]
y=[1,0,1,0,1,0,1]
x_train,x_test,y_train,y_test = train_test_split(x,y)
standardScaler = StandardScaler()
standardScaler.fit(x_train)
print(x_train)
print(x_test)
print(y_train)
print(y_test)
x_train = standardScaler.transform(x_train)
x_test = standardScaler.transform(x_test)
print(x_train)
print(x_test)
sklearn_knn_clf = KNeighborsClassifier(n_neighbors=2)
sklearn_knn_clf.fit(x_train,y_train)
score = sklearn_knn_clf.score(x_test,y_test)
print(score)
v = sklearn_knn_clf.predict([[2]])
print(v)