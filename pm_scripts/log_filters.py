import copy
from os import path

from pm_scripts import constants
from pm_scripts import utils

from pm4py.algo.filtering.log.end_activities import end_activities_filter
from pm4py.algo.filtering.log.attributes import attributes_filter
from pm4py.objects.log import log as pm4py_log
from pm4py.util import constants as pm4py_constants


def filter_complete_cases(log):
    filtered_log = end_activities_filter.apply(log, constants.COMPLETE_STATES)
    print("Removed ({}) incomplete cases from IEEE log".format(len(log) - len(filtered_log)))
    return filtered_log


def filter_invoice_type(log, target_invoice_type):
    filtered_log = pm4py_log.EventLog(
        attributes=copy.deepcopy(log.attributes),
        extensions=copy.deepcopy(log.extensions),
        omni_present=copy.deepcopy(log.omni_present),
        classifiers=copy.deepcopy(log.classifiers)
    )
    for trace in log:
        new_trace = pm4py_log.Trace(attributes=copy.deepcopy(trace.attributes))
        if (trace.attributes[constants.INVOICE_TYPE] == target_invoice_type):
            for event in trace:
                new_event = copy.deepcopy(event)
                new_trace.append(new_event)
            filtered_log.append(new_trace)
    return filtered_log


def get_invoice_type_statistics(log):
    return attributes_filter.get_trace_attribute_values(log, constants.INVOICE_TYPE)
