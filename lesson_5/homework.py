# Task 1
print("--------------- Task 1 ----------------")

def _convert_cel_to_far(celcious):
    return round(celcious * 9/5 + 32, 2)

def _convert_far_to_cel(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

fahrenheit = int(input("Enter a temperature in degrees F: "))
print(f"{fahrenheit} degrees F = {_convert_far_to_cel(fahrenheit)} degrees C.")
celcious = int(input("Enter a temperature in degrees C: "))
print(f"{celcious} degrees C = {_convert_cel_to_far(celcious)} degrees F.")


# Task 2
print("--------------- Task 2 ----------------")

def invest(*, amount, rate, years):
    sumOfMoney = amount
    for year in range(years):
        sumOfMoney = round(sumOfMoney + (sumOfMoney / 100) * rate, 2)
        print(f"year {year+1}: ${sumOfMoney}")

invest(amount=100, rate=2, years=10)


# Task 3
print("--------------- Task 3 ----------------")

def factorsOfPositiveNumber():
    number = int(input("Enter a positive integer: "))

    for rangeNumber in range(number):
        if number % (rangeNumber+1) == 0:
            print(f"{rangeNumber+1} is a factor of {number}.")

factorsOfPositiveNumber()


# Task 4
print("--------------- Task 4 ----------------")
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def _enrollment_stats(listOfUniversities=[]):
    studentEnrollment = []
    tuitionFees = []

    for values in listOfUniversities:
        studentEnrollment.append(values[1])
        tuitionFees.append(values[2])

    return [
        studentEnrollment,
        tuitionFees
    ]

def _mean(listArg=[]):
    return sum(listArg)/len(listArg)

def _median(listArg=[]):
    listArg.sort()
    median = 0
    if len(listArg) % 2 == 0:
        median = listArg[int(len(listArg)/2+1)] + listArg[int(len(listArg)/2)] / 2
    else:
        median = listArg[int((len(listArg)-1)/2)]
    return median

totalStudents = format(round(sum(_enrollment_stats(listOfUniversities=universities)[0]), 2), ",")
totalTuition = format(round(sum(_enrollment_stats(listOfUniversities=universities)[1]), 2), ",")

studentMean = format(round(_mean(_enrollment_stats(listOfUniversities=universities)[0]), 2), ",")
studentMedian = format(round(_median(_enrollment_stats(listOfUniversities=universities)[0]), 2))

tutionMean = format(round(_mean(_enrollment_stats(listOfUniversities=universities)[1]), 2))
tuitionMedian =format(round(_median(_enrollment_stats(listOfUniversities=universities)[1]), 2))

print(f"Total students: {totalStudents}.")
print(f"Total tuition: $ {totalTuition}.")

print(f"Student mean: {studentMean}.")
print(f"Student median: {studentMedian}.")

print(f"Tution mean: {tutionMean}.")
print(f"Tution median: {tuitionMedian}.")


# Task 5
print("--------------- Task 5 ----------------")

def isPrime(*, number):
    dividableCounts = 0
    for i in range(number):
        if number % (i+1) == 0:
            dividableCounts+=1
            if dividableCounts > 2:
                return False

    if dividableCounts > 2:
        return False

    return True


print(isPrime(number=9))
print(isPrime(number=7))
print(isPrime(number=11))
print(isPrime(number=6))
print(isPrime(number=157))

