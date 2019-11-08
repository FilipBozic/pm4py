# Project description
Utalization of [pm4py library](http://pm4py.org/) in order to solve [2019 PM BPI challange](https://icpmconference.org/2019/icpm-2019/contests-challenges/bpi-challenge-2019/)

## Installation
### Docker
+ https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=94798094
+ compse version 1.24.1

### PM4Py
+ ```host$ docker pull javert899/pm4py:latest```

### Graphviz
+ ```host$ sudo apt install graphviz```

---

## Usage
+ Make this working directory on host
+ IEEE 2019 log is to big for git, so [download it](icpmconference.org/2019/wp-content/uploads/sites/6/2019/01/log_IEEE.xes_.gz) and save it as 'logs/log_IEEE.xes'

### Start pm4py docker
+ ```host$ ./start_pm4py.sh```

### Start ipython in docker container
+ ```docker$ cd pm4py```
+ ```docker$ ipython```

### Mine ieee log in ipython
```python
from pm_scripts import constants, log_filters, utils

log = utils.load_log(constants.IEEE_LOG)
completed_only_log = log_filters.filter_complete_cases(log)
two_way_match_log = log_filters.filter_invoice_type(completed_only_log, constants.TWO_WAY_MATCHER)

#Pick your miner (needs more filtering both on logs and during model creation)
from pm4py.algo.discovery.alpha import factory as alpha_miner
utils.save_log_to_dot(two_way_match_log, alpha_miner, 'two_way_invoice')

```

### Transform dot to png on host (and view)
+ ```host$ ./dot2png_pm4py.sh two_way_invoice.dot```
