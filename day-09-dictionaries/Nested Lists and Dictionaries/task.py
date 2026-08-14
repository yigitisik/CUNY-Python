vlogs = {
    "Germany": ["Dortmund", "Munich", "Cologne"],
    "Belgium": ["Antwerp", "Bern", "Gent"],
}

print(vlogs.get("Belgium", ["Not found", ""])[1])  # Outputs "Bern"
print(vlogs.get("France", ["Not found", ""])[1])   # Outputs ""
