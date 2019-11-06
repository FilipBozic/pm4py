# Transform dot file to png and save in writable dir
if [ $# -lt 1 ]; then
  echo 1>&2 "$0: missing dot file name"
  exit 2
fi

src_dir=./results-docker
dest_dir=./results
dest_file=$dest_dir/$1.png
mkdir -p $dest_dir
dot -T png $src_dir/$1 > $dest_file
echo "Petrinet saved as: $dest_file"

xdg-open $dest_file
