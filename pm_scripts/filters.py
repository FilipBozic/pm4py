from os import path

from pm_scripts import constants
from pm_scripts import utils

from pm4py.algo.filtering.log.end_activities import end_activities_filter
from pm4py.algo.filtering.log.attributes import attributes_filter
from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.util import constants as pm4py_constants


def filter_complete_cases(log=None):
    if log is None:
        log = xes_importer.import_log(constants.IEEE_LOG)
        print("Loaded IEEE log with {} purchase order items".format(len(log)))

    filtered_log = end_activities_filter.apply(log, constants.COMPLETE_STATES)
    print("Removed ({}) incomplete cases from IEEE log".format(
        len(log) - len(filtered_log)))
    return filtered_log


def filter_invoice_type(invoice_type, log=None):
    if log is None:
        log = filter_complete_cases()
    # TODO FIX THIS SHIT, maybe completely wrong
    # attributes_filter.apply_events(log,
    #                            ["2-way match"],
    #                            parameters={
    #                                pm4py_constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY: constants.INVOICE_TYPE,
    #                                "positive": True})
    pass


def get_invoce_type_stastics(log=None):
    if log is None:
        log = filter_complete_cases()
    return attributes_filter.get_trace_attribute_values(log, constants.INVOICE_TYPE)
