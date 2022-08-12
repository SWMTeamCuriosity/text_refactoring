import csv
import json
import os

with open("./data/smaller_one.json", "r") as f:
    data = json.load(f);

with open("./data/bigger_one.json", "r") as f:
    data_second = json.load(f);

voice_phishing = data + data_second

voice_phishing_sentence = []
for i in voice_phishing :
    for j in (i["results"]["utterances"]) :
        if len(j["msg"]) > 2 :
            j.split(".")

print(len(voice_phishing_sentence))

directory = "./data/normal_data"
lists = os.listdir(directory)
normal_data = []
normal_data_sentences = []

for i in lists :
    with open(directory + "/" + i) as f :
        cur_list = json.load(f)
        normal_data += (list(cur_list.values()))

for i in normal_data :
    for j in i :
        if len(j) > 2 :
            normal_data_sentences.append(j)
print(len(normal_data_sentences))


with open("./result.csv", "w", newline="") as csv_file :
    writer = csv.writer(csv_file)
    for i in voice_phishing_sentence[:18000] :
        writer.writerow([i, True])
    for i in range(20000):
        writer.writerow([normal_data_sentences[i], False])

with open("./test.csv", "w", newline="") as csv_file :
    writer = csv.writer(csv_file)
    for i in voice_phishing_sentence[18000:] :
        writer.writerow([i])

with open("./tst_normal.csv", "w", newline="") as csv_file :
    writer = csv.writer(csv_file)
    for i in normal_data_sentences[20000:] :
        writer.writerow([i])


