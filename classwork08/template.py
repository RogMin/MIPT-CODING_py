import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#TODO: Вариант 10, Минченков Егор

def task1(x,y):
    # TODO: первое задание
    print((x**2) - (y**2))

def task2(str):
    # TODO: второе задание
    count = 0
    for x in list(str):
        print(x)
        if x.isupper():
            count += 1
    print(count)
def task3(arr):
    # TODO: третье задание
    print(list([for b in list(arr.split(' ')) if (b.Contain("sus"))]))

def task5(list_of_smth):
    # TODO:
    print(list_of_smth[len(list_of_smth)-5:1:-3])

def task6(list1, list2, list3, list4):
    # TODO: пятое задание
    print(set(list1) & set(list2) & set(list3) & set(list4))


def task7(seed = 10):
    # TODO: ...
    np.random.seed(10)
    matrix = np.asmatrix((np.random.randint(0,25,(5,5))))
    return(matrix, np.linalg.det(matrix))

def task8(f, min_x, max_x, N, min_y, max_y):
    # TODO: ...
    x = np.linspace(min_x,max_x,N)
    y = f(x)
    y = y[min_y:max_y]
    plt.grid(which='major', axis='both', alpha=1)
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(x,y, "g-",x, np.diff(y) / np.diff(x))
    plt.savefig('function.png')
    plt.show()

def task12(filename="video-games.csv"):
    # TODO: ...
    dict = {}
    df = pd.read_csv(filename)
    #1:
    dict["n_games"] = df.shape[0]
    #2:
    dict["by_years"] = df.groupby("year")["year"].count()
    #3:
    pub = (df[df.publisher == "EA"].groupby("publisher").agg({"price": "mean"}))
    dict["mean_price"] = pub
    #4:
    dict["age_max_price"] = df.groupby("age_raiting")["price"].max()
    #5:
    newdf = df[(df.max_players == 1) | (df.max_players == 2)].groupby("max_players").agg({"review_raiting": "mean"})
    dict["mean_raiting_1_2"] = newdf
    #6:
    newdf = df.groupby("price")["age_raiting"].min()
    newdf["max"] = df.groupby("price")["age_raiting"].max()
    dict["min_max_price"] = newdf
    print(dict)



task12()
