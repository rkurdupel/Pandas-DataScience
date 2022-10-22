import pandas as pd
df = pd.read_csv('GoogleApps.csv')
print(df)

#Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?

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

print(df[df["Reviews"] == df["Reviews"].max()]["Category"]) # надрукувати всю інформацію про додаток  в якого найбільше відгуків
# df["Reviews"].max() - з стовпчика Reviews отримати максимальну кількість відгуків за допомогою max()
# df["Reviews"] - отримати всі дані з стовпчика Review
# Category - категорія додатка

#get_max_review = df["Reviews"].max() # отримати найбільшу кількість  відгук
#get_game = df[df["Reviews"] == get_max_review]["App"] # отримати додаток в якого найбільше відгуків


#get_category = df[df["App"] == "Clash of Clans"]["Category"]  # отримати категорію додатка
#print(get_category)

#print(df["Reviews"].max())  # отримати максимальну кількість відгуків
#min_reviews = df["Reviews"].min()   # отримати мінімальну кількість відгуків

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
print(df[df['Reviews'] == df['Reviews'].max()]['Category'])

#print(df[df["Rating"] == df["Rating"].max()]["Category"])
#print(df[df["App"] == df["App"].mean()]["Category"])

print(df[df["Installs"] == df["Installs"].min()]["App"])    # надрукувати додатки (App) в який найменше скачувань (Installs)
print(df[df["Installs"] == df["Installs"].min()]["Rating"]) # надрукувати рейтинг додатків (Rating) в яких найменше скачувань (Installs)

for (index, row) in df.iterrows():  # пройтись по кожному рядку та стовпчику в файлі (csv) за допомогою цикла for та iterrows() - який дає змогу отримати всі індекси та рядки з файлу (csv)
    #print(index)    # надрукувати всі індекси (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ...., 7351) з файлу (csv)
    #print(row)      # надрукувати всі рядки та дані до кожного рядка з файлу (csv)

    #           7309
    #       App               BEBONCOOL GAMEPAD V1.0
    #       Category                            GAME
    #       Rating                               3.9
    #       Reviews                              404
    #       Size                                 2.2
    #       Installs                          100000
    #       Type                                Free
    #       Price                                  0
    #       Content Rating                  Everyone
    #       Last Updated             August 30, 2017
    #       Current Ver                          1.2
    #       Android Ver                   4.0 and up

    print(row["App"])   # надрукувати всі дані з стовпчика App з файлу (csv)    
    #print(row["Type"][index])

print(df.head(3))   # надрукувати перші три стовпчики з даними з файлу (csv)
print(df.tail(5))   # надрукувати п'ять останніх стовпчика з даними з файлу (csv)
print(df.describe())    # описати дані з файлу (csv) за допомогою describe()
print(df.mean())    # надрукувати середні арефметичні дані з файлу за допомогою mean()
print(df.max()) # надрукувати програму та її дані де всі дані максимальні з файлу (csv) за допомогою max()
print(df.min()) # надрукувати програму та її дані де усі дані мінімальні з файлу (csv) за допомогою min()
print(df.count())   # надрукувати кількість непустих значень з файлу (csv) за допомогою count()
