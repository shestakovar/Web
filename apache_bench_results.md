## GET /dishes/
```bash
$ ab -c 10 -n 1000 http://localhost/api/v1/dishes/
```
<details><summary>Balanced</summary>

```
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)


Server Software:        Dish
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v1/dishes/
Document Length:        8483 bytes

Concurrency Level:      10
Time taken for tests:   16.600 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      8775000 bytes
HTML transferred:       8483000 bytes
Requests per second:    60.24 [#/sec] (mean)
Time per request:       166.003 [ms] (mean)
Time per request:       16.600 [ms] (mean, across all concurrent requests)
Transfer rate:          516.22 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       4
Processing:    23  163 131.1    154     426
Waiting:       23  163 131.1    153     426
Total:         23  163 131.1    154     426

Percentage of the requests served within a certain time (ms)
  50%    154
  66%    283
  75%    288
  80%    291
  90%    300
  95%    316
  98%    387
  99%    399
 100%    426 (longest request)
```
</details>

<details><summary>Unbalanced</summary>

```
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)


Server Software:        Dish
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v1/dishes/
Document Length:        8483 bytes

Concurrency Level:      10
Time taken for tests:   22.314 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      8775000 bytes
HTML transferred:       8483000 bytes
Requests per second:    44.81 [#/sec] (mean)
Time per request:       223.144 [ms] (mean)
Time per request:       22.314 [ms] (mean, across all concurrent requests)
Transfer rate:          384.03 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       5
Processing:    26  221  14.3    220     269
Waiting:       26  221  14.3    220     269
Total:         27  221  14.3    220     270

Percentage of the requests served within a certain time (ms)
  50%    220
  66%    223
  75%    225
  80%    227
  90%    231
  95%    236
  98%    248
  99%    254
 100%    270 (longest request)
```
</details>

## GET /dishes/1/
```bash
$ ab -c 10 -n 1000 http://localhost/api/v1/dishes/1/
```
<details><summary>Balanced</summary>

```
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)


Server Software:        Dish
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v1/dishes/1/
Document Length:        1292 bytes

Concurrency Level:      10
Time taken for tests:   5.800 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      1598000 bytes
HTML transferred:       1292000 bytes
Requests per second:    172.42 [#/sec] (mean)
Time per request:       57.997 [ms] (mean)
Time per request:       5.800 [ms] (mean, across all concurrent requests)
Transfer rate:          269.08 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0       8
Processing:     8   57  46.1     43     149
Waiting:        8   57  46.1     43     149
Total:          8   58  46.1     47     149

Percentage of the requests served within a certain time (ms)
  50%     47
  66%    100
  75%    103
  80%    104
  90%    109
  95%    114
  98%    119
  99%    125
 100%    149 (longest request)
```
</details>


<details><summary>Unbalanced</summary>

```
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)


Server Software:        Dish
Server Hostname:        localhost
Server Port:            80

Document Path:          /api/v1/dishes/1/
Document Length:        1292 bytes

Concurrency Level:      10
Time taken for tests:   8.305 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      1598000 bytes
HTML transferred:       1292000 bytes
Requests per second:    120.41 [#/sec] (mean)
Time per request:       83.052 [ms] (mean)
Time per request:       8.305 [ms] (mean, across all concurrent requests)
Transfer rate:          187.90 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0      10
Processing:     8   82   6.8     81     120
Waiting:        8   82   6.7     81     117
Total:          9   83   6.8     81     120

Percentage of the requests served within a certain time (ms)
  50%     81
  66%     82
  75%     83
  80%     85
  90%     89
  95%     92
  98%     98
  99%    101
 100%    120 (longest request)
```
</details>