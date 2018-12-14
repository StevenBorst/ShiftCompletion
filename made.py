from datetime import datetime
import threading

def get_made():
  threading.Timer(5.0, get_made).start()
  start= datetime(2018, 12, 14, 11, 00, 0)
  end= datetime(2018, 12, 14, 14, 00, 0)
  total= (end - start).total_seconds()
  now = datetime.now()
  seconds_since = (now - start).total_seconds()
  percent = seconds_since/total
  percent= percent*100
  percent = '%.2f' % percent
  rate = float(0.00388888888)
  made = rate*seconds_since
  made = '%.2f' % made
  print("Made: $", made, "Completion: ", percent, "%")

get_made()
