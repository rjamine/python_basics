# code questions: 7, 8,

# code question 8
def update_log_list(log_list):
   for log in log_list:
      if log.get("app") == "webserver":
         log["level"] = "ERROR"
      if log.get("app") == "database":
         log["timestamp"] = "2023-12-07T11:50:00"
   return log_list

log_sample = [
   {"app": "webserver", "level": "argh", "message": "Critical error", "timestamp": "2023-12-07T11:55:00"},
   {"app": "database", "level": "ERROR", "message": "Database connection lost", "timestamp": "me time"}]

print(update_log_list(log_sample))

