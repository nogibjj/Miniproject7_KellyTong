```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen FROM women_stemDB GROUP BY Major ORDER BY SumTotal DESC LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=7017725, SumWomen=4223675), Row(Major='NURSING', SumTotal=5234850, SumWomen=4690525), Row(Major='COMPUTER SCIENCE', SumTotal=3207975, SumWomen=714400), Row(Major='MECHANICAL ENGINEERING', SumTotal=2280675, SumWomen=272675), Row(Major='ELECTRICAL ENGINEERING', SumTotal=2038175, SumWomen=400400), Row(Major='MATHEMATICS', SumTotal=1809925, SumWomen=811025), Row(Major='CHEMISTRY', SumTotal=1663250, SumWomen=840175), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=1551300, SumWomen=875925), Row(Major='GENERAL ENGINEERING', SumTotal=1528800, SumWomen=386725), Row(Major='CIVIL ENGINEERING', SumTotal=1328825, SumWomen=301800)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen 
            FROM women_stemDB 
            GROUP BY Major 
            ORDER BY SumTotal DESC 
            LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=7298434, SumWomen=4392622), Row(Major='NURSING', SumTotal=5444244, SumWomen=4878146), Row(Major='COMPUTER SCIENCE', SumTotal=3336294, SumWomen=742976), Row(Major='MECHANICAL ENGINEERING', SumTotal=2371902, SumWomen=283582), Row(Major='ELECTRICAL ENGINEERING', SumTotal=2119702, SumWomen=416416), Row(Major='MATHEMATICS', SumTotal=1882322, SumWomen=843466), Row(Major='CHEMISTRY', SumTotal=1729780, SumWomen=873782), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=1613352, SumWomen=910962), Row(Major='GENERAL ENGINEERING', SumTotal=1589952, SumWomen=402194), Row(Major='CIVIL ENGINEERING', SumTotal=1381978, SumWomen=313872)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen 
            FROM women_stemDB 
            GROUP BY Major 
            ORDER BY SumTotal DESC 
            LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=7579143, SumWomen=4561569), Row(Major='NURSING', SumTotal=5653638, SumWomen=5065767), Row(Major='COMPUTER SCIENCE', SumTotal=3464613, SumWomen=771552), Row(Major='MECHANICAL ENGINEERING', SumTotal=2463129, SumWomen=294489), Row(Major='ELECTRICAL ENGINEERING', SumTotal=2201229, SumWomen=432432), Row(Major='MATHEMATICS', SumTotal=1954719, SumWomen=875907), Row(Major='CHEMISTRY', SumTotal=1796310, SumWomen=907389), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=1675404, SumWomen=945999), Row(Major='GENERAL ENGINEERING', SumTotal=1651104, SumWomen=417663), Row(Major='CIVIL ENGINEERING', SumTotal=1435131, SumWomen=325944)]
```

