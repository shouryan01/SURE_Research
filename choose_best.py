import csv
import pprint as pp

#first just minimize time and distance
#minimize per category

# G = distance = current[0]
# F = price = price
# H = duration = current[1]

def find_best():
    skip_word = "Origin"    
    smallest = (1000, 1000)
    count = 0
    price_index = 0
    best_output = []
    best_price = []
    output = []
    final = []
    best_small_sedan = 1000
    best_med_sedan = 1000
    best_large_sedan = 1000
    best_small_suv = 1000
    best_med_suv = 1000
    best_minivan = 1000
    best_pickup = 1000
    
    best_small_sedan_values = (1000, 1000)
    best_med_sedan_values = (1000, 1000)
    best_large_sedan_values = (1000, 1000)
    best_small_suv_values = (1000, 1000)
    best_med_suv_values = (1000, 1000)
    best_minivan_values = (1000, 1000)
    best_pickup_values = (1000, 1000)

    prices = []
    with open("prices_data.csv") as prices_file:
        for row in csv.reader(prices_file):
            prices.append(row[0])

    with open("canton_simulation.csv") as input_file: #, open("prices_data.csv") as prices_file
        reader = csv.reader(input_file)
        next(input_file)
        next(input_file)
        for input_line in reader: #, price in zip(input_file, prices_file):
            if "end" in input_line:
                output.append(smallest)
                best_output.append([smallest, best_small_sedan_values, best_med_sedan_values, best_large_sedan_values, best_small_suv_values, best_med_sedan_values, best_minivan_values, best_pickup_values])
                best_price.append([best_small_sedan, best_med_sedan, best_large_sedan, best_small_suv, best_med_suv, best_minivan, best_pickup])

                # print(smallest)
                break
            elif skip_word not in input_line:
                current = tuple(input_line)
                current = (float(current[0]), float(current[1]))
                small_sedan = 0.75*13.038*(float(prices[price_index])-0.03) + 0.0715*current[0] + 0.0839*current[0] + (0.005*current[1]**2)
                med_sedan = 0.75*15.56*(float(prices[price_index])-0.03) + 0.0831*current[0] + 0.0956*current[0] + (0.005*current[1]**2)
                large_sedan = 0.75*17.06*(float(prices[price_index])-0.03) + 0.1143*current[0] + 0.0969*current[0] + (0.005*current[1]**2)
                small_suv = 0.75*14.64*(float(prices[price_index])-0.03) + 0.0827*current[0] + 0.0948*current[0] + (0.005*current[1]**2)
                med_suv = 0.75*19.18*(float(prices[price_index])-0.03) + 0.1125*current[0] + 0.1011*current[0] + (0.005*current[1]**2)
                minivan = 0.75*19.92*(float(prices[price_index])-0.03) + 0.1122*current[0] + 0.0942*current[0] + (0.005*current[1]**2)
                pickup = 0.75*25.68*(float(prices[price_index])-0.03) + 0.1523*current[0] + 0.088*current[0] + (0.005*current[1]**2)
                
                if smallest > current:
                    smallest = current

                if best_small_sedan > small_sedan:
                    best_small_sedan, best_small_sedan_values = small_sedan, current
                if best_med_sedan > med_sedan:
                    best_med_sedan, best_med_sedan_values = med_sedan, current
                if best_large_sedan > large_sedan:
                    best_large_sedan, best_large_sedan_values = large_sedan, current
                if best_small_suv > small_suv:
                    best_small_suv, best_small_suv_values = small_suv, current
                if best_med_suv > med_suv:
                    best_med_suv, best_med_suv_values = med_suv, current
                if best_minivan > minivan:
                    best_minivan, best_minivan_values = minivan, current
                if best_pickup > pickup:
                    best_pickup, best_pickup_values = pickup, current

                price_index += 1
            else:
                count += 1
                price_index = 0
                output.append(smallest)
                best_output.append([smallest, best_small_sedan_values, best_med_sedan_values, best_large_sedan_values, best_small_suv_values, best_med_sedan_values, best_minivan_values, best_pickup_values])
                best_price.append([best_small_sedan, best_med_sedan, best_large_sedan, best_small_suv, best_med_suv, best_minivan, best_pickup])
                # print(smallest)
                smallest = (1000, 1000)

                best_small_sedan = 1000
                best_med_sedan = 1000
                best_large_sedan = 1000
                best_small_suv = 1000
                best_med_suv = 1000
                best_minivan = 1000
                best_pickup = 1000

                best_small_sedan_values = (1000, 1000)
                best_med_sedan_values = (1000, 1000)
                best_large_sedan_values = (1000, 1000)
                best_small_suv_values = (1000, 1000)
                best_med_suv_values = (1000, 1000)
                best_minivan_values = (1000, 1000)
                best_pickup_values = (1000, 1000)
                
                next(input_file)

        # print(best_small_sedan)
        # print(best_med_sedan)
        # print(best_large_sedan)
        # print(best_small_suv)
        # print(best_med_suv)
        # print(best_minivan)
        # print(best_pickup)

        # print(best_small_sedan_values)
        # print(best_med_sedan_values)
        # print(best_large_sedan_values)
        # print(best_small_suv_values)
        # print(best_med_suv_values)
        # print(best_minivan_values)
        # print(best_pickup_values)

        # pp.pprint(best_output)
        results = list(map(list, zip(*best_output)))
        for result in results:
            final.append([sum(i) / len(result) for i in zip(*result)])

        best_price_results = [sum(col) / float(len(col)) for col in zip(*best_price)]

    return best_price_results

# results = find_best()
# results = list(map(list, zip(*results)))

# pp.pprint(results)

# final = []

# for result in results:
#     final.append([sum(i) / len(result) for i in zip(*result)])

# pp.pprint(final)
print(find_best())