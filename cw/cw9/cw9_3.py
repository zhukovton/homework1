# import  pathlib
#
#
# class MypPath:
#     def __init__(self, bp=""):
#         self.bp = bp
#
#     def __truediv__(self, other: "MypPath" | str):
#         if isinstance(other, MypPath):
#             return MypPath(f"{self.bp}\\{other.bp}")
#
# path = pathlib.Path(pathlib.Path.home())
# print(path / "dir")
