def replace_value(values, index, new_value):
    values[index]=new_value
    return None
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1
def summarize(values):
    return min(values),max(values),sum(values)
numberdays=int(input("Enter the number of days:"))
original=[]
for i in range(numberdays):
    numberphonecalls=int(input("Enter the number of phone calls:"))
    original.append(numberphonecalls)
updated=original[:]
wantedday=int(input("Enter the index to correct:"))
wantednumbercalls=int(input("Enter the new number of calls:"))
replace_value(updated,wantedday,wantednumbercalls)
searchfor=int(input("Enter the number of calls to search for: "))
target=searchfor
find_first(updated,target)
saved=find_first(updated,target)
updated.count(target)
savedupdated=updated.count(target)
summarized=summarize(updated)
minimum, maximum, total = summarized
sortedupdated=sorted(updated)
print(f"Original:{original}")
print(f"Updated:{updated}")
print(f"Sorted:{sortedupdated}")
print(f"Minimum number of calls: {minimum}")
print(f"Maximum number of calls:{maximum}")
print(f"Total number of calls:  {total}")
if saved != -1:
    print(f"First matching index: {saved}")
else:
    print("Target not found")
print(f"Matching values: {savedupdated}")
