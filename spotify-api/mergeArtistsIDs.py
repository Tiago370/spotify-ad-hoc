artistsIDs = []
with open('IDs/artists/artistsIDs_10001.txt', 'r') as f:
    for line in f:
        line = line.replace('\n', '')
        artistsIDs.append(line)
artistsIDs = list(set(artistsIDs))
with open('IDs/artists/artistsIDs_20047.txt', 'r') as f:
    for line in f:
        line = line.replace('\n', '')
        artistsIDs.append(line)
artistsIDs = list(set(artistsIDs))
with open('IDs/artists/30825_ok.txt', 'r') as f:
    for line in f:
        line = line.replace('\n', '')
        artistsIDs.append(line)
artistsIDs = list(set(artistsIDs))
print("Total artists:", len(artistsIDs))
artistsIDs = sorted(artistsIDs)
with open('IDs/artists/artistsIDs_30825.txt', 'w') as f:
    for line in artistsIDs:
        f.write(line + '\n')