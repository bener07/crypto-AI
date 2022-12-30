from csv_updater import thread
from database.models import coins
from time import sleep

btc = coins.objects.get(id=1)
th = thread(btc, "info")
th.start()
print("Started!")
sleep(4)
print("Trying to kill")
th.kill()