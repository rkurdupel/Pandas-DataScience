import pandas as pd
df = pd.read_csv('GoogleApps.csv')
print(df)

# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?

print(df[df["Type"] == "Paid"]["Price"].min())
# Type = "Paid" - пошуковий запит знайти Paid
# Чому дорівнює медіанна (median) кількість установок (Installs)
print(df[df["Category"] == "ART_AND_DESIGN"]["Installs"].median())
# додатків із категорії (Category) "ART_AND_DESIGN"?


# На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
# більше максимальної кількості відгуків для платних програм (Type == 'Paid')?
print(df[df["Type"] == "Free"]["Reviews"].max())
print(df[df["Type"] == "Paid"]["Reviews"].max())
print(44893888 - 190086)


# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')?
#print(df[df["Content Rating"] == "Teen"]["Size"].min())



# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?

get_max_review = df["Reviews"].max() # отримати найбільшу кількість  відгук
get_game = df[df["Reviews"] == get_max_review]["App"] # отримати додаток в якого найбільше відгуків


get_category = df[df["App"] == "Clash of Clans"]["Category"]  # отримати категорію додатка
print(get_category)

print(df["Reviews"].max())  # отримати максимальну кількість відгуків
min_reviews = df["Reviews"].min()   # отримати мінімальну кількість відгуків

#print(type(get_game))  # надрукувати тип значення змінної get_game, результат (result) : <class 'pandas.core.series.Series'>        
# Series - перевіряє тільки один рядок, DataFrame всю табличку, всі данні в файлі

#print(df["Category"])  # надрукувати всі дані з стовпчика Category (надрукується 5 перший, 5 останніх)
#print(df["Reviews"].head(56))   # надрукувати 56 (від 0 (включно) - 55 (включно)) даних з стовпчика за допомогою head(56)
#print(df["Rating"].tail(26))    # надрукувати 26  останніх данних з стовпичка (7326 (включно) - 7351 (включно)) за допомогою tail(26)


# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# з кількістю установок (Installs) понад 10000?
print(df[(df["Price"] > 20) & (df["Installs"] > 10000)]["Rating"].mean())   # ціна > 20 ["Price"] > 20, кількість завантажень (Installs) > 10000 ["Installs"] > 10000, та отримати середній рейтинг (Rating) (mean()) ["Rating"].mean()


#a = df[(df["Price"] > 20) and (df["Installs"] > 1000)]["Rating"].mean()
#a = print(df[df["Price"] > 20] & ["Installs"] > 1000["Rating"].mean())
#print(a)
