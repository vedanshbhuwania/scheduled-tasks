# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
import os
import requests
import smtplib
api_key="323554271b6141e671455bfa232d9a4f"
api_key_secret=os.environ.get("API_KEY")
parameters={
    "lat":22.565573,
    "lon":88.370215,
    "appid":api_key_secret,
    "cnt":4,
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
print(response.status_code)
response.raise_for_status()
weather_data=response.json()
weather_id=[]
for i in range(4):
    weather_id.append(weather_data["list"][i]["weather"][0]["id"])
print(weather_id)
for id in weather_id:
    if id<700:
        connection=smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        my_email="rashibhuwania20@gmail.com"
        password="kzzoaqehjyidxzrc"
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr="unknown_man@gmail.com",to_addrs=my_email,msg="Its going to Rain . Bring an umbrella")
        connection.close()
        break
