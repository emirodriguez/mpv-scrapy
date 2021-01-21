import schedule
import db_check

# schedule crawler
schedule.every(30).minutes.do(db_check.check_result_send_mess)

# run script infinitely
while True:
    schedule.run_pending()