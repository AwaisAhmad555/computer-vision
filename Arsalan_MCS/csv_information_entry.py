import pandas as pd
import numpy as np
import os
import pymysql



dataFrame = pd.read_csv("car table.csv")


print(len(dataFrame.values))

print(dataFrame.shape)

print()

try:
    connection = pymysql.connect(host="localhost",
                                 user="root",
                                 password="",
                                 database="test",
                                 port=3306
                                 )

    cursor = connection.cursor()

    print("Connection Successful !")
    #print(connection.server_status)

    query_values = []

    for i in range(len(dataFrame.values[:,0])):


        for j in range(len(dataFrame.values[0, :])):

            query_values.append(dataFrame.values[i, j])

            pass

        insert_query = "INSERT INTO car_detail(Registration_No, Chassis_Number, Engine_Number, Model, Registration_Date, Token_Paid, Owner_Name, Color, Company, Fuel_Type, Engine_Capacity, Vehicle_price, Latest_payment_details) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # values = (first_name, last_name, contact, email, security_question, security_answer, password)
        values = query_values

        cursor.execute(insert_query, values)

        connection.commit()

        query_values.clear()


        pass




    connection.close()

    pass

except Exception as exp:


    print(exp)



    pass