install.packages("data.table")
install.packages("sqldf")
library(sqldf)
library(data.table)

appEvents = as.data.frame(fread("C:\\Users\\ryan\\kaggleTD\\app_events.csv", sep = ","))

train = as.data.frame(fread("C:\\Users\\ryan\\kaggleTD\\gender_age_train.csv", sep = ","))

test = as.data.frame(fread("C:\\Users\\ryan\\kaggleTD\\gender_age_test.csv", sep = ","))

events = as.data.frame(fread("C:\\Users\\ryan\\kaggleTD\\events.csv", sep = ","))

brand = as.data.frame(fread("C:\\Users\\ryan\\kaggleTD\\phone_brand_device_model.csv", sep = ","))

categories = as.data.frame(fread("C:\\Users\\ryan\\kaggleTD\\label_categories.csv", sep = ","))

train2 = sqldf("SELECT a.device_id, b.event_id, b.timestamp, b.longitude,
	b.latitude FROM train as a LEFT JOIN events as b on a.device_id = b.device_id")




















