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

app_labels = as.data.frame(fread("C:\\Users\\ryan\\kaggleTD\\app_labels.csv", sep = ","))




train$device_id = as.numeric(train$device_id)
brand$device_id = as.numeric(brand$device_id)
test$device_id = as.numeric(test$device_id)
events$device_id = as.numeric(events$device_id)

app_labels$app_id = as.numeric(app_labels$app_id)

#group is a keyword in sql, change the y from group to response
names(train)[4] = "response"

events$timestamp = as.numeric(as.POSIXct(events$timestamp))



train2 = sqldf("SELECT a.device_id, a.response, a.gender, a.age,   b.phone_brand, b.device_model
FROM train AS a LEFT JOIN brand AS b on a.device_id = b.device_id")


test2 = sqldf("SELECT a.device_id, b.event_id, SUM(b.timestamp) AS sumtime,
MAX(b.timestamp) AS maxtime, MIN(b.timestamp) AS mintime, AVG(b.timestamp)
AS avgtime, MAX(b.timestamp) - MIN(b.timestamp) AS deltatime
FROM test[1:10] AS a LEFT JOIN events AS b on a.device_id = b.device_id
GROUP BY 1")


t =sqldf("SELECT b.device_id, b.event_id, SUM(b.timestamp) AS sumtime,
MAX(b.timestamp) AS maxtime, MIN(b.timestamp) AS mintime, AVG(b.timestamp)
AS avgtime, MAX(b.timestamp) - MIN(b.timestamp) AS deltatime
FROM events AS b GROUP BY 1")





#used to evaluate unique keys
for (i in 1:ncol(train))
{
	print(length(unique(train[,i])))
	print(colnames(train)[i])
}



events2 = sqldf("SELECT events.event_id, events.device_id,
	events.timestamp, events.longitude, events.latitude,
	SUM(appEvents.is_installed) as totalinstalled 
	FROM events LEFT JOIN appEvents ON events.event_id = 
	appEvents.event_id 
	GROUP BY 1")



one = sqldf("
		(SELECT app_labels.app_id, app_labels.label_id, categories.category
		FROM app_labels LEFT JOIN 
		categories 
		ON app_labels.label_id = categories.label_id
		)one
		

	
		")
