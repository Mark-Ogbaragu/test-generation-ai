# AI Test Generator - AI for Software Engineering
def generate_test(function_code):
    """Simple AI concept: auto-generates test template"""
    func_name = function_code.split('def ')[1].split('(')[0]
    test = f"""
def test_{func_name}():
    # Auto-generated test
    result = {func_name}(2, 3)
    assert result is not None
    print(f"Test for {func_name} passed!")
"""
    return test

# Example
sample = "def add(a,b): return a+b"
print(generate_test(sample))
