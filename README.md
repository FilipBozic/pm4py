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
+ Note: You can allways check log size (number of traces) with ```len(log)```

```python
from pm_scripts import constants, log_filters, utils

log = utils.load_log(constants.IEEE_LOG)
completed_only_log = log_filters.filter_complete_cases(log)

two_way_log = log_filters.filter_trace_attribute(completed_only_log, constants.INVOICE_TYPE, constants.TWO_WAY_MATCHER)
three_way_before_log = log_filters.filter_trace_attribute(completed_only_log, constants.INVOICE_TYPE, constants.THREE_WAY_BEFORE_MATCHER)
three_way_after_log = log_filters.filter_trace_attribute(completed_only_log, constants.INVOICE_TYPE, constants.THREE_WAY_AFTER_MATCHER)
consignment_log = log_filters.filter_trace_attribute(completed_only_log, constants.INVOICE_TYPE, constants.CONSIGNMENT_MATCHER)

# Show top trace variants
log_filters.get_top_n_variants(two_way_log)
```

```python
[{'variant': 'Vendor creates invoice,Create Purchase Order Item,Change Approval for Purchase Order,Record Invoice Receipt,Clear Invoice',
  'count': 76},
 {'variant': 'Change Approval for Purchase Order,Vendor creates invoice,Change Approval for Purchase Order,Create Purchase Order Item,Change Approval for Purchase Order,Record Invoice Receipt,Clear Invoice',
  'count': 15},
 {'variant': 'Change Approval for Purchase Order,Vendor creates invoice,Create Purchase Order Item,Record Invoice Receipt,Clear Invoice',
  'count': 13}]
```

```python
two_way_log_filtered = log_filters.auto_filter_variants(two_way_log)
three_way_before_log_filtered = log_filters.auto_filter_variants(three_way_before_log)
three_way_after_log_filtered = log_filters.auto_filter_variants(three_way_after_log)
consignment_log_filtered = log_filters.auto_filter_variants(consignment_log)

#Pick your miner (needs more filtering both on logs and during model creation)
from pm4py.algo.discovery.alpha import factory as alpha_miner
utils.save_log_to_dot(two_way_log_filtered, alpha_miner, 'two_way')
utils.save_log_to_dot(three_way_before_log_filtered, alpha_miner, 'three_way_before')
utils.save_log_to_dot(three_way_after_log_filtered, alpha_miner, 'three_way_after')
utils.save_log_to_dot(consignment_log_filtered, alpha_miner, 'consignment')
```

+ Mine traces with multiple items for one document
```python
from pm4py.algo.filtering.log.attributes import attributes_filter

po_stats = attributes_filter.get_trace_attribute_values(two_way_log, 'Purchasing Document')
po_stats = sorted(po_stats.items(), key=lambda x: x[1], reverse=True)
multi_item_po_log = log_filters.filter_trace_attribute(two_way_log, 'Purchasing Document', po_stats[0][0])

utils.save_log_to_xes(multi_item_po_log, 'multi_item_po')
utils.save_log_to_dot(multi_item_po_log, alpha_miner, 'multi_item_po')
```

### Transform dot to png on host (and view)
```
host$ ./dot2png_pm4py.sh two_way.dot
host$ ./dot2png_pm4py.sh three_way_before.dot
host$ ./dot2png_pm4py.sh three_way_after.dot
host$ ./dot2png_pm4py.sh consignment.dot
```


### Some numbers
```python
In [11]: len(log)
Out[11]: 251734

In [12]: len(completed_only_log)
Out[12]: 189451

In [4]: len(two_way_log)
Out[4]: 169

In [5]: len(three_way_before_log)
Out[5]: 179318

In [6]: len(three_way_after_log)
Out[6]: 9560

In [7]: len(consignment_log)
Out[7]: 404

```