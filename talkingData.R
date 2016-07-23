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

train$device_id = as.numeric(train$device_id)
brand$device_id = as.numeric(brand$device_id)
test$device_id = as.numeric(test$device_id)
events$device_id = as.numeric(events$device_id)
#group is a keyword in sql, change the y from group to response
names(train)[4] = "response"

events$timestamp = as.integer(as.POSIXct(events$timestamp))



train2 = sqldf("SELECT a.device_id, a.response, a.gender, a.age,   b.phone_brand, b.device_model
FROM train AS a LEFT JOIN brand AS b on a.device_id = b.device_id")


test2 = sqldf("SELECT a.device_id, b.event_id, SUM(b.timestamp)
FROM test AS a LEFT JOIN events AS b on a.device_id = b.device_id
GROUP BY 1")

