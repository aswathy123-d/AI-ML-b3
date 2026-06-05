temperature = []
humidity = []

def avg_temp():
    global n
    average_temperature = sum(temperature)/n
    print(f"Average temperature :{average_temperature} ")


def avg_humi(): 
    global n
    average_humidity = sum(humidity)/n
    print(f"Average humidity :{average_humidity} ")   

def main():
   

    global n
    n = int(input("Enter number of days :"))
    for i in range(n):

        temp = float(input("Enter the day by day temperature : "))
        humi = float(input("Enter the humidity of each day : "))
        temperature.append(temp)
        humidity.append(humi)
    print(temperature)
    print(humidity)

    if temp < 20 and humi > 60:
        print("It is rainy")
    else:
        print("It is sunny")
    avg_temp()
    avg_humi()        
main()

