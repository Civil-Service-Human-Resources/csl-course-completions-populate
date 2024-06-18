import sys
import plan
import apply
import revert

step = sys.argv[1]
    
if step == "plan":
    plan.plan()

if step  == "apply":
    apply.apply()

if step == "revert":
    revert.revert()