def print_melon_tallies(filename, melon_tallies):
    f = open(filename)
    for line in f:
        data = line.split(",")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count
    f.close()
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        
        statement = "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
        actual_print(statement, False)
    
def print_sales(filename):
    f = open(filename)
    sales = [0, 0]
    for line in f:
        data = line.split(",")
        #Changed line below from 'if data[1] == 0' to: 
        if data[2] == "Online":
            sales[0] += float(data[3])
        else:
            sales[1] += float(data[3])

    print "******************************************"
    print "Salespeople generated %0.2f in revenue." % sales[1]
    print "Internet sales generated %0.2f in revenue." % sales[0]
    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"
    print "******************************************"

def actual_print(statement, upper):
    if upper == True:
        print statement.upper()
    else:
        print statement    

def main():
    print "******************************************"
    melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}
    print_melon_tallies("orders_by_type.csv", melon_tallies)

    print_sales("orders_with_sales.csv")
    
if __name__ == "__main__":
    main()