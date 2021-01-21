import schedule
import db_check
import time

# schedule crawler
schedule
schedule.every(1).seconds.do(db_check.check_result_send_mess)

# run script infinitely
while True:
    schedule.run_pending()
    time.sleep(1)