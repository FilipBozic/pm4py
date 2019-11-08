from importlib import import_module

from pm_scripts import constants

from pm4py.objects.log.exporter.xes import factory as xes_exporter
from pm4py.visualization.petrinet import factory as vis_factory


def load_log(log_path):
    base_module_name = "pm4py.objects.log.importer"
    extension = log_path.rsplit(".", 1)[1] if len(log_path.rsplit(".", 1)) == 2 else "xes"
    full_module_name = "{}.{}.factory".format(base_module_name, extension)

    log_importer = import_module(full_module_name)
    log = log_importer.import_log(log_path)
    print("Loaded {} log with {} events".format(log_path, len(log)))

    return log


def save_log_to_xes(log, xes_name):
    dest_file = _format_file_name_extension(xes_name, "xes")
    dest_file_path = "{}/{}".format(constants.LOGS_DIR, dest_file)
    xes_exporter.export_log(log, dest_file_path)

    print("Log saved as: {}".format(dest_file_path))


def save_log_to_dot(log, miner, dot_name):
    net, initial_marking, final_marking = miner.apply(log)
    gviz = vis_factory.apply(net, initial_marking, final_marking)
    dest_file = _format_file_name_extension(dot_name, "dot")
    gviz.save(dest_file, constants.RESULTS_DIR)

    print("Dot saved as: {}/{}".format(constants.RESULTS_DIR, dest_file))


def _format_file_name_extension(file_name, extension):
    return file_name if file_name.endswith(extension) else "{}.{}".format(file_name, extension)
