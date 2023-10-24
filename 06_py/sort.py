cisla = [4, 1, 6, 7, 3]

def sortNumbers(data:list[float], condition:str)->list:
    sorted = [data[0]]
    for i in range(1, len(data), +1):
        if condition == "ASC":
            if data[i] >= sorted[len(sorted)-1]:
                sorted.append(data[i])
            else:
                for n in range(len(sorted)-1, -1, -1):
                    if n == 0:
                        sorted.insert(0, data[i])
                    elif data[i] >= sorted[n-1]:
                        sorted.insert(n, data[i])
                        break
                    elif data[i] < sorted[n-1]:
                        continue
        elif condition == "DESC":
            if data[i] <= sorted[len(sorted)-1]:
                sorted.append(data[i])
            else:
                for n in range(0, len(sorted), +1):
                    if len(sorted) == 1:
                        sorted.insert(0, data[i])
                        break
                    elif data[i] >= sorted[n]:
                        sorted.insert(n, data[i])
                        break
                    elif data[i] < sorted[n]:
                        continue
    return sorted

reputation = [2, 5, 6]
manufactures = ['Ford', 'BMW', 'Audi']

def sortData(weights:list[float], data:list[str], condition:str):
    while len(weights) == len(data):
        sorted_data = [data[0]]
        sorted_weights = [weights[0]]
        for i in range(1, len(weights), +1):
            if condition == "ASC":
                if weights[i] >= sorted_weights[len(sorted_weights)-1]:
                    sorted_weights.append(weights[i])
                    sorted_data.append(data[i])
                else:
                    for n in range(len(sorted_weights)-1, -1, -1):
                        if n == 0:
                            sorted_weights.insert(0, weights[i])
                            sorted_data.insert(0, data[i])
                        elif weights[i] >= sorted_weights[n-1]:
                            sorted_weights.insert(n, weights[i])
                            sorted_data.insert(n, data[i])
                            break
                        elif weights[i] < sorted_weights[n-1]:
                            continue
            elif condition == "DESC":
                if weights[i] <= sorted_weights[len(sorted_weights)-1]:
                    sorted_weights.append(weights[i])
                    sorted_data.append(data[i])
                else:
                    for n in range(0, len(sorted_weights), +1):
                        if len(sorted_weights) == 1:
                            sorted_weights.insert(0, weights[i])
                            sorted_data.insert(0, data[i])
                            break
                        elif weights[i] > sorted_weights[n]:
                            sorted_weights.insert(n, weights[i])
                            sorted_data.insert(n, data[i])
                            break
                        elif weights[i] <= sorted_weights[n]:
                            continue
        return sorted_data
    else:
        raise ValueError('Invalid input data')