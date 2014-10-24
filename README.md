abx
===

Apache Bench X

Test performance by increasing concurrency, outputs a CSV of mean/median/max response time and failure rate.

### Usage:
```
./abx.py time_per_test url_to_test
```

### Example:
```bash
./abx.py 10 http://gramercystudios.com/

running ab -c 5 -t 10 http://gramercystudios.com/
Finished 200 requests
running ab -c 10 -t 10 http://gramercystudios.com/
Finished 431 requests
running ab -c 15 -t 10 http://gramercystudios.com/
Finished 648 requests
running ab -c 20 -t 10 http://gramercystudios.com/
Finished 864 requests
running ab -c 25 -t 10 http://gramercystudios.com/
Finished 1099 requests
running ab -c 30 -t 10 http://gramercystudios.com/
Finished 1318 requests
running ab -c 40 -t 10 http://gramercystudios.com/
Finished 1780 requests
running ab -c 50 -t 10 http://gramercystudios.com/
Finished 2245 requests
running ab -c 60 -t 10 http://gramercystudios.com/
Finished 2686 requests
running ab -c 70 -t 10 http://gramercystudios.com/
Finished 3125 requests
running ab -c 80 -t 10 http://gramercystudios.com/
Finished 3565 requests
running ab -c 90 -t 10 http://gramercystudios.com/
Finished 4064 requests
running ab -c 100 -t 10 http://gramercystudios.com/
Finished 4527 requests


concurrency,total_mean,total_median,total_max,percentage_failed
5,247.0,236.0,703.0,0.0
10,229.0,232.0,331.0,0.0
15,229.0,229.0,363.0,0.0
20,229.0,228.0,438.0,0.0
25,225.0,225.0,459.0,0.0
30,225.0,226.0,541.0,0.0
40,222.0,223.0,525.0,0.0
50,220.0,220.0,343.0,0.0
60,221.0,222.0,482.0,0.0
70,221.0,221.0,333.0,0.0
80,222.0,222.0,373.0,0.0
90,219.0,219.0,458.0,0.0
100,218.0,219.0,337.0,0.0
```

![](http://i.imgur.com/LaOZT3D.png)
