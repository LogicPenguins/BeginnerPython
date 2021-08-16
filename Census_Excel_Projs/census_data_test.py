import os
import census2010

anchorage_pop = census2010.all_data['AK']['Anchorage']['pop']
print(f'The 2010 population of Anchorage was {anchorage_pop} people.')