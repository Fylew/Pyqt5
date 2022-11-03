import random
import datetime
def podshet_Tonn():
    date = datetime.datetime.now()
    line = 60
    proizvod = 950
    weight_beg = 500
    num_beg = 1
    if line == 60:
        proizvod += proizvod * 4.5/100

    for i in range(num_beg, 20):
        if i == num_beg:
            tonn_in_min = round((1000-weight_beg) / (proizvod / 60),2)
            print("Эту тонну нужно добить осталось {} минут(а)".format(round(tonn_in_min)))
        else:
            tonn_in_min = round(1000/ (proizvod / 60),2)
        date += datetime.timedelta(minutes=tonn_in_min)
        print("{} тонна будет готова в {}".format(i+1,date.strftime("%d.%m %H:%M")))

podshet_Tonn()