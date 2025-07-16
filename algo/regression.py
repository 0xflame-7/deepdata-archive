class Regressor:
  def __init__(self):
    self.a = None
    self.b = None


  def fit(self, X_train, Y_train):
    num = 0
    den = 0
    for i in range(len(X_train)):
      num += (X_train[i] - X_train.mean()) * (Y_train[i] - Y_train.mean())
      den += (X_train[i] - X_train.mean()) ** 2
    self.a = num / den
    self.b = Y_train.mean() - self.a * X_train.mean()

    print(self.a, self.b)

  
  def predict(self, X_test):
    return self.a * X_test + self.b