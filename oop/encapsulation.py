class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print(self.__secretCount)

   def get_count(self):
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter._JustCounter__secretCount)
counter.get_count()