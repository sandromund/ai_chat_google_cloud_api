import requests

resp = requests.post("https://index-zawl3fkjca-ew.a.run.app",
                     files={'text': "Hallo wie geht es dir?"})

print(resp.json())