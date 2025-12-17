import pkg1.arithmetic
import pkg2.string_ops

a=5
b=2
name="sunbeam"
print(f"{a}+{b}={pkg1.arithmetic.add(a,b)}")
print(f"{a}*{b}={pkg1.arithmetic.mul(a,b)}")
print(f"original str = {name}\treversed str = {pkg2.string_ops.str_rev(name)}")
print(f"vowel count = {pkg2.string_ops.vowelcount(name)}")
