### Definitions:
* **Data** is information that is stored or processed by a computer. 
* **Data Type** is an attribute of data that describes the values it can have and how the data can be used.
* **Data Structures** are containers that allow us to combine several pieces of data into a single structure. They help us connect and group our data and give us organization, storage and access the data in an efficient manner.
* **Pointers** are addresses that point to where the structure is or sometimes part of the structure.

### Storage
With primitive types we know how much space they require, so they each bit is stored consecutively one after the other.

With data stuctures we do not know the exact amount of storage it will need and it may change how much storage it needs at different times. If data stored consecutively in data structures we run the risk of overwriting precious data. That is why these are often referred as referenced types. Reference types reference their specific value fron an addess of where the item is stored rather than direct access to the data itself. 

### Data Types - primitive, basic, value: 
* Numbers:
    * Whole numbers
        * short (16 bits; from -32,768 to 32,767)
        * int (32 bits; from ~-2 billion to ~2 billion)
        * long (64 bits; from -(2^63) to 2^63)
    * Decimal numbers: 
        * float (32 bits; ~7 decimal digits)
        * double (64 bits: ~16 decimal digits)
    * Signed 
        * contains positive and negative values
        * 16-bit short range: -32,768 to 32,767
    * Unsigned
        * contains only positive values and it doubles the range
        *16-bit short range: 0 to 65,535

* Boolean 
    * bool
        * True (1 bit; 1)
        * False (1 bit; 0)

* Characters 
    * char
        * A single character

### Data Structures
A collection with a defined way of accessing and storing data.

Size of a data structure depends on how much the programmer allocates, unlike the defined storage of the primitive types no matter the value is. 

* String
    * A sequence of characters that is surrounded by matching single, double or tripple quotation marks. 

* Array
    * A collection of elements, where each item is identified by an index or key.
