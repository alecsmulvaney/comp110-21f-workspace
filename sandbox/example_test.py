
schools = dict()

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150 
print(schools)

print(f"UNC has {schools['UNC']} students")

schools.pop("Duke")

is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)

schools = {}
print(schools)

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)


#print(schools["UNCC"])

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
    print(schools[school])

