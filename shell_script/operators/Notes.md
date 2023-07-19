# There are five operators in shell
```
- Arithmetic Operators
- Relational Operators
- Boolean Operators
- Bitwise Operators
- File Test Operators

```

## Arithmetic Operators
```
- Arithmetic Operators
Additions
    - `expr $a+$b` = 30
Subtraction
    - `expr $a-$b` = -10
Multiplication
    - `expr $a\*$b` = 200
Division
    - `expr $a/$b` = 2
Modulus
    - `expr $a%$b` = 0
Assignment
    - `a=$b` = 10
Equal
    - `a=$b` = 10
Not Equal
    - `a!=$b` = 1
```
## Relational Operators
```
-eq = is equal to
-ne = is not equal to
-gt = is greater than
-lt = is less than
-ge = is greater than or equal to
-le = is less than or equal to
```
## Boolean Operators
```
a=20
b=10
! = Logical NOT ; [!false] = true
&& = Logical AND; [$a -lt 20 && $b -gt 100] = false
|| = Logical OR; [$a -lt 20 || $b -gt 100] = true
-o = Logical OR; [$a -lt 20 -o $b -gt 100] = true
-a = Logical AND; [$a -lt 20 -a $b -gt 100] = false

left shift (<<) = 00001010 << 2 = 00101000 (40)
what is happening here is that the bits are shifted to the left by two places and the empty spaces are filled with zeros.
right shift (>>) = 00001010 >> 2 = 00000010 (2)
what is happening here is that the bits are shifted to the right by two places and the empty spaces are filled with zeros.


```
## File Test Operators
```
- b file = True if the file exists and is a block special file. [ -b $file ]
- c file = True if the file exists and is a character special file. [ -c $file ]
- d file = True if the file exists and is a directory. [ -d $file ]
- f file = True if the file exists and is a regular file. [ -f $file ]
- g file = True if the file exists and its set-group-id (SGID) bit is set. [ -g $file ]
- k file = True if the file exists and its "sticky" bit is set. [ -k $file ]
- p file = True if the file exists and is a named pipe (FIFO).  [ -p $file ]
- t file = True if the file descriptor is opened on a terminal. [ -t $file ]
- u file = True if the file exists and its set-user-id bit is set. [ -u $file ]
- r file = True if the file exists and is readable. [ -r $file ]
- w file = True if the file exists and is writable. [ -w $file ]
- x file = True if the file exists and is executable. [ -x $file ]
- s file = True if the file exists and its size is greater than zero.   [ -s $file ]
- e file = True if the file exists; provided, however, that -L is not also specified. [ -e $file ]
```
## Makind Decisions statements
```
    5 conditional statements
    - if statement
    - if-else statement
    - if-elif-else statement
    - nested if statement
    - case statement
```

## Tests
```
Tests are virtual files that are used to test the conditions of a file. They are used along with if statements and while loops.
``` 

syntax:
 [ test-condition ]
[ -e /etc/passwd ]
file exists are not, if it exists it will return true else false
[ -f /etc/passwd ]
file exists and it is a regular file
[ -d /etc/passwd ]

if [ -f /etc/passwd ]
then
    echo "file exists"
else
    echo "file does not exist"
fi

if-else statement

if [ -f /etc/passwd ]
then
    echo "file exists"
else
    echo "file does not exist"
fi
 
if-elif-else statement

if [ -f /etc/passwd ]
then
    echo "file exists"
elif [ -d /etc/passwd ]
then
    echo "file is a directory"
else
    echo "file does not exist"
fi

Nested if statement

if [ -f /etc/passwd ]
then
 echo "file exists"
else 
  if [ -w /etc/passwd ]
  then
    echo "have write access"
  fi
fi

if [ -f /etc/passwd ]
then
    echo ""

```