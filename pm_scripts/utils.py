from importlib import import_module

from pm_scripts import constants

from pm4py.visualization.petrinet import factory as vis_factory


def load_log(log_path):
    base_module_name = "pm4py.objects.log.importer"
    extension = log_path.rsplit(".", 1)[1] if len(log_path.rsplit(".", 1)) == 2 else "xes"
    full_module_name = "{}.{}.factory".format(base_module_name, extension)

    log_importer = import_module(full_module_name)
    log = log_importer.import_log(log_path)
    print("Loaded {} log with {} events".format(log_path, len(log)))

    return log


def save_log_to_dot(log, miner, dot_name):
    net, initial_marking, final_marking = miner.apply(log)
    gviz = vis_factory.apply(net, initial_marking, final_marking)

    dest_file = '{}.dot'.format(dot_name)
    gviz.save(dest_file, constants.RESULTS_DIR)

    print('Petrinet saved as: {}/{}'.format(constants.RESULTS_DIR, dest_file))
