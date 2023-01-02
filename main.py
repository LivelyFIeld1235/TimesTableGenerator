def UI():
    numToGenerate = input("Enter a number or a range (x,y) to generate times table >");
    isValidNUM,isRange = False, False;
    while(isValidNUM == False):
        try:
            if(numToGenerate.count(",") == 1):
                numToGenerate = numToGenerate.replace(" ", "").replace("(","").replace(")","");
                minmax = int(numToGenerate.split(",")[0]),int(numToGenerate.split(",")[1]);
                return [min(minmax),max(minmax)];
            else:
                var = int(numToGenerate);
                if (var > 1 or var == -1):
                    isValidNUM = True;
                else:
                    raise Exception;
        except ValueError:
            if("quit" in numToGenerate.lower()):
                return -1;
            numToGenerate = input("Please enter a valid number>");
        except Exception:
            numToGenerate = input("something went wrong>");
    return int(numToGenerate);

def display(integer):
    for i in range(1,21):
        print(integer, "x", i, "=",integer*i,end = "\n");

def main():
    tableNUM = UI();
    while (tableNUM != -1):
        try:
            if(len(tableNUM) == 2):
                for i in range(tableNUM[0],tableNUM[1]+1):
                    display(i)
                    print("\n")
                tableNUM = UI();
        except TypeError:
                display(tableNUM);
                tableNUM = UI();
    print("goodbye")
if __name__ == "__main__":
    main();