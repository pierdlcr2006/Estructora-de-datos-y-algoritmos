**Lab4: Stacks**  
**Capacidades**

* Definir las reglas básicas para la implementación de pilas.  
* Elaborar y Diseñar pilas con listas estáticas, dinámicas y enlazadas.

**Seguridad**

* Generar un ambiente seguro.  
* Evitar el consumo de alimentos.  
* Dejar el ambiente ordenado y limpio.

**Preparación**

* El alumno debe revisar previamente el material cargado.

**Recursos**

* Computadora.

**Instrucciones**  
Cada integrante del grupo debe seleccionar un ejercicio diferente y desarrollarlo con la siguiente estructura:

* Nombre del alumno  
* Ejercicio a desarrollar  
* Prompt engineering (Si aplica)  
  * Prompt ingresado y/o captura  
  * Análisis del prompt  
  * Ajustes del prompt y/o captura  
  * Comentarios de los compañeros  
* Código (Si aplica)  
  * Código desarrollado  
  * Análisis del código  
  * Captura de la ejecución del código  
  * Comentarios de los compañeros  
* Ejercicios (Si aplica)  
  * Explicar cómo funciona el algoritmo  
  * Hacer su diagrama de cómo se ejecuta.  
  * Comentarios del problema  
  * Hacer 3 casos de prueba

Desarrollar todo el código en inglés

# **Stack Data Structure Laboratory Guide**

## **Table of Contents**

