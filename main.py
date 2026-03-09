from fastapi import FastAPI, status, HTTPException, Query

app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Pupose: Add two numbers together.
        Parameters:
        - a: First number
        - b: Second number
    Expected Result: The mathematical sum of a and b.
    Expected Output: JSON with operation name, inputs, and result.
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers")    
    return {"operation": "add", "num_a": a, "num_b": b, "result": a + b}


@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: str, b: str):
    """
    Pupose: Subtract two numbers together.
        Parameters:
        - a: First number
        - b: Second number
    Expected Result: The difference of a and b.
    Expected Output: JSON with operation name, inputs, and result.
    
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers")    
    return {"operation": "subtract", "num_a": a, "num_b": b, "result": a - b}


@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: str, b: str):
    """
    Purpose:multiply two numbers together.
        Parameters:
        - a: First number
        - b: Second number
    Expected Result: The mathematical product of a and b.
    Expected Output: JSON with operation name, inputs, and result.
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers")    
    return {"operation": "multiply", "num_a": a, "num_b": b, "result": a * b}


@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: str, b: str):
    """
    Purpose: divide two numbers together.
        Parameters:
        - a: First number
        - b: Second number
    - Expected Result: The quotient of a / b.
    - Expected Output: JSON with operation name, inputs, and result.
        - Raises a 422 error if b is zero.
    """
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Division by zero is not allowed. Please provide a non-zero value for b.")
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers") 
    return {"operation": "divide", "a": a, "b": b, "result": a / b}   


@app.get("/area/rectangle")
def calculate_rectangle_area(width: str, height: str):
    """
    Purpose: Calculate the area of rectangle using width and hight.
        - width = first number and width of the rectangle
        - height = second number and height of the rectangle
    - Expected Result: The area as a positive float.
    - Expected Output: JSON with shape details and area.
    
    """
    try:
        # 1. Convert strings to numbers first
        w = float(width)
        h = float(height)
    except ValueError:
        raise HTTPException(
            status_code=422, 
            detail="Both 'width' and 'height' must be valid numbers"
        )

    # positive error handling
    if w < 0 or h < 0:
        raise HTTPException(
            status_code=400, 
            detail="Width and height must be positive numbers."
        )
    
    return {
        "shape": "rectangle",
        "width": w,
        "height": h,
        "area": w * h
    }


@app.get("/convert/temperature")
def convert_temp(value: float, direction: str):
    """
    Converts temperature between Celsius and Fahrenheit.
    - direction: 'c_to_f' (Celsius to Fahrenheit)
    - direction: 'f_to_c' (Fahrenheit to Celsius)

    Returns:
    - JSON object with the result either f_to_c or c_to_f
    """
    direction = direction.lower()

    if direction == "c_to_f":
        # Formula: (C * 9/5) + 32
        converted = (value * 9/5) + 32
        return {"input": f"{value}°C", "result": f"{converted}°F"}

    elif direction == "f_to_c":
        # Formula: (F - 32) * 5/9
        converted = (value - 32) * 5/9
        return {"input": f"{value}°F", "result": f"{converted}°C"}

    else:
        raise HTTPException(
            status_code=400, 
            detail="Invalid direction. Use 'c_to_f' or 'f_to_c'."
        )


@app.get("/average/{a}/{b}/{c}")
def calculate_average(a: str, b: str, c: str):
    """
    Purpose: Calculate the average for 3 numbers.
        Parameters:
        - a: First number
        - b: Second number
        - c: Third number

    - Expected Result: (a + b + c) / 3.
    - Expected Output: JSON with inputs and average.
    """
    try:
        num_a = float(a)
        num_b = float(b)
        num_c = float(c)
        
        total = num_a + num_b + num_c
        average = total / 3
        
        return {
            "operation": "average",
            "numbers": [num_a, num_b, num_c],
            "average": average
        }

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail="All parameters (a, b, and c) must be valid numbers."
            )