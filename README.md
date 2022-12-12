## Most Active Cookie

A command line program in Python 3 language to process a csv log file and return the nth active cookie for a specific day

### CSV file example

|cookie          |timestamp                |
|----------------|-------------------------|
|AtY0laUfhglK3lC7|2018-12-09T14:19:00+00:00|
|SAZuXPGUrfbcn5UA|2018-12-09T10:13:00+00:00|
|5UAVanZf6UtGyKVS|2018-12-09T07:25:00+00:00|
|AtY0laUfhglK3lC7|2018-12-09T06:19:00+00:00|
|SAZuXPGUrfbcn5UA|2018-12-08T22:03:00+00:00|
|4sMM2LxV07bPJzwf|2018-12-08T21:30:00+00:00|
|fbcn5UAVanZf6UtG|2018-12-08T09:30:00+00:00|
|4sMM2LxV07bPJzwf|2018-12-07T23:30:00+00:00|


### Usage

The only reuiement to run the application is Python3

> $ python3 -f path-of-the-csv-file -d date-in-form-of (dd-mm-yyyy)

Eaxmple
> $ python3 -f cookie_log.csv -d 2018-12-09

for more info about the parameters:

> $ python3 --help
```
optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Cookie file path
  -d DATE, --date DATE  Specify the date (dd-mm-yyyy)
  -n N, --n N           [optional] The nth most active cookie. default is 0 which means the most
                        active.
```

To run the unit/integration tests. in root dir, run:

> $ python3 -m unittest

#### Example output to stdout:
most active cookie or cookies printed in seperate lines.
``` 
AtY0laUfhglK3lC7 
AtY0laUfhglK3lC8
```

```
No logs found
```