* [Stack Data Structure Laboratory Guide](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#stack-data-structure-laboratory-guide)  
  * [Table of Contents](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#table-of-contents)  
  * [1\. Understanding the Concept](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#1-understanding-the-concept)  
  * [2\. Stack Implementations](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#2-stack-implementations)  
    * [2.1 Fixed Array Implementation](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#21-fixed-array-implementation)  
    * [2.2 Dynamic Array Implementation](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#22-dynamic-array-implementation)  
    * [2.3 Linked List Implementation](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#23-linked-list-implementation)  
  * [3\. Practical Applications](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#3-practical-applications)  
    * [3.1 Balanced Parentheses Checking](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#31-balanced-parentheses-checking)  
    * [3.2 Postfix Expression Evaluation](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#32-postfix-expression-evaluation)  
  * [4\. Real-world Case: Browser History](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#4-real-world-case-browser-history)  
  * [Practical Exercises](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#practical-exercises)  
    * [Exercise 1: Reverse a String](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#exercise-1-reverse-a-string)  
    * [Exercise 2: Evaluate Infix Expressions](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#exercise-2-evaluate-infix-expressions)  
    * [Exercise 3: Implement a Stack with getMin() Function](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#exercise-3-implement-a-stack-with-getmin-function)  
    * [Exercise 4: Implement a History Feature](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#exercise-4-implement-a-history-feature)  
    * [Exercise 5: Check for Balanced HTML Tags](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#exercise-5-check-for-balanced-html-tags)  
  * [Submission Requirements](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#submission-requirements)  
  * [6\. Deepening the Concept](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#6-deepening-the-concept)  
    * [Implementation Comparison](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#implementation-comparison)  
    * [Key Applications in Software Systems](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#key-applications-in-software-systems)  
  * [7\. Next Steps](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#7-next-steps)  
    * [Advanced Stack Implementations](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#advanced-stack-implementations)  
    * [Integration with Other Data Structures](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#integration-with-other-data-structures)  
    * [Algorithm Challenges](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#algorithm-challenges)  
  * [8\. Conclusions](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#8-conclusions)  
    * [Key Concepts](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#key-concepts)  
    * [Practical Applications](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#practical-applications)  
    * [Efficiency Considerations](https://file+.vscode-resource.vscode-cdn.net/d%3A/develop/tecsup/o3/algorithms/laboratories/lab04/GUIDE.md#efficiency-considerations)

## **1\. Understanding the Concept**

A stack is a data structure that follows the LIFO (Last-In, First-Out) principle, similar to a stack of books where you can only:

* Add an item to the top of the stack ("push" operation)  
* Remove an item from the top of the stack ("pop" operation)  
* View the top item without removing it ("peek" or "top" operation)

**Basic Operations**:

* **Push**: Add an element to the top  
* **Pop**: Remove and return the element from the top  
* **Peek/Top**: View the top element without removing it  
* **isEmpty**: Check if the stack is empty  
* **Size**: Get the number of elements in the stack

**Expected Time Complexity**:

* Push: O(1)  
* Pop: O(1)  
* Peek: O(1)  
* isEmpty: O(1)  
* Size: O(1)

## **2\. Stack Implementations**

In this section, we'll explore three different ways to implement a stack: using a fixed-size array, a dynamic array, and a linked list. Each implementation has its own advantages and trade-offs.

### **2.1 Fixed Array Implementation**

class ArrayStack:

    """Stack implementation using a fixed-size array."""

    

    def \_\_init\_\_(self, capacity=10):

        """Initialize empty stack with fixed capacity."""

        self.data \= \[None\] \* capacity

        self.capacity \= capacity

        self.top \= \-1  *\# Index of top element, \-1 means empty stack*

    

    def is\_empty(self):

        """Check if stack is empty."""

        return self.top \== \-1

    

    def is\_full(self):

        """Check if stack is full."""

        return self.top \== self.capacity \- 1

    

    def push(self, item):

        """Add item to the top of the stack."""

        if self.is\_full():

            raise OverflowError("Stack overflow \- stack is full")

        

        self.top \+= 1

        self.data\[self.top\] \= item

        return True

    

    def pop(self):

        """Remove and return the top item from the stack."""

        if self.is\_empty():

            raise IndexError("Stack underflow \- stack is empty")

        

        item \= self.data\[self.top\]

        self.data\[self.top\] \= None  *\# Remove reference to the object*

        self.top \-= 1

        return item

    

    def peek(self):

        """Return the top item without removing it."""

        if self.is\_empty():

            raise IndexError("Stack underflow \- stack is empty")

        

        return self.data\[self.top\]

    

    def size(self):

        """Return the number of items in the stack."""

        return self.top \+ 1

    

    def \_\_str\_\_(self):

        """Return a string representation of the stack."""

        if self.is\_empty():

            return "Stack: \[\]"

        

        items \= \[str(self.data\[i\]) for i in range(self.top \+ 1)\]

        return f"Stack: \[{', '.join(items)}\]"

def test\_array\_stack():

    """Test fixed array stack implementation with basic operations."""

    *\# Test basic operations*

    print("Test: Basic operations with fixed array stack")

    stack \= ArrayStack(5)

    

    print(f"Empty stack: {stack}")

    print(f"Is empty? {stack.is\_empty()}")

    

    *\# Push operations*

    for i in range(1, 4):

        stack.push(i \* 10)

        print(f"After push({i\*10}): {stack}")

    

    *\# Test peek*

    print(f"Peek: {stack.peek()}")

    

    *\# Test pop*

    print(f"Pop: {stack.pop()}")

    print(f"After pop: {stack}")

    

    *\# Test full stack*

    stack.push(40)

    stack.push(50)

    print(f"Full stack: {stack}")

    

    try:

        stack.push(60)  *\# Should raise OverflowError*

        print("Push succeeded unexpectedly")

    except OverflowError as e:

        print(f"Error as expected: {e}")

    

    *\# Empty the stack*

    while not stack.is\_empty():

        print(f"Pop: {stack.pop()}")

    

    print(f"Final stack: {stack}")

    print("All array stack tests passed\!")

*\# Example usage*

if \_\_name\_\_ \== "\_\_main\_\_":

    test\_array\_stack()

### **2.2 Dynamic Array Implementation**

class DynamicArrayStack:

    """Stack implementation using a dynamic array that resizes when full."""

    

    def \_\_init\_\_(self, initial\_capacity=10):

        """Initialize empty stack with dynamic capacity."""

        self.data \= \[None\] \* initial\_capacity

        self.capacity \= initial\_capacity

        self.top \= \-1

    

    def is\_empty(self):

        """Check if stack is empty."""

        return self.top \== \-1

    

    def resize(self, new\_capacity):

        """Resize the stack to a new capacity."""

        new\_data \= \[None\] \* new\_capacity

        

        *\# Copy existing elements to the new array*

        for i in range(self.top \+ 1):

            new\_data\[i\] \= self.data\[i\]

            

        self.data \= new\_data

        self.capacity \= new\_capacity

    

    def push(self, item):

        """Add item to the top of the stack."""

        if self.top \== self.capacity \- 1:

            *\# Double the capacity when full*

            self.resize(2 \* self.capacity)

        

        self.top \+= 1

        self.data\[self.top\] \= item

        return True

    

    def pop(self):

        """Remove and return the top item from the stack."""

        if self.is\_empty():

            raise IndexError("Stack underflow \- stack is empty")

        

        item \= self.data\[self.top\]

        self.data\[self.top\] \= None  *\# Remove reference to the object*

        self.top \-= 1

        

        *\# Shrink the array if it's only 1/4 full*

        if 0 \< self.top \+ 1 \<= self.capacity // 4 and self.capacity \> 10:

            self.resize(self.capacity // 2)

            

        return item

    

    def peek(self):

        """Return the top item without removing it."""

        if self.is\_empty():

            raise IndexError("Stack underflow \- stack is empty")

        

        return self.data\[self.top\]

    

    def size(self):

        """Return the number of items in the stack."""

        return self.top \+ 1

    

    def \_\_str\_\_(self):

        """Return a string representation of the stack."""

        if self.is\_empty():

            return "Stack: \[\]"

        

        items \= \[str(self.data\[i\]) for i in range(self.top \+ 1)\]

        return f"Stack: \[{', '.join(items)}\]"

def test\_dynamic\_array\_stack():

    """Test dynamic array stack with auto-resizing capability."""

    print("Test: Dynamic array stack with auto-resizing")

    stack \= DynamicArrayStack(3)  *\# Start with small capacity*

    

    print(f"Initial capacity: {stack.capacity}")

    

    *\# Push beyond initial capacity*

    for i in range(1, 8):

        stack.push(i)

        print(f"After push({i}): size={stack.size()}, capacity={stack.capacity}")

    

    *\# Pop to trigger shrinking*

    for \_ in range(6):

        val \= stack.pop()

        print(f"After pop \-\> {val}: size={stack.size()}, capacity={stack.capacity}")

    

    print("All dynamic array stack tests passed\!")

*\# Example usage*

if \_\_name\_\_ \== "\_\_main\_\_":

    test\_dynamic\_array\_stack()

### **2.3 Linked List Implementation**

class Node:

    """Node class for the Linked List Stack."""

    

    def \_\_init\_\_(self, data=None):

        """Initialize node with data and next reference."""

        self.data \= data

        self.next \= None

class LinkedListStack:

    """Stack implementation using a linked list."""

    

    def \_\_init\_\_(self):

        """Initialize empty stack using linked list."""

        self.head \= None  *\# Top of the stack*

        self.count \= 0  *\# Number of elements*

    

    def is\_empty(self):

        """Check if stack is empty."""

        return self.head is None

    

    def push(self, item):

        """Add item to the top of the stack."""

        new\_node \= Node(item)

        new\_node.next \= self.head

        self.head \= new\_node

        self.count \+= 1

        return True

    

    def pop(self):

        """Remove and return the top item from the stack."""

        if self.is\_empty():

            raise IndexError("Stack underflow \- stack is empty")

        

        item \= self.head.data

        self.head \= self.head.next

        self.count \-= 1

        return item

    

    def peek(self):

        """Return the top item without removing it."""

        if self.is\_empty():

            raise IndexError("Stack underflow \- stack is empty")

        

        return self.head.data

    

    def size(self):

        """Return the number of items in the stack."""

        return self.count

    

    def \_\_str\_\_(self):

        """Return a string representation of the stack."""

        if self.is\_empty():

            return "Stack: \[\]"

        

        items \= \[\]

        current \= self.head

        while current:

            items.append(str(current.data))

            current \= current.next

            

        return f"Stack: \[{', '.join(items)}\]"

def test\_linked\_list\_stack():

    """Test linked list stack implementation with push and pop operations."""

    print("Test: Linked list stack implementation")

    stack \= LinkedListStack()

    

    print(f"Empty stack: {stack}")

    

    *\# Push operations*

    for i in range(1, 6):

        stack.push(i \* 10)

        print(f"After push({i\*10}): {stack}")

    

    print(f"Stack size: {stack.size()}")

    print(f"Top element: {stack.peek()}")

    

    *\# Pop operations*

    while not stack.is\_empty():

        print(f"Pop: {stack.pop()}, Remaining: {stack}")

    

    *\# Test edge cases*

    try:

        empty\_peek \= stack.peek()

        print("Peek should have raised an exception\!")

    except IndexError as e:

        print(f"Error as expected: {e}")

    

    print("All linked list stack tests passed\!")

*\# Example usage*

if \_\_name\_\_ \== "\_\_main\_\_":

    test\_linked\_list\_stack()

## **3\. Practical Applications**

Stacks are used in many areas of computer science and software engineering. The following applications demonstrate how stacks solve common programming problems.

### **3.1 Balanced Parentheses Checking**

A classic application of stacks is checking if parentheses, brackets, and braces are balanced in an expression.

def is\_balanced(expression):

    """Check if an expression has balanced parentheses, brackets, and braces."""

    stack \= \[\]

    opening \= "({\["

    closing \= ")}\]"

    

    *\# Dictionary to match opening and closing brackets*

    brackets\_map \= {

        ')': '(',

        '}': '{',

        '\]': '\['

    }

    

    for char in expression:

        if char in opening:

            stack.append(char)

        elif char in closing:

            if not stack:  *\# Stack is empty but we found a closing bracket*

                return False

            

            top \= stack.pop()

            if top \!= brackets\_map\[char\]:

                return False

    

    *\# If stack is empty, all brackets were matched*

    return len(stack) \== 0

def test\_balanced\_parentheses():

    """Test parentheses balancing with various expressions."""

    test\_cases \= \[

        ("()", True),

        ("()\[\]{}", True),

        ("(\[\])", True),

        ("(\[)\]", False),

        ("{\[\]}", True),

        (")(", False),

        ("((((", False),

        ("))))", False),

        ("a\*(b+c)-(d/e)", True)

    \]

    

    print("Testing parentheses balancing:")

    for expr, expected in test\_cases:

        result \= is\_balanced(expr)

        print(f"Expression: '{expr}', Balanced: {result}, Expected: {expected}")

        assert result \== expected, f"Test failed for '{expr}'"

    

    print("All balanced parentheses tests passed\!")

*\# Example usage*

if \_\_name\_\_ \== "\_\_main\_\_":

    test\_balanced\_parentheses()

### **3.2 Postfix Expression Evaluation**

Stacks are fundamental for evaluating expressions in postfix notation (Reverse Polish Notation).

def evaluate\_postfix(expression):

    """Evaluate a postfix expression in Reverse Polish Notation."""

    stack \= \[\]

    operators \= {

        '+': lambda a, b: a \+ b,

        '-': lambda a, b: a \- b,

        '\*': lambda a, b: a \* b,

        '/': lambda a, b: a / b,

        '^': lambda a, b: a \*\* b

    }

    

    tokens \= expression.split()

    

    for token in tokens:

        if token in operators:

            *\# It's an operator, pop two operands and apply*

            if len(stack) \< 2:

                raise ValueError("Invalid postfix expression: not enough operands")

            

            b \= stack.pop()  *\# Second operand*

            a \= stack.pop()  *\# First operand*

            

            *\# Apply the operator*

            result \= operators\[token\](a, b)

            stack.append(result)

        else:

            *\# It's an operand, convert to number and push*

            try:

                stack.append(float(token))

            except ValueError:

                raise ValueError(f"Invalid token in expression: {token}")

    

    *\# If we have exactly one value in the stack, it's the result*

    if len(stack) \== 1:

        return stack\[0\]

    else:

        raise ValueError("Invalid postfix expression: too many operands")

def test\_postfix\_evaluation():

    """Test postfix expression evaluation with different operations."""

    test\_cases \= \[

        ("3 4 \+", 7),             *\# 3 \+ 4 \= 7*

        ("5 2 \-", 3),             *\# 5 \- 2 \= 3*

        ("3 4 \* 2 \+", 14),        *\# 3 \* 4 \+ 2 \= 14*

        ("7 2 / 3 \*", 10.5),      *\# 7 / 2 \* 3 \= 10.5*

        ("5 1 2 \+ 4 \* \+ 3 \-", 14) *\# 5 \+ ((1 \+ 2\) \* 4\) \- 3 \= 14*

    \]

    

    print("Testing postfix expression evaluation:")

    for expr, expected in test\_cases:

        try:

            result \= evaluate\_postfix(expr)

            print(f"Expression: '{expr}', Result: {result}, Expected: {expected}")

            assert abs(result \- expected) \< 1e-10, f"Test failed for '{expr}'"

        except Exception as e:

            print(f"Expression: '{expr}', Error: {str(e)}")

    

    print("All postfix evaluation tests passed\!")

*\# Example usage*

if \_\_name\_\_ \== "\_\_main\_\_":

    test\_postfix\_evaluation()

## **4\. Real-world Case: Browser History**

Web browsers use stacks to implement the "Back" and "Forward" navigation features. This example demonstrates how stacks are used in software you interact with daily.

Let's implement a web browser history using stacks, similar to the "Back" and "Forward" buttons in a browser.

class BrowserHistory:

    """Simple browser history implementation using stacks."""

    

    def \_\_init\_\_(self):

        """Initialize browser history with back and forward stacks."""

        self.back\_stack \= \[\]  *\# Stack for back navigation*

        self.forward\_stack \= \[\]  *\# Stack for forward navigation*

        self.current\_page \= None

    

    def visit(self, url):

        """Visit a new page, adding current to back stack and clearing forward stack."""

        if self.current\_page:

            self.back\_stack.append(self.current\_page)

        

        self.current\_page \= url

        self.forward\_stack \= \[\]  *\# Clear forward history*

        

        return f"Visited: {url}"

    

    def back(self):

        """Navigate back in history."""

        if not self.back\_stack:

            return "No back history"

        

        *\# Move current page to forward stack*

        self.forward\_stack.append(self.current\_page)

        *\# Set current page to the last back page*

        self.current\_page \= self.back\_stack.pop()

        

        return f"Navigated back to: {self.current\_page}"

    

    def forward(self):

        """Navigate forward in history."""

        if not self.forward\_stack:

            return "No forward history"

        

        *\# Move current page to back stack*

        self.back\_stack.append(self.current\_page)

        *\# Set current page to the last forward page*

        self.current\_page \= self.forward\_stack.pop()

        

        return f"Navigated forward to: {self.current\_page}"

    

    def get\_current(self):

        """Get the current page."""

        if not self.current\_page:

            return "No current page"

        

        return f"Current page: {self.current\_page}"

def test\_browser\_history():

    """Test browser navigation with back and forward operations."""

    print("Testing browser navigation:")

    browser \= BrowserHistory()

    

    print(browser.get\_current())

    

    *\# Visit some pages*

    print(browser.visit("https://www.example.com"))

    print(browser.visit("https://www.example.com/page1"))

    print(browser.visit("https://www.example.com/page2"))

    

    *\# Test navigation*

    print(browser.get\_current())

    print(browser.back())

    print(browser.back())

    print(browser.forward())

    

    *\# Visit a new page (should clear forward history)*

    print(browser.visit("https://www.example.com/page3"))

    print(browser.get\_current())

    

    *\# Try to go forward (should have no forward history)*

    print(browser.forward())

    

    *\# Test edge cases*

    print(browser.back())

    print(browser.back())

    print(browser.back())  *\# Should show no back history*

    

    print("All browser history tests completed successfully\!")

*\# Example usage*

if \_\_name\_\_ \== "\_\_main\_\_":

    test\_browser\_history()

## **Practical Exercises**

The following exercises will help you practice the stack implementation concepts you've learned. For each exercise, implement the solution following the approach described.

### **Exercise 1: Reverse a String**

Use a stack to reverse a string. Push each character onto a stack, then pop them to get the reversed string.

### **Exercise 2: Evaluate Infix Expressions**

Extend the expression evaluation code to handle infix expressions like (3 \+ 4\) \* 2. Hint: Convert infix to postfix first, then evaluate.

### **Exercise 3: Implement a Stack with getMin() Function**

Implement a stack that supports the following operations in O(1) time:

* push(x) \- Push element x onto stack  
* pop() \- Remove the element on top of the stack  
* top() \- Get the top element  
* getMin() \- Retrieve the minimum element in the stack

### **Exercise 4: Implement a History Feature**

Build a text editor feature that supports typing, deleting, and undo operations using stacks.

### **Exercise 5: Check for Balanced HTML Tags**

Extend the balanced parentheses checker to validate HTML tags, ensuring that each opening tag has a corresponding closing tag in the correct order.

## **Submission Requirements**

For each implementation, include:

1. Clear documentation of your approach  
2. Complete code with proper error handling  
3. Test cases demonstrating functionality  
4. Time and space complexity analysis

## **6\. Deepening the Concept**

Understanding the strengths and weaknesses of different stack implementations helps you choose the right one for specific scenarios.

### **Implementation Comparison**

| Implementation | Advantages | Disadvantages | Best Use Cases |
| :---- | :---- | :---- | :---- |
| Fixed Array | • Simple implementation • Excellent memory locality • Predictable memory usage | • Size limit • Overflow risk • Wasted space for partial fills | • When maximum size is known • Performance-critical applications • Embedded systems |
| Dynamic Array | • Flexible size • Good memory locality • No overflow risk | • Occasional costly resizing • Potential memory over-allocation | • General-purpose usage • When stack size varies significantly • Most software applications |
| Linked List | • Unlimited size • Consistent insertion time • Memory efficient for sparse usage | • Extra memory per node • Poor cache locality • No random access | • Memory-constrained systems • Frequent large data variations • When implementing other data structures |

### **Key Applications in Software Systems**

Stacks play crucial roles in computing:

1. **Program Execution**: The call stack tracks function calls, local variables, and return addresses in almost all programming languages.  
2. **Memory Management**: Operating systems use stacks for program execution context and memory allocation.  
3. **Browser History**: Web browsers implement back/forward navigation with stack structures.  
4. **Undo/Redo**: Text editors and design software use stacks to track operation history.  
5. **Syntax Parsing**: Compilers and interpreters use stacks for expression evaluation and syntax checking.

## **7\. Next Steps**

After mastering the basics of stacks, consider these advancement paths to deepen your expertise:

### **Advanced Stack Implementations**

1. **Thread-safe Stack**: Implement a concurrent stack that safely handles multiple threads accessing it simultaneously.  
2. **Bounded Stack**: Create a stack with a maximum size that uses a circular buffer to optimize memory usage.  
3. **Persistent Stack**: Design a stack that preserves previous versions after modifications.

### **Integration with Other Data Structures**

1. **Stack-based Graph Traversal**: Implement depth-first search using stacks instead of recursion.  
2. **Expression Tree Builder**: Create a system that builds expression trees from infix notation using stacks.  
3. **Custom Memory Allocator**: Implement a stack-based memory allocator for temporary objects.

### **Algorithm Challenges**

1. **Next Greater Element**: For each element in an array, find the first greater element that appears to its right.  
2. **Largest Rectangle in Histogram**: Use a stack to find the largest rectangular area in a histogram.  
3. **Stock Span Problem**: Calculate the span of stock's price for all days.

These next steps will solidify your understanding of stacks and prepare you for more complex data structure applications.

## **8\. Conclusions**

Stacks represent one of the most fundamental and versatile data structures in computer science. Through this laboratory, you've learned:

### **Key Concepts**

* **LIFO Principle**: The Last-In-First-Out nature of stacks determines how data flows through the structure.  
* **Core Operations**: All stack implementations provide push, pop, peek, isEmpty, and size operations.  
* **Implementation Trade-offs**: Different implementations (array-based, dynamic, linked list) have unique performance characteristics.

### **Practical Applications**

The stack's simple interface belies its incredible utility in solving complex problems:

* Balancing symbols in expressions  
* Evaluating arithmetic expressions  
* Implementing navigation history  
* Supporting function calls in programming languages  
* Enabling backtracking in algorithms

### **Efficiency Considerations**

* **Time Complexity**: Well-implemented stacks provide O(1) operations for all basic functions.  
* **Space Efficiency**: The choice of implementation affects memory usage and performance.  
* **Context Importance**: The right stack implementation depends on your specific requirements.

As you continue your journey in data structures and algorithms, you'll find stacks appearing as building blocks in more complex structures and algorithms. This foundational knowledge will serve you throughout your programming career.

**Reto**  
Proponer un algoritmo que resuelva un problema del 1 al 8 de la siguiente web [https://adventjs.dev/](https://adventjs.dev/) e iterar hasta tener 5 estrellas. (Entrar con tus datos)

**Desarrollo**

**Incrementos**

* **Repositorio (0-5)**  
* **Código fuente (0-5)**  
* **Informe (-10-0)**  
* **Expo (0-10)**

**Conclusiones**

1. 