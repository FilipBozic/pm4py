## Installation
### Docker
+ https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=94798094
+ compse version 1.24.1

### PM4Py
+ ```host$ docker pull javert899/pm4py:latest```
---
## Usage 
Make this working directory on host

### Start pm4py docker
+ ```host$ ./start_pm4py.sh```

### Run script in docker container
+ ```docker$ cd pm4py```
+ ```docker$ python pm-scripts/log2petrinet.py logs/running-example.xes```

### Transform dot to png on host (and view)
+ ```host$ ./dot2png_pm4py.sh running-example.dot```
