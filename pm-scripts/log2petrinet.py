import argparse

from pm4py.algo.discovery.alpha import factory as alpha_miner
from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.visualization.petrinet import factory as vis_factory

DEST_SRC = './results-docker'
parser = argparse.ArgumentParser(
    description='Transforms xes log file to petrinet and save in dot format'
)
parser.add_argument('log_filepath', type=str, help='path log file')
args = parser.parse_args()

log = xes_importer.import_log(args.log_filepath)
net, initial_marking, final_marking = alpha_miner.apply(log)
gviz = vis_factory.apply(net, initial_marking, final_marking)

dest_file = '{}.dot'.format(args.log_filepath.split('/')[-1].split('.')[0])
gviz.save(dest_file, DEST_SRC)

print('Petrinet saved as: {}/{}'.format(DEST_SRC, dest_file))
