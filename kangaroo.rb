#!/bin/ruby

require 'json'
require 'stringio'

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2)
    # Case 0
    # Same start, same velocity
    if x1 == x2 && v1 == v2
        return 'YES'
    end
    # Case 1 and 3
    # One of the kangaroos is starting ahead and staying ahead.
    if (x1 > x2 && v1 > v2) || (x2 > x1 && v2 > v1)
        return 'NO'
    end
    # Case 4 and 5
    # Same starting points but one is always faster
    if (v1 > v2 && x1 == x2) || (v2 > v1 && x2 == x1)
        return 'NO'
    end
    # Case 6
    # Different starting points but same velocity, so one will never catch up
    if v1 == v2 && x1 != x2
        return 'NO'
    end
    # Case 2a and 2b
    # Find the intersection :)
    jumps = (x2 - x1) / (v1 - v2)
    if x1 + (jumps * v1) == x2 + (jumps * v2)
        return 'YES'
    else
        return "NO"
    end
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

x1V1X2V2 = gets.rstrip.split

x1 = x1V1X2V2[0].to_i

v1 = x1V1X2V2[1].to_i

x2 = x1V1X2V2[2].to_i

v2 = x1V1X2V2[3].to_i

result = kangaroo x1, v1, x2, v2

fptr.write result
fptr.write "\n"

fptr.close()
