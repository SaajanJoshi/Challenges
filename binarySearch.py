class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

root = Node(8)
root.left = Node(4)
root.right = Node(2)

root.left.left = Node(2)
root.left.right = Node(6)

root.left.left.left = Node(5)
root.left.left.right = Node(7)

root.left.right.left = Node(3)
root.left.right.right = Node(0)

root.right.left = Node(10)
root.right.right = Node(14)

root.right.left.left = Node(5)
root.right.left.right = Node(7)

root.right.right.left = Node(8)
root.right.right.right = Node(10)

maxValueTemp = 0
minValueTemp = 0
def getRootValue(initValue, initNextValue, root_node, node, prev_root_node, node_next, k, maxValue, minValue):
  try:
   valueLeft = root_node.left.value
   valueRight = root_node.right.value

   if (initValue > k and initValue < maxValue):
       maxValue = initValue
   if (initValue > minValue and initValue < k):
       minValue = initValue

   if (initNextValue > k and initNextValue < maxValue):
       maxValue = initNextValue
   if (initNextValue > minValue and initNextValue < k):
       minValue = initNextValue

   if (valueLeft > k and valueLeft < maxValue):
       maxValue = valueLeft
   if (valueRight > k and valueRight < maxValue):
       maxValue = valueRight

   if (valueLeft > minValue and valueLeft < k):
       minValue = valueLeft
   if (valueRight > minValue and valueRight < k):
       minValue = valueRight

   maxValueTemp = maxValue
   minValueTemp = minValue
   if node_next == 'L':
    getRootValue(initValue, initNextValue, root_node.left, node, root_node, 'R', k, maxValue, minValue)
   else:
    getRootValue(initValue, initNextValue, prev_root_node.right, node, prev_root_node, 'L', k, maxValue, minValue)
  except:
    return
  else:
      return {
          'max': maxValueTemp,
          'min': minValueTemp
      }



def findCeilingFloor(root_node, k, floor=None, ceil=None):
 initValue = root_node.value
 initLeft = root_node.left.value
 Value = getRootValue(initValue,initLeft,root_node.left, 'L', '', 'L', k , 100000, 0)
 print(Value)
 initRight = root_node.right.value
 Value2 = getRootValue(initValue,initRight,root_node.right, 'R', '', 'L', k, Value['max'], Value['min'])
 print(Value2)
 return Value2

print(findCeilingFloor(root, 6))

