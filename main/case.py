# місце для твого коду

import pandas as pd

df = pd.read_csv("IMDB-Movie-Data.csv")

#df["Director"].item()

a = df[df["Revenue (Millions)"] == df["Revenue (Millions)"].max()]["Director"].item()
print(a)

# надрукувати режисера в якого найбільший дохід
# результат: 50    J.J Abrams

# якщо використати метод item() - виведеться тільки J.J Abrams 