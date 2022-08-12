import json
import os

f1 = open("./bigger_one_result_using_vito.json", "r")
f2 = open("./smaller_one_result_using_vito.json")

j1 = json.load(f1);
j2 = json.load(f2);

result = j1 + j2;
with open("./voice_phishing_data_using_vito.json", "w") as f :
    json.dump(result, f, ensure_ascii = False, indent = 4)

f1.close()
f2.close()
