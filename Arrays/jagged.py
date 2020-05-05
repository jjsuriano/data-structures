# JAGGED ARRAYS

# Playing arround with Python to create a jagged array class

class JaggedArray():
    def __init__(self, rows=1):
        if isinstance(rows, int) and rows > 0:
            self.rows = rows
            self.jArray = []
            for i in range(self.rows):
                self.jArray.append([])

    def append(self, value, row:int):
        if not isinstance(row, int): 
            print('IndexError: row index {} is invalid'.format(row))
            return self.jArray

        if row not in range(self.rows):
            print('IndexError: row index {} is out of bounds'.format(row))
            return self.jArray
        
        size = len(self.jArray[row])
        new_row = [ None for i in range(size+1)]
        for i in range(size+1):
            if i == size:
                new_row[i] = value
            else: 
                new_row[i] = self.jArray[row][i]
        self.jArray[row] = new_row

        return self.jArray
            

    def deleteAt(self, row, col):
        if not isinstance(row, int): 
            print('IndexError: row index {} is invalid'.format(row))
            return self.jArray

        if row not in range(self.rows):
            print('IndexError: row index {} is out of bounds'.format(row))
            return self.jArray
        
        if not isinstance(col, int): 
            print('IndexError: column index {} is invalid'.format(col))
            return self.jArray

        if col not in range(len(self.jArray[row])):
            print('IndexError: column index {} is out of bounds'.format(col))
            return self.jArray
        
        size = len(self.jArray[row])
        new_row = [self.jArray[row][i] for i in range(size) if i != col]
        self.jArray[row] = new_row
        return self.jArray


    def deleteLastOf(self, row):
        if not isinstance(row, int): 
            print('IndexError: row index {} is invalid'.format(row))
            return self.jArray

        if row not in range(self.rows):
            print('IndexError: row index {} is out of bounds'.format(row))
            return self.jArray

        size = len(self.jArray[row])
        new_row = [self.jArray[row][i] for i in range(size-1)]
        self.jArray[row] = new_row
        return self.jArray
    
    def elementAt(self, row, col):
        if not isinstance(row, int): 
            print('IndexError: row index {} is invalid'.format(row))
            return self.jArray

        if row not in range(self.rows):
            print('IndexError: row index {} is out of bounds'.format(row))
            return self.jArray
        
        if not isinstance(col, int): 
            print('IndexError: column index {} is invalid'.format(col))
            return self.jArray

        if col not in range(len(self.jArray[row])):
            print('IndexError: column index {} is out of bounds'.format(col))
            return self.jArray
        
        return self.jArray[row][col]


    def lengths(self):
        lengths = []
        for i in range(self.rows):
            lengths.append(len(self.jArray[i]))
            print('Row {} has {} element(s)'.format(i, len(self.jArray[i])))
        return (lengths)

    def print(self):
        print('Rows: {}'.format(self.rows))
        for i in range(self.rows):
            print(self.jArray[i])



j_array = JaggedArray(3)
print()
print('Initializing Jagged Array with 3 rows...')
j_array.lengths()
print()
j_array.print()

print()
print('Appending 5 in row 1...')
j_array.append(5, 1)
print()
j_array.lengths()
print()
j_array.print()

print()
print('Appending 10 in row 3...')
j_array.append(10, 3)
print()
j_array.lengths()
print()
j_array.print()

print()
print('Appending 10 in row 2...')
j_array.append(11, 2)
print()
j_array.lengths()
print()
j_array.print()

print()
print('Appending 10 in row 2:')
j_array.append(10, 1)
print()
j_array.lengths()
print()
j_array.print()

print()
print('Appending 1 in row 0...')
j_array.append(1, 0)
print()
j_array.lengths()
print()
j_array.print()

print()
print('Deleting the last element in row 0...')
j_array.deleteLastOf(0)
print()
j_array.lengths()
print()
j_array.print()

print()
print('Deleting the element at index 0 in row 1...')
j_array.deleteAt(1, 0)
print()
j_array.lengths()
print()
j_array.print()

print()
print('Accessing the first element of row 2...')
print('The first element is: {}'.format(j_array.elementAt(2, 0)))
print()
j_array.lengths()
print()
j_array.print()