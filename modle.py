#可以重复使用 载入-使用
#import / import 名称 as 别名
# import sys
# print(sys.platform)
# print(sys.maxsize)
# print(sys.path)

# import mainmd
# result=mainmd.dis(1,1,5,5)
# print(result)
#
# result=mainmd.slope(1,2,4,5)
# print(result)

import sys
sys.path.append("module")
print(sys.path)
import mainmd
print(mainmd.dis(1,1,5,5))

