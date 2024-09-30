def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    max_units = 0   
    for numberOfBoxes, unitsPerBox in boxTypes:
        boxes_to_take = min(truckSize, numberOfBoxes)
      
        max_units += boxes_to_take * unitsPerBox
       
        truckSize -= boxes_to_take
      
        if truckSize == 0:
            break

    return max_units
 
boxTypes = [[1, 3], [2, 2], [3, 1]]   
truckSize = 4

result = maximumUnits(boxTypes, truckSize)
print(f"Maximum units that can be loaded on the truck: {result}")
