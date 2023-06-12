# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

count_of_open = len(yelp_business[yelp_business['is_open'] == 1])
type(count_of_open)

Explanation :
1. yelp_business = nama dataframe
2. ['is_open'] = nama column dari dataframe yang ingin kita pakai
3. [yelp_business['is_open'] == 1] <- mengecek kondisi business yang open (boolean condition atau filter condition)
4. yelp_business[yelp_business['is_open'] == 1 <- nama dataframe (sebelum bracket [] dengan filter condition)
5. len = menghitung sesuai kondisi
