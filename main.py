# ex. 1
def transform_to_row(infile, outfile):
    with open(infile, "r") as cities:
        content = cities.readline()
        rows = content.rsplit(",")

    with open(outfile, 'w') as citiesrow:
        for line in rows:
            citiesrow.write(line)
            citiesrow.write("\n")

print(transform_to_row("cities.txt", "citiesrow.txt"))

# ex. 2
def add_greeting(infile, outfile):
    with open(infile, "r") as cities:
        content = cities.readlines()

    with open(outfile, "w") as hellocities:
        for line in content:
            hellocities.write("Hello ")
            hellocities.write(line)

print(add_greeting("citiesrow.txt", "hellocities.txt"))

# ex. 3
def strip_greeting(infile, outfile):
    with open(infile, "r") as hellocities:
        content = hellocities.readlines()

    with open(outfile, "w") as nogreeting:
        for line in content:
            stripped = line.strip("Hello ")
            nogreeting.write(stripped)

print(strip_greeting("hellocities.txt", "nogreeting.txt"))

# ex. 4
def combine_files(file1, file2, outfile):
    with open(file1, "r") as capitals:
        line_count1 = 0
        for line in capitals:
            if line != "\n":
                line_count1 += 1
    with open(file2, "r") as countries:
        line_count2 = 0
        for line in countries:
            if line != "\n":
                line_count2 += 1

    if line_count1 == line_count2:
        with open(file1, "r") as capitals:

            with open(file2, "r") as countries:

                with open(outfile, "w") as combinedfiles:
                    caplines = capitals.readlines()
                    countlines = countries.readlines()
                    combine = list(zip(caplines,countlines))
                    for i in range(len(caplines)):
                        line = caplines[i].strip() + " " + countlines[i]
                        combinedfiles.write(line)
    else:
        print("Sorry, the files have to have the same amount of lines")

print(combine_files("capitals.txt", "countries.txt", "combinedfiles.txt"